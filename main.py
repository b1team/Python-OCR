import pytesseract

from backend.routers import app

from backend.setting import Config

from backend.routers.home import home_bp
from backend.routers.scan import scan_bp
from backend.routers.result import result_bp

app.register_blueprint(home_bp)
app.register_blueprint(scan_bp)
app.register_blueprint(result_bp)


if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    app.run(debug=Config.debug, host=Config.host, port=Config.port)
