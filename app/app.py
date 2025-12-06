from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/")
def index():
    return jsonify(message="Hello from DevSecOps Project 1!"), 200

if __name__ == "__main__":
    import os

    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "5000"))

    app.run(host=host, port=port)

