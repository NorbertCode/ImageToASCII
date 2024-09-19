from flask import Flask, redirect, render_template, request
import generator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Main Page")

@app.route("/result", methods=["POST"])
def result():
    file = request.files.get("image", None)
    if file:
        ascii = generator.generate(file)
        return render_template("result.html", title="Result", ascii=ascii)
    else:
        return redirect("/error")

@app.route("/error")
def error():
    return render_template("error.html", title="Error")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
