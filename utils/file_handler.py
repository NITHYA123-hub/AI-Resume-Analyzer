import fitz
from PIL import Image
import pytesseract
from docx import Document


import shutil


tesseract_path = shutil.which("tesseract")


if tesseract_path:

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

def extract_text_from_pdf(pdf_file):
    """
    Extract text from uploaded PDF.
    """

    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def extract_text_from_image(image_file):
    """
    Extract text from uploaded image using OCR.
    """

    image = Image.open(image_file)

    text = pytesseract.image_to_string(image)

    return text


def extract_text_from_txt(txt_file):
    """
    Extract text from TXT file.
    """

    return txt_file.read().decode("utf-8")

def extract_text_from_docx(docx_file):

    text = ""

    document = Document(docx_file)

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text