from paddleocr import PaddleOCR
from pdf2image import convert_from_path

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_text = []

    for img in images:
        result = ocr.ocr(img, cls=True)
        if result and result[0]:
            for line in result[0]:
                extracted_text.append(line[1][0])

    return "\n".join(extracted_text)

if __name__ == "__main__":
    text = extract_text_from_pdf("../sample_resume.pdf")
    with open("resume_raw.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("✅ OCR extraction completed")
