from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/quem-somos", methods=["GET", "POST"])
def quemSomos():
    return render_template("quemsomos.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    return render_template("contato.html")

app.run(debug=True)