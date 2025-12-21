import os
import re

def parse_resume(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    info = {}

    # Name: assume first non-empty line
    info["name"] = lines[0] if lines else "Name Unknown"

    # Email
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    info["email"] = email_match.group(0) if email_match else "Email not found"

    # Phone number
    phone_match = re.search(r"\+?\d[\d\s-]{7,}\d", text)
    info["phone"] = phone_match.group(0) if phone_match else "Phone not found"

    # Skills: search for common patterns like "Skills", "Technical Skills", or bullet points
    skills = []
    for i, line in enumerate(lines):
        if "skill" in line.lower():
            # next 5 lines as possible skills
            skills = [s.strip("-• ") for s in lines[i+1:i+6] if s.strip()]
            break
    info["skills"] = skills if skills else ["Skills not found"]

    # Education: lines after "Education" or "Academic"
    edu = []
    for i, line in enumerate(lines):
        if "education" in line.lower() or "academic" in line.lower():
            edu = [lines[j] for j in range(i+1, min(i+5, len(lines))) if lines[j].strip()]
            break
    info["education"] = edu if edu else ["Education info not found"]

    # Optional: add Experience parsing if you like
    exp = []
    for i, line in enumerate(lines):
        if "experience" in line.lower() or "work" in line.lower():
            exp = [lines[j] for j in range(i+1, min(i+6, len(lines))) if lines[j].strip()]
            break
    info["experience"] = exp if exp else ["Experience info not found"]

    return info

def to_markdown(info):
    return f"""
# {info['name']}

**Email:** {info['email']}  
**Phone:** {info['phone']}

## Education
- {"\n- ".join(info['education'])}

## Skills
- {"\n- ".join(info['skills'])}

## Experience
- {"\n- ".join(info['experience'])}
"""

if __name__ == "__main__":
    # Correct absolute path to the OCR text
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
    raw_path = os.path.join(BASE_DIR, "backend", "resume_raw.txt")

    # Read OCR text
    with open(raw_path, encoding="utf-8") as f:
        raw = f.read()

    print("📝 OCR text preview:\n", raw[:500], "\n...")  # optional: preview first 500 chars

    info = parse_resume(raw)
    md = to_markdown(info)

    # Output markdown to docs folder
    output_path = os.path.join(BASE_DIR, "docs", "content.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"✅ Markdown generated at: {output_path}")
