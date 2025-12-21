import os
import openai  # We'll assume Novita API works like OpenAI API
import markdown

# ✅ Use your Novita API key from .env or environment variables
NOVITA_API_KEY = os.getenv("NOVITA_API_KEY")
openai.api_key = NOVITA_API_KEY

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
md_path = os.path.join(BASE_DIR, "docs", "content.md")
html_path = os.path.join(BASE_DIR, "docs", "index.html")
css_path = os.path.join(BASE_DIR, "docs", "style.css")

# Read Markdown
with open(md_path, "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert to basic HTML
html_body = markdown.markdown(md_text)

# Example CSS (you can enhance)
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
"""

# Wrap HTML body in a basic template
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

# Save files
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print(f"✅ Website generated at {html_path} with CSS")
