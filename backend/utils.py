import io

import pytesseract
from PIL import Image
import requests


def detect_file(file, lang):
    scanned_text = pytesseract.image_to_string(
        Image.open(io.BytesIO(file)), lang=lang
    )
    return scanned_text


def download_file_from_url(url, file_name):
    r = requests.get(url, stream=True)
    with open(file_name, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return file_name