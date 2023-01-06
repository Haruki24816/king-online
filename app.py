from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_bytes()


if __name__ == "__main__":
    socketio = SocketIO(app, logger=True, engineio_logger=True)
else:
    socketio = SocketIO(app)


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def catch_all(path):
    return send_from_directory("dist", path)


if __name__ == "__main__":
    socketio.run(app, debug=True)
