import os
import re

def parse_resume(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    info = {}

    info["name"] = lines[0] if lines else "Name Unknown"

    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    info["email"] = email_match.group(0) if email_match else "Email not found"

    phone_match = re.search(r"\+?\d[\d\s-]{7,}\d", text)
    info["phone"] = phone_match.group(0) if phone_match else "Phone not found"

    # Skills
    skills = []
    for i, line in enumerate(lines):
        if "skill" in line.lower():
            skills = [s.strip("-• ") for s in lines[i+1:i+6]]
            break
    info["skills"] = skills if skills else ["Skills not found"]

    # Education
    edu = []
    for i, line in enumerate(lines):
        if "education" in line.lower():
            edu = [lines[j] for j in range(i+1, min(i+4, len(lines)))]
            break
    info["education"] = edu if edu else ["Education info not found"]

    # Experience
    exp = []
    for i, line in enumerate(lines):
        if "experience" in line.lower():
            exp = [lines[j] for j in range(i+1, min(i+4, len(lines)))]
            break
    info["experience"] = exp if exp else ["Experience info not found"]

    return info

if __name__ == "__main__":
    raw_path = os.path.join("resume_raw.txt")
    with open(raw_path, encoding="utf-8") as f:
        raw_text = f.read()
    
    info = parse_resume(raw_text)
    print("✅ Parsed resume info:", info)
