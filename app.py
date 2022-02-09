import os
import uuid
from datetime import timedelta
from flask import Flask, render_template, redirect, request, session
from flask_socketio import SocketIO, emit, join_room


class Room:

    def __init__(self, name):
        self.name = name


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=1)
socketio = SocketIO(app)
rooms = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/make_room")
def make_room():
    room_id = uuid.uuid1()
    name = request.args.get("name")

    if name in ("", None):
        name = "名前のない部屋"

    rooms[room_id] = Room(name)
    return redirect(f"/{room_id}")


@app.route("/<uuid:room_id>")
def room(room_id):
    return render_template("room.html", room_id=room_id)


if __name__ == "__main__":
    socketio.run(app, debug=True)
