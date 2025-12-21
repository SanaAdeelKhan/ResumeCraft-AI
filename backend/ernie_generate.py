import os
import openai  # Use Novita API like OpenAI API
import markdown

# ✅ Get your Novita API key from environment variable or .env
NOVITA_API_KEY = os.getenv("NOVITA_API_KEY")
openai.api_key = NOVITA_API_KEY

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_path = os.path.join(BASE_DIR, "resume_raw.txt")
md_path = os.path.join(BASE_DIR, "docs", "content.md")
html_path = os.path.join(BASE_DIR, "docs", "index.html")
css_path = os.path.join(BASE_DIR, "docs", "style.css")

# Read raw OCR text
with open(raw_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# ✅ Ask ERNIE to convert raw resume text into Markdown with sections: Name, Contact, Skills, Education, Experience
prompt = f"""
Convert the following resume text into a modern, readable Markdown format suitable for a personal profile website.
Include sections: Name, Email, Phone, Education, Skills, Experience.
Use lists, headings, and make it visually clear.

Resume text:
{raw_text}
"""

response = openai.ChatCompletion.create(
    model="gpt-4",  # substitute with ERNIE model if using Novita API
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)

md_text = response['choices'][0]['message']['content']

# Save Markdown
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_text)

# Convert Markdown to HTML
html_body = markdown.markdown(md_text)

# Example CSS (enhance as you like)
css_content = """
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    max-width: 900px;
    margin: auto;
    padding: 40px;
    background-color: #f5f5f5;
    color: #333;
}
h1, h2 {
    color: #1a73e8;
}
ul {
    list-style: square;
    margin-left: 20px;
}
"""

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ResumeCraft-AI</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
{html_body}
</body>
</html>
"""

# Save HTML and CSS
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print(f"✅ ERNIE-powered website generated at {html_path}")
