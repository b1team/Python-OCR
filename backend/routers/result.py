from flask import Blueprint, render_template, session

result_bp = Blueprint(
    "result_bp",
    __name__,
)


@result_bp.route("/result", methods=["GET"])
def result():
    data = session["data"]
    if "data" in session:
        data = session["data"]
        return render_template(
            "convert.html",
            title="Result",
            session_id=data["session_id"],
            text=data["text"]
        )
    else:
        return "Bad request", 400
