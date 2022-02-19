from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    session,
)
import datetime

from backend.utils import detect_file
from backend.logger import logger

scan_bp = Blueprint(
    "scan_bp",
    __name__,
    template_folder="../../templates",
    static_folder="../../static",
)


@scan_bp.route("/scanner", methods=["POST"])
def scan_file():
    start_time = datetime.datetime.now()
    image_data = request.files["file"].read()
    lang = request.form.get("lang", "vie")
    logger.info("Scanning file with language: %s", lang)
    scanned_text = detect_file(image_data, lang)
    session["data"] = {
        "text": scanned_text,
        "time": str((datetime.datetime.now() - start_time).total_seconds()),
    }

    return redirect(url_for("result_bp.result"))
