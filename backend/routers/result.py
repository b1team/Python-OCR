from flask import Blueprint, render_template, session

result_bp = Blueprint(
    "result_bp",
    __name__,
    template_folder="../../templates",
    static_folder="../../static",
)


@result_bp.route("/result")
def result():
    if "data" in session:
        data = session["data"]
        return render_template(
            "result.html",
            title="Result",
            time=data["time"],
            text=data["text"],
            words=len(data["text"].split(" ")),
        )
    else:
        return "Wrong request method."
