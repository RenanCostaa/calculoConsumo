from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    print("teste")
    return render_template('index.html')