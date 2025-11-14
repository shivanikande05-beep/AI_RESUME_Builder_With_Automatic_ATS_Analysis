# backend/app.py
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import sqlite3
import os
import tempfile
from werkzeug.utils import secure_filename
from extract import extract_text_from_file
from ats import calculate_ats_score
from generate_resume import create_pdf_from_dict, create_txt_from_dict
from datetime import datetime

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "dev-key-for-local"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        resume_text TEXT,
        job_description TEXT,
        ats_score INTEGER,
        missing_keywords TEXT,
        created_at TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    jd = request.form.get("job_description", "").strip()
    file = request.files.get("resume_file")

    if not jd:
        flash("Job description is required", "error")
        return redirect(url_for("index"))

    if not file or file.filename == "":
        flash("Please upload a resume file (pdf/docx/txt)", "error")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash("File type not allowed. Use pdf, docx, or txt.", "error")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    saved_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{datetime.now().timestamp()}_{filename}")
    file.save(saved_path)

    resume_text = extract_text_from_file(saved_path)
    ats_score, missing, details = calculate_ats_score(resume_text, jd)

    # store in sqlite
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO resumes (filename, resume_text, job_description, ats_score, missing_keywords, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (filename, resume_text, jd, ats_score, ",".join(missing), datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

    return render_template("result.html",
                           resume_text=resume_text,
                           job_description=jd,
                           score=ats_score,
                           missing=missing,
                           details=details)

@app.route("/generate", methods=["POST"])
def generate():
    # Form fields for resume generation
    data = {
        "name": request.form.get("name",""),
        "email": request.form.get("email",""),
        "phone": request.form.get("phone",""),
        "summary": request.form.get("summary",""),
        "experience": request.form.get("experience",""),
        "education": request.form.get("education",""),
        "skills": request.form.get("skills",""),
        "projects": request.form.get("projects","")
    }

    out_pdf = create_pdf_from_dict(data)
    out_txt = create_txt_from_dict(data)

    # send PDF by default; allow user to download txt via link on result page
    return send_file(out_pdf, as_attachment=True, download_name="generated_resume.pdf")

@app.route("/download_txt", methods=["POST"])
def download_txt():
    data = request.json or {}
    out_txt = create_txt_from_dict(data)
    return send_file(out_txt, as_attachment=True, download_name="generated_resume.txt")

if __name__ == "__main__":
    app.run(debug=True)
