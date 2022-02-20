import os

from flask import Blueprint, send_file

download_bp = Blueprint(
    "download_bp",
    __name__,
    template_folder="../../templates",
    static_folder="../../static",
)


@download_bp.route('/download/<path:filename>')
def download_file(filename):
    path = os.path.abspath(filename)
    try:
        send_file(path, as_attachment=True)
    except Exception:
        return "File not found"