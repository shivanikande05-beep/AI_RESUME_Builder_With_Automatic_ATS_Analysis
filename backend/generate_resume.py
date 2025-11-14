# backend/generate_resume.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import textwrap
import tempfile
import os

# helper to wrap long text
def draw_wrapped_text(c, text, x, y, max_width=500, line_height=14, font="Helvetica", size=10):
    c.setFont(font, size)
    wrapped = textwrap.wrap(text, width=90)
    for line in wrapped:
        c.drawString(x, y, line)
        y -= line_height
    return y

def draw_section_title(c, title, x, y):
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, title)
    y -= 4
    c.setLineWidth(1)
    c.line(x, y, 550, y)
    return y - 10

def create_pdf_from_dict(data):
    fd, path = tempfile.mkstemp(suffix=".pdf")
    os.close(fd)

    c = canvas.Canvas(path, pagesize=letter)
    x = 50
    y = 760

    # ---- HEADER ----
    c.setFont("Helvetica-Bold", 18)
    c.drawString(x, y, data.get("name", ""))
    y -= 25

    c.setFont("Helvetica", 10)
    c.drawString(x, y, f"{data.get('email', '')}  |  {data.get('phone', '')}")
    y -= 20

    # ---- SUMMARY ----
    y = draw_section_title(c, "SUMMARY", x, y)
    y = draw_wrapped_text(c, data.get("summary", ""), x, y)

    # ---- EXPERIENCE ----
    y = draw_section_title(c, "EXPERIENCE", x, y)
    for line in data.get("experience", "").split("\n"):
        if line.strip():
            bullet = "• " + line.strip()
            y = draw_wrapped_text(c, bullet, x, y)
            y -= 4

    # ---- SKILLS ----
    y = draw_section_title(c, "SKILLS", x, y)
    y = draw_wrapped_text(c, data.get("skills", ""), x, y)

    # ---- PROJECTS ----
    y = draw_section_title(c, "PROJECTS", x, y)
    for line in data.get("projects", "").split("\n"):
        if line.strip():
            bullet = "• " + line.strip()
            y = draw_wrapped_text(c, bullet, x, y)
            y -= 4

    c.save()
    return path

def create_txt_from_dict(data):
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)

    with open(path, "w", encoding="utf-8") as f:
        for key, val in data.items():
            f.write(f"{key.upper()}:\n{val}\n\n")
    return path
