from flask import Flask

from backend.setting import Config

app = Flask(__name__)
app.secret_key = Config.secret_key
