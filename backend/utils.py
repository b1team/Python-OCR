import io

import pytesseract
from PIL import Image


def detect_file(file, lang):
    scanned_text = pytesseract.image_to_string(
        Image.open(io.BytesIO(file)), lang=lang
    )
    return scanned_text
