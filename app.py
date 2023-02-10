from flask import Flask, send_from_directory, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from room import Room
import secrets
import string
import random


app = Flask(__name__)
app.secret_key = secrets.token_bytes()
socketio = SocketIO(app, logger=True, engineio_logger=True)
rooms = {}


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def catch_all(path):
    return send_from_directory("dist", path)


@socketio.on("c0-make-room")
def make_room(data):
    room_name = data["room_name"]
    owner_name = data["owner_name"]

    while True:
        room_id = "".join(random.sample(string.ascii_letters + string.digits, k=8))
        if room_id not in rooms:
            break

    try:
        rooms[room_id] = Room(room_name)
    except Exception as error:
        emit("s0-failed-make-room", {"reason": error.message})
        return

    try:
        player_id = rooms[room_id].add_player(owner_name)
    except Exception as error:
        emit("s0-failed-make-room", {"reason": error.message})
        return
    
    session["room_id"] = room_id
    session["player_id"] = player_id
    join_room(room_id)
    emit("s0-enter-room", {"room_id": room_id, "player_id": player_id})


@socketio.on("c0-enter-room")
def enter_room(data):
    room_id = data["room_id"]
    player_name = data["player_name"]

    if room_id not in rooms:
        emit("s0-failed-enter-room", {"reason": "存在しない部屋です"})
        return
    
    try:
        player_id = rooms[room_id].add_player(player_name)
    except Exception as error:
        emit("s0-failed-enter-room", {"reason": error.message})
        return
    
    session["room_id"] = room_id
    session["player_id"] = player_id
    join_room(room_id)
    emit("s0-enter-room", {"room_id": room_id, "player_id": player_id})


@socketio.on("c0-leave")
def leave():
    room_id = session["room_id"]
    player_id = session["player_id"]

    rooms[room_id].leave(player_id)
    leave_room(room_id)

    session.pop("room_id")
    session.pop("player_id")


@socketio.on("disconnect")
def disconnect():
    room_id = session.get("room_id")
    player_id = session.get("player_id")

    if room_id == None:
        return
    
    room = rooms[room_id]
    room.offline(player_id)
    socketio.sleep(60)

    if room.is_offline(player_id):
        room.leave(player_id)


@socketio.on("c0-reconnect")
def reconnect(data):
    room_id = data["room_id"]
    player_id = data["player_id"]

    if rooms[room_id].reconnect(player_id):
        session["room_id"] = room_id
        session["player_id"] = player_id
        join_room(room_id)
        emit("s0-reconnect")
    else:
        emit("s0-failed-reconnect")


if __name__ == "__main__":
    socketio.run(app, debug=True)
