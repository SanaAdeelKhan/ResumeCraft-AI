def to_markdown(text):
    return f"""
# Resume Content

## Extracted Information
{text}

## Skills
- Python
- AI / Machine Learning
- Web Development

## Experience
- Automatically parsed from resume
"""

if __name__ == "__main__":
    with open("resume_raw.txt", encoding="utf-8") as f:
        raw = f.read()

    md = to_markdown(raw)

    with open("../web/content.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("✅ Markdown generated")
