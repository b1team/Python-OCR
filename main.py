import pytesseract

from backend.routers import app

from backend.setting import Config

from backend.routers.home import home_bp
from backend.routers.scan import scan_bp
from backend.routers.result import result_bp
from backend.routers.qr_image import qr_bp
from backend.routers.download import download_bp
from backend.routers.signin import signin_bp
from backend.routers.signup import signup_bp
from backend.routers.team import team_bp

app.register_blueprint(home_bp)
app.register_blueprint(scan_bp)
app.register_blueprint(result_bp)
app.register_blueprint(qr_bp)
app.register_blueprint(download_bp)
app.register_blueprint(signin_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(team_bp)


if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    app.run(debug=Config.debug, host=Config.host, port=Config.port)
