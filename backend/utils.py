import io
import os
import time

import numpy
import pytesseract
import qrcode
import requests
from PIL import Image

from .remove_shadow import remove_shadow as rs
from .unproject import un_project


def detect_file(file, lang, unproject=False, remove_shadow=False):
    pil_image = Image.open(io.BytesIO(file))
    open_cv_image = numpy.array(pil_image.convert("RGB"))
    img = open_cv_image[:, :, ::-1].copy()
    if unproject:
        img = un_project(img)
    if remove_shadow:
        img = rs(img)
    scanned_text = pytesseract.image_to_string(img, lang=lang)
    return scanned_text



def download_file_from_url(url, file_name):
    r = requests.get(url, stream=True)
    with open(file_name, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()


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
