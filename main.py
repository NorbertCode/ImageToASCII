from flask import Flask, render_template, request
import generator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        file = request.files.get("image", None)
        if file:
            print(generator.generate(file))
        return ""
    else:
        return render_template("index.html", title="Main Page")

if __name__ == "__main__":
    app.run(debug=True)
