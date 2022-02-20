from flask import Blueprint, render_template, session

result_bp = Blueprint(
    "result_bp",
    __name__,
)


@result_bp.route("/result", methods=["GET"])
def result():
    # data = session["data"]
    return render_template(
        "convert.html",
        title="Result",
        # time=data["time"],
        # text=data["text"],
        # words=len(data["text"].split(" ")),
    )
    if "data" in session:
        data = session["data"]
        return render_template(
            "convert.html",
            title="Result",
            time=data["time"],
            text=data["text"],
            words=len(data["text"].split(" ")),
        )
    else:
        return "Bad request", 400
