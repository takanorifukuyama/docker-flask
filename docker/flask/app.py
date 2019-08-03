from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def index():
    return "<h1>Hello World! ハローワールド!</h1>"

if __name__ == "__main__":
    app.run()
