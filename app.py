from flask import Flask, send_from_directory, session, request
from flask_socketio import SocketIO, emit, join_room
from room import Room
from errors import EventError0
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


@socketio.on_error()
def error_handler(error):
    if isinstance(error, EventError0):
        emit(str(error))
    else:
        emit("s0-error-unknown")
        import traceback
        traceback.print_exc()


@socketio.on("c0-make-room")
def make_room(data):
    room_name = data["room_name"]
    owner_name = data["owner_name"]

    while True:
        room_id = "".join(random.sample(
            string.ascii_letters + string.digits, k=8))
        if room_id not in rooms:
            break

    rooms[room_id] = Room(room_name)
    room = rooms[room_id]
    player_id = room.add_player(owner_name, request.sid)

    session["room_id"] = room_id
    session["player_id"] = player_id

    join_room(room_id)
    emit("s0-enter-room", {"room_id": room_id, "player_id": player_id})
    emit("s0-dist-room-info", {"room_info": room.info()})
    emit("s0-dist-players-data", {"players": room.players})


@socketio.on("c0-enter-room")
def enter_room(data):
    room_id = data["room_id"]
    player_name = data["player_name"]

    if room_id not in rooms:
        raise EventError0("s0-error-no-room-id")

    room = rooms[room_id]
    player_id = room.add_player(player_name, request.sid)

    session["room_id"] = room_id
    session["player_id"] = player_id

    join_room(room_id)
    emit("s0-enter-room", {"room_id": room_id, "player_id": player_id})
    emit("s0-dist-room-info", {"room_info": room.info()}, to=room_id)
    emit("s0-dist-players-data", {"players": room.players}, to=room_id)
    emit("s1-join", {"player_id": player_id}, to=room_id)


@socketio.on("c0-leave")
def leave():
    room_id = session["room_id"]
    player_id = session["player_id"]

    room = rooms[room_id]
    room.leave(player_id)

    emit("s0-dist-room-info", {"room_info": room.info()}, to=room_id)
    emit("s0-dist-players-data", {"players": room.players}, to=room_id)
    emit("s1-leave", {"player_id": player_id}, to=room_id)

    if room.owner_exists() == False:
        emit("s0-finish", to=room_id)
        rooms.pop(room_id)


@socketio.on("disconnect")
def disconnect():
    room_id = session.get("room_id")
    player_id = session.get("player_id")

    if room_id not in rooms:
        return

    room = rooms[room_id]
    player_status = room.player_status(player_id)

    if player_status != "online":
        return

    room.offline(player_id)
    emit("s0-dist-players-data", {"players": room.players}, to=room_id)
    socketio.sleep(60)

    if player_status == "offline":
        room.leave(player_id)
        emit("s0-dist-room-info", {"room_info": room.info()}, to=room_id)
        emit("s0-dist-players-data", {"players": room.players}, to=room_id)
        emit("s1-leave", {"player_id": player_id}, to=room_id)

    if room.owner_exists() == False:
        emit("s0-no-owner", to=room_id)
        rooms.pop(room_id)


@socketio.on("c0-reconnect")
def reconnect(data):
    room_id = data["room_id"]
    player_id = data["player_id"]

    if room_id not in rooms:
        emit("s0-failed-reconnect")

    room = rooms[room_id]

    if room.reconnect(player_id, request.sid):
        session["room_id"] = room_id
        session["player_id"] = player_id
        join_room(room_id)
        emit("s0-reconnect")
        emit("s0-dist-room-info", {"room_info": room.info()}, to=room_id)
        emit("s0-dist-players-data", {"players": room.players}, to=room_id)
    else:
        emit("s0-failed-reconnect")


@socketio.on("c0-kick")
def kick(data):
    player_id = data["player_id"]
    reason = data["reason"]
    room_id = session["room_id"]

    room = rooms[room_id]
    sid = room.get_sid(player_id)
    room.leave(player_id)

    if sid != None:
        emit("s0-kick", {"reason": reason}, to=sid)

    emit("s0-dist-room-info", {"room_info": room.info()}, to=room_id)
    emit("s0-dist-players-data", {"players": room.players}, to=room_id)
    emit("s1-kick", {"player_id": player_id}, to=room_id)


@socketio.on("c1-message")
def message(data):
    message = data["message"]
    room_id = session["room_id"]
    player_id = session["player_id"]

    emit("s1-message",
         {"player_id": player_id, "message": message},
         to=room_id)


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0")
