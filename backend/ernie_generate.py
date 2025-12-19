import os
import requests

API_KEY = os.getenv("NOVITA_API_KEY")

API_URL = "https://api.novita.ai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

PROMPT_TEMPLATE = """
You are a professional web portfolio designer.

Transform the following resume content into a modern, elegant,
single-page personal website with:

- Hero section (name + tagline)
- About Me
- Skills
- Experience
- Projects
- Contact section

Use clean Markdown.

Resume Content:
{content}
"""

def generate_portfolio(md_content):
    payload = {
        "model": "ernie-4.5",
        "messages": [
            {"role": "user", "content": PROMPT_TEMPLATE.format(content=md_content)}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    with open("../web/content.md", encoding="utf-8") as f:
        md = f.read()

    refined = generate_portfolio(md)

    with open("../web/content.md", "w", encoding="utf-8") as f:
        f.write(refined)

    print("✅ ERNIE portfolio content generated")
