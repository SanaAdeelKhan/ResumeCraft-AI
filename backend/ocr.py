from paddleocr import PaddleOCR
from pdf2image import convert_from_path
import os

# ✅ Poppler path (Windows fix)
POPPLER_PATH = r"C:\Users\Muhammad Adeel Khan\Release-25.12.0-0\poppler-25.12.0\Library\bin"

# ✅ Absolute path to PDF file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
PDF_PATH = os.path.join(BASE_DIR, "SANAADEEL-CV.pdf")

ocr = PaddleOCR(use_textline_orientation=True, lang='en')  # Updated parameter

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    extracted_text = []

    for img in images:
        result = ocr.ocr(img)
        if result and result[0]:
            for line in result[0]:
                extracted_text.append(line[1][0])

    return "\n".join(extracted_text)

if __name__ == "__main__":
    print("📄 Reading PDF from:", PDF_PATH)

    text = extract_text_from_pdf(PDF_PATH)

    with open("resume_raw.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("✅ OCR extraction completed successfully")
