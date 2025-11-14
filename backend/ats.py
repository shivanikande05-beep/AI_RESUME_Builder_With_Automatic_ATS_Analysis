import re
from collections import Counter

# -----------------------------------------------------------
# REAL ATS: ONLY MATCH TECH SKILLS, TOOLS, FRAMEWORKS, PATTERNS
# -----------------------------------------------------------

TECH_KEYWORDS = {
    # Frontend
    "html", "css", "javascript", "react", "redux", "angular", "vue",
    "tailwind", "bootstrap", "vite", "webpack",

    # Backend
    "node", "nodejs", "express", "django", "flask", "fastapi",
    "php", "laravel", "java", "spring", "ruby", "rails", ".net",

    # Databases
    "mysql", "postgresql", "postgres", "mongodb", "oracle", "nosql", "sql",

    # APIs
    "rest", "restful", "api", "json",

    # Realtime
    "websocket", "socket.io",

    # Cloud
    "aws", "ec2", "s3", "lambda", "azure", "gcp",

    # DevOps
    "docker", "kubernetes", "ci", "cd", "git", "github", "pm2",

    # Patterns
    "pubsub", "pub/sub", "event", "event-driven", "middleware",
    "mvc", "microservices",

    # Testing
    "jest", "mocha", "chai", "pytest",

    # AI/ML (optional)
    "tensorflow", "sklearn", "numpy", "pandas", "matplotlib"
}

STOPWORDS = {
    "and","or","the","a","an","to","with","for","in","on","of","by","at","from",
    "as","is","are","be","this","that","it","you","your","we","our","i","my","me",
    "will","have","has","had","can","should","may","such","other","than","etc",
    "developer","development","developers","experience","skills","years","job",
    "role","responsible","requirements","preferred","good","must","should",
    "ability","proficiency","familiarity","nice","understanding","strong"
}

def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s\-+#/.]", " ", text)
    tokens = [t.strip() for t in text.split() if t.strip()]
    return tokens

def extract_keywords(text):
    tokens = tokenize(text)
    filtered = []

    for t in tokens:
        if t in STOPWORDS:
            continue

        # check for tech keywords
        if t in TECH_KEYWORDS:
            filtered.append(t)

        # accept combinations like react.js or node.js
        if "react" in t:
            filtered.append("react")
        if "node" in t:
            filtered.append("node")
        if "express" in t:
            filtered.append("express")
        if "docker" in t:
            filtered.append("docker")
        if "socket" in t:
            filtered.append("websocket")

    return list(set(filtered))

def calculate_ats_score(resume_text, jd_text):
    jd_keywords = extract_keywords(jd_text)
    resume_keywords = extract_keywords(resume_text)

    if not jd_keywords:
        return 0, [], {"reason": "No technical keywords found in JD."}

    matched = [kw for kw in jd_keywords if kw in resume_keywords]
    missing = [kw for kw in jd_keywords if kw not in matched]

    match_pct = len(matched) / len(jd_keywords)
    score = int(match_pct * 100)

    return score, missing, {
        "matched_keywords": matched,
        "total_keywords": len(jd_keywords),
        "match_percentage": round(match_pct * 100, 2)
    }
