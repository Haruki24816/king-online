from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_bytes()
socketio = SocketIO(app, logger=True, engineio_logger=True)


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def catch_all(path):
    return send_from_directory("dist", path)


@socketio.on("message")
def receive_message(data):
    emit("message", data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)
