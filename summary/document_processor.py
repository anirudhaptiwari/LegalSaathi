import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io
import os
import docx
import tiktoken
import tempfile

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def truncate_text(text: str, max_tokens: int = 8000) -> str:
    encoding = tiktoken.get_encoding("cl100k_base")
    encoded = encoding.encode(text)
    truncated = encoded[:max_tokens]
    return encoding.decode(truncated)

def extract_text_from_pdf(file_path):
    text = ''
    try:
        pdf_document = fitz.open(file_path)
    except Exception as e:
        raise ValueError(f"Error opening PDF file: {e}")
    
    for page_num in range(len(pdf_document)):
        try:
            page = pdf_document[page_num]
            text += page.get_text()
            
            for img in page.get_images(full=True):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))
                text += '\n' + extract_text_from_image(image)
            
            if num_tokens_from_string(text) >= 7500:
                break
        except Exception as e:
            print(f"Error processing page {page_num}: {e}")
            continue
    
    pdf_document.close()
    return truncate_text(text)

def extract_text_from_docx(file_path):
    text = ''
    try:
        doc = docx.Document(file_path)
    except Exception as e:
        raise ValueError(f"Error opening DOCX file: {e}")
    
    for para in doc.paragraphs:
        text += para.text + '\n'
        if num_tokens_from_string(text) >= 7500:
            break
    
    for rel in doc.part.rels.values():
        if num_tokens_from_string(text) >= 7500:
            break
        try:
            if "image" in rel.target_ref:
                image_part = rel.target_part
                image = Image.open(io.BytesIO(image_part.blob))
                text += '\n' + extract_text_from_image(image)
        except Exception as e:
            print(f"Error processing image in DOCX: {e}")
            continue
    
    return truncate_text(text)

def extract_text_from_image(image):
    try:
        # Convert image to text using Tesseract
        text = pytesseract.image_to_string(image, lang='mar')  # 'mar' is for Marathi language
        if not text.strip():
            print("Warning: No text extracted from image")
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""

def process_document(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        return extract_text_from_docx(file_path)
    elif file_extension in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp']:
        with Image.open(file_path) as image:
            return extract_text_from_image(image)
    else:
        raise ValueError("Unsupported file format")