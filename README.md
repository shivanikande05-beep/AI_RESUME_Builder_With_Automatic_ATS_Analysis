# 🚀 Resume ATS Analyzer + AI Resume Generator
An advanced web application that analyzes resumes using a custom ATS engine and generates clean, professional PDF/TXT resumes — all without using any external APIs.
## Author : https://www.linkedin.com/in/shivnanda-kande-382a22383/?utm_source=share_via&utm_content=profile&utm_medium=member_android
This project is built using:
🟦 **Python (Flask)**
🟩 **HTML / CSS (Dark Mode UI)**
🟨 **JavaScript**
🗂 **SQLite Database**
📄 **ReportLab PDF Generator**

Deployed using **Render.com** (free hosting).

---

## 📌 Features

### ✅ **1. Resume ATS Score**

* Upload any resume (.pdf, .txt, .docx)
* Extracts text
* Compares with Job Description
* Calculates ATS score
* Highlights missing keywords
* Only matches **real technical keywords**
* Supports fuzzy matching

### ✅ **2. AI-Style Resume Generator**

* Fill form with:

  * Name
  * Email
  * Phone
  * Summary
  * Skills
  * Experience
  * Projects
* Generates:

  * 📄 **Professional PDF Resume**
  * 📄 **Clean TXT Resume**

### ✅ **3. Dark Mode Modern UI**

* Premium SaaS-style UI
* Responsive design
* Glassmorphism
* Perfect for portfolio projects

### ✅ **4. SQLite Database**

* Stores uploaded resumes
* Stores analysis logs

### ✅ **5. No API Keys Needed**

* Everything works offline
* No OpenAI or external APIs

---

## 🗂 **Project Structure**

```
resume-ats-builder/
│── backend/
│   ├── app.py                # Main Flask app
│   ├── ats.py                # ATS scoring logic
│   ├── extract.py            # Resume text extraction
│   ├── generate_resume.py    # PDF/TXT resume generator
│   ├── database.db           # SQLite DB
│
│── static/
│   ├── style.css             # Dark mode UI design
│
│── templates/
│   ├── index.html            # Home page (upload + form)
│   ├── result.html           # ATS result page
│
│── requirements.txt          # Python dependencies
│── start.sh                  # Render startup script
│── README.md                 # Documentation (this file)
```

---

## ⚙️ **Installation (Local Development)**

### 🔧 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/resume-ats-builder
cd resume-ats-builder
```

### 🔧 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 🔧 3. Install Dependencies

```
pip install -r requirements.txt
```

### 🔧 4. Run the App

```
cd backend
python app.py
```

App runs on:

```
http://127.0.0.1:5000
```

---

## 🚀 **Deployment Guide (Render.com)**

### 1️⃣ Add required files:

* `requirements.txt`
* `start.sh`

**start.sh**

```bash
#!/bin/bash
gunicorn backend.app:app --bind 0.0.0.0:$PORT
```

### 2️⃣ Push to GitHub

```
git add .
git commit -m "ready for deploy"
git push
```

### 3️⃣ Deploy on Render

* Create account → [https://render.com](https://render.com)
* New Web Service
* Select GitHub repo
* Fill details:

| Setting       | Value                           |
| ------------- | ------------------------------- |
| Runtime       | Python                          |
| Build Command | pip install -r requirements.txt |
| Start Command | bash start.sh                   |
| Instance      | Free                            |
| Region        | Singapore                       |

Render gives you a live URL:

```
https://resume-ats-builder.onrender.com
```

---

## 🧠 **How ATS Scoring Works**

The ATS engine analyzes:

### ✔ Technical keywords

React, Node, Express, MongoDB, PostgreSQL, Docker, AWS, Webpack, Vite, Socket.IO, etc.

### ✔ Fuzzy text matching

Matches similar keywords:

* "react.js" → React
* "nodejs" → Node
* "socketio" → Socket.IO

### ❌ Ignores:

* Marketing words
* Numbers
* Company intro text
* Non-technical fluff

This makes score accurate and professional.

---

## 📄 **PDF Resume Generator Features**

* Clean one-page layout
* No box symbols or broken formatting
* Uses ReportLab
* Works offline
* Supports long text wrapping
* Dark mode-compatible

---

## 🛠 **Tech Stack**

| Area            | Technology                |
| --------------- | ------------------------- |
| Frontend        | HTML, CSS (Dark Mode), JS |
| Backend         | Flask (Python)            |
| File Processing | PyPDF2, python-docx       |
| PDF Generator   | ReportLab                 |
| Database        | SQLite                    |
| Deployment      | Render                    |

---

## 📸 Screenshots (Optional)

*(If you want, you can add images later)*

---

## 🤝 Contributing

Pull requests are welcome!# 🚀 Resume ATS Analyzer + AI Resume Generator

An advanced web application that analyzes resumes using a custom ATS engine and generates clean, professional PDF/TXT resumes — all without using any external APIs.

This project is built using:
🟦 **Python (Flask)**
🟩 **HTML / CSS (Dark Mode UI)**
🟨 **JavaScript**
🗂 **SQLite Database**
📄 **ReportLab PDF Generator**

Deployed using **Render.com** (free hosting).

---

## 📌 Features

### ✅ **1. Resume ATS Score**

* Upload any resume (.pdf, .txt, .docx)
* Extracts text
* Compares with Job Description
* Calculates ATS score
* Highlights missing keywords
* Only matches **real technical keywords**
* Supports fuzzy matching

### ✅ **2. AI-Style Resume Generator**

* Fill form with:

  * Name
  * Email
  * Phone
  * Summary
  * Skills
  * Experience
  * Projects
* Generates:

  * 📄 **Professional PDF Resume**
  * 📄 **Clean TXT Resume**

### ✅ **3. Dark Mode Modern UI**

* Premium SaaS-style UI
* Responsive design
* Glassmorphism
* Perfect for portfolio projects

### ✅ **4. SQLite Database**

* Stores uploaded resumes
* Stores analysis logs

### ✅ **5. No API Keys Needed**

* Everything works offline
* No OpenAI or external APIs

---

## 🗂 **Project Structure**

```
resume-ats-builder/
│── backend/
│   ├── app.py                # Main Flask app
│   ├── ats.py                # ATS scoring logic
│   ├── extract.py            # Resume text extraction
│   ├── generate_resume.py    # PDF/TXT resume generator
│   ├── database.db           # SQLite DB
│
│── static/
│   ├── style.css             # Dark mode UI design
│
│── templates/
│   ├── index.html            # Home page (upload + form)
│   ├── result.html           # ATS result page
│
│── requirements.txt          # Python dependencies
│── start.sh                  # Render startup script
│── README.md                 # Documentation (this file)
```

---

## ⚙️ **Installation (Local Development)**

### 🔧 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/resume-ats-builder
cd resume-ats-builder
```

### 🔧 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 🔧 3. Install Dependencies

```
pip install -r requirements.txt
```

### 🔧 4. Run the App

```
cd backend
python app.py
```

App runs on:

```
http://127.0.0.1:5000
```

---

## 🚀 **Deployment Guide (Render.com)**

### 1️⃣ Add required files:

* `requirements.txt`
* `start.sh`

**start.sh**

```bash
#!/bin/bash
gunicorn backend.app:app --bind 0.0.0.0:$PORT
```

### 2️⃣ Push to GitHub

```
git add .
git commit -m "ready for deploy"
git push
```

### 3️⃣ Deploy on Render

* Create account → [https://render.com](https://render.com)
* New Web Service
* Select GitHub repo
* Fill details:

| Setting       | Value                           |
| ------------- | ------------------------------- |
| Runtime       | Python                          |
| Build Command | pip install -r requirements.txt |
| Start Command | bash start.sh                   |
| Instance      | Free                            |
| Region        | Singapore                       |

Render gives you a live URL:

```
https://resume-ats-builder.onrender.com
```

---

## 🧠 **How ATS Scoring Works**

The ATS engine analyzes:

### ✔ Technical keywords

React, Node, Express, MongoDB, PostgreSQL, Docker, AWS, Webpack, Vite, Socket.IO, etc.

### ✔ Fuzzy text matching

Matches similar keywords:

* "react.js" → React
* "nodejs" → Node
* "socketio" → Socket.IO

### ❌ Ignores:

* Marketing words
* Numbers
* Company intro text
* Non-technical fluff

This makes score accurate and professional.

---

## 📄 **PDF Resume Generator Features**

* Clean one-page layout
* No box symbols or broken formatting
* Uses ReportLab
* Works offline
* Supports long text wrapping
* Dark mode-compatible

---

## 🛠 **Tech Stack**

| Area            | Technology                |
| --------------- | ------------------------- |
| Frontend        | HTML, CSS (Dark Mode), JS |
| Backend         | Flask (Python)            |
| File Processing | PyPDF2, python-docx       |
| PDF Generator   | ReportLab                 |
| Database        | SQLite                    |
| Deployment      | Render                    |

---

## 📸 Screenshots (Optional)

*(If you want, you can add images later)*

---

## 🤝 Contributing

Pull requests are welcome!
