import os
from PIL import Image
from pytesseract import image_to_string, pytesseract


def extract_text_via_ocr_service(file_obj):
  pytesseract.tesseract_cmd = os.environ.get("TESSERACT_CMD")
  im = Image.open(file_obj)
  text = image_to_string(im).split("\n")
  non_empty_lines = [line for line in text if line.strip() != ""]
  string_without_empty_lines = ""
  for line in non_empty_lines:
    if line == non_empty_lines[-1]:
      string_without_empty_lines += line
    else:
      string_without_empty_lines += line + "\n"  
  return string_without_empty_lines
