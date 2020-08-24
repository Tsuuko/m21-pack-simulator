from flask import Flask, render_template, request
import simulator

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        result = simulator.run()
        return render_template("index.html", result=result)
    else:
        return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True)
