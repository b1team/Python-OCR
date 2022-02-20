from flask import Blueprint, render_template


signin_bp = Blueprint(
    "signin_bp",
    __name__,
)


@signin_bp.route("/signin")
def signin():
    return render_template("signin.html", title="Đăng nhập - Chuyển ảnh thành văn bản")
