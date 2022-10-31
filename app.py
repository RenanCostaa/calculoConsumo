from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():

    return render_template('index.html')


if app == __name__:
    app.run(debug=True)
