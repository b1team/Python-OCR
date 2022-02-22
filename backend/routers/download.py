import os

from flask import Blueprint, send_file, session
from backend.setting import Config
download_bp = Blueprint(
    "download_bp",
    __name__,
)


@download_bp.route('/download')
def download_file():
    if "text" in session:
        text = session['text']
        session_id = session["data"]["session_id"]
        txt_folder = Config.txt_folder
        file_name = f"{txt_folder}/text_{session_id}.txt"
        text = text.replace('', '')
        with open(file_name, "w") as f:
            f.write(text)
        return send_file(file_name, as_attachment=True)