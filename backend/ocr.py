from paddleocr import PaddleOCR
from pdf2image import convert_from_path
import os

POPPLER_PATH = r"C:\Users\Muhammad Adeel Khan\Release-25.12.0-0\poppler-25.12.0\Library\bin"

ocr = PaddleOCR(use_textline_orientation=True, lang='en')

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    extracted_text = []

    for img in images:
        # PaddleOCR expects numpy array or path
        result = ocr.ocr(img, cls=True)
        if result and result[0]:
            for line in result[0]:
                extracted_text.append(line[1][0])
    
    return "\n".join(extracted_text)

if __name__ == "__main__":
    pdf_file = os.path.join("..", "SANAADEEL-CV.pdf")
    text = extract_text_from_pdf(pdf_file)

    raw_path = os.path.join("resume_raw.txt")
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"✅ OCR extraction completed. Saved to {raw_path}")
