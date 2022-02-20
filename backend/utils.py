import io
import time
import os

import pytesseract
from PIL import Image
import qrcode


def detect_file(file, lang):
    scanned_text = pytesseract.image_to_string(
        Image.open(io.BytesIO(file)), lang=lang
    )
    return scanned_text


def create_folder(folder):
    if not os.path.exists(os.path.abspath(folder)):
        os.makedirs(folder)
    return folder


def generate_qr(folder, text):
    qr = qrcode.QRCode(
        version=1,
        box_size=20,
        border=1)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_name = f"{time.time()}.png"
    img.save(f'{folder}/{file_name}')
    return file_name