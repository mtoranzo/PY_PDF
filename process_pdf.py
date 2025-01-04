import fitz  # PyMuPDF

def extract_text_and_images(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    images = []
    for page in doc:
        text += page.get_text()
        for img in page.get_images():
            images.append(img)
    return text, images

if __name__ == "__main__":
    pdf_path = "manual.pdf"
    text, images = extract_text_and_images(pdf_path)
    print(text)
    for img in images:
        print(img)