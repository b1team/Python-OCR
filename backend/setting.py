from environs import Env

env = Env()
env.read_env()


class Config:
    host = env.str("HOST", "127.0.0.1")
    port = env.int("PORT", 5000)
    debug = env.bool("DEBUG", False)
    secret_key = env.str("SECRET_KEY", "secret_key")
    qrcode_folder = env.str("QRCODE_FOLDER", "qrcode")
    image_folder = env.str("IMAGE_FOLDER", "images")
    txt_folder = env.str("TXT_FOLDER", "text")
