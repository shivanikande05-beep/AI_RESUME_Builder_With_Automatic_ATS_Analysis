# backend/extract.py
import os
import io

def extract_text_from_pdf(path):
    try:
        from PyPDF2 import PdfReader
    except Exception as e:
        raise RuntimeError("PyPDF2 not installed") from e

    text = []
    with open(path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text).strip()

def extract_text_from_docx(path):
    try:
        from docx import Document
    except Exception as e:
        raise RuntimeError("python-docx not installed") from e

    doc = Document(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text and p.text.strip()]
    return "\n".join(paragraphs).strip()

def extract_text_from_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def extract_text_from_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(path)
    if ext == ".docx":
        return extract_text_from_docx(path)
    if ext == ".txt":
        return extract_text_from_txt(path)
    return ""
