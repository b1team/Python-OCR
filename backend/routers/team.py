from flask import Blueprint, render_template


team_bp = Blueprint(
    "team_bp",
    __name__,
)


@team_bp.route("/team")
def show_team():
    return render_template("team.html", title="Thành viên - Chuyển ảnh thành văn bản")
