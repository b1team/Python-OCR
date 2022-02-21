import uuid
from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    session,
    send_from_directory,
    jsonify
)
import datetime

from backend.utils import detect_file
from backend.logger import logger
from backend.setting import Config

scan_bp = Blueprint(
    "scan_bp",
    __name__,
)


@scan_bp.route("/scanner", methods=["POST"])
def scan_file():
    start_time = datetime.datetime.now()
    image_data = request.files["uploadFile"].read()
    session_id = uuid.uuid4().hex
    file_name = f"{Config.image_folder}/scanner_" + str(session_id) + ".png"
    with open(file_name, "wb") as f:
        f.write(image_data)
    lang = request.form.get("lang", "vie")
    logger.info("Scanning file with language: %s", lang)
    scanned_text = detect_file(image_data, lang)
    session['text'] = scanned_text
    session["data"] = {
        "text": scanned_text,
        "session_id": session_id,
        "lang": lang,
        "time": str((datetime.datetime.now() - start_time).total_seconds()),
    }

    return redirect(url_for("result_bp.result"))


@scan_bp.route("/images/<image_id>", methods=["GET"])
def show_image(image_id):
    file_name = "scanner_" + str(image_id) + ".png"
    return send_from_directory(Config.image_folder, file_name)


@scan_bp.route("/update-text", methods=["POST"])
def update():
    if "data" in session:
        body = request.json
        session["text"] = body["text"]
        return jsonify({
            "status": "success",
            "text": body["text"], 
        })
    else:
        return "Bad request", 400