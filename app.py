import os
import uuid
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for, request, session
from flask_socketio import SocketIO, emit, join_room, disconnect


class Room:

    def __init__(self, room_id, name):
        self.room_id = room_id
        self.name = name
        self.status = "募集中"
        self.players = {}


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
    room_id = str(uuid.uuid1())
    room_name = request.args.get("room_name")

    if room_name in ("", None):
        room_name = "名前のない部屋"

    rooms[room_id] = Room(room_id, room_name)
    return redirect(f"/{room_id}")


@app.route("/<uuid:room_id>")
def room(room_id):
    room_id = str(room_id)
    return render_template("room.html", room_id=room_id)


@socketio.on("connect")
def on_connect(auth):
    print("接続")


@socketio.on("disconnect")
def on_disconnect():
    print("切断")


@socketio.on("check_room_id")
def check_room_id(data):
    room_id = data["room_id"]

    if room_id not in rooms:
        emit("kick", {"message": "存在しない部屋です"})
        disconnect()
        return

    room = rooms[room_id]

    if room.status != "募集中":
        emit("kick", {"message": "この部屋は現在募集中ではありません"})
        disconnect()
        return

    room.players[request.sid] = ""
    emit("ask_player_name", {"room_name": room.name})


if __name__ == "__main__":
    socketio.run(app)
