import os

from flask import Blueprint, session, send_from_directory

from backend.utils import generate_qr, create_folder
from backend.setting import Config

qr_bp = Blueprint(
    "qr_bp",
    __name__,
)


@qr_bp.route("/qr", methods=["GET"])
def qrcode():
    if "data" in session:
        data = session["data"]
        text = data["text"]
        folder_name = create_folder(Config.qrcode_folder)
        qr_image = generate_qr(folder_name, text)
        return send_from_directory(os.path.abspath(folder_name), qr_image)
    