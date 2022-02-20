from flask import Flask

from backend.setting import Config

app = Flask(__name__, static_folder="../../frontend/static", template_folder="../../frontend/templates")
app.secret_key = Config.secret_key
