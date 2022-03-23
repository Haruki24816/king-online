import os
import uuid
from datetime import timedelta
from flask import Flask, render_template, redirect, request, session
from flask_socketio import SocketIO, emit, join_room
from room import Room


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
    name = request.args.get("name")
    rooms[room_id] = Room(name)
    return redirect(f"/{room_id}")


@app.route("/<uuid:room_id>")
def room(room_id):
    return render_template("room.html", room_id=str(room_id))


@socketio.on("join")
def on_join(data):
    if data["room_id"] not in rooms:
        emit("kick", {"message": "エラー：存在しない部屋です"})
        return

    room_id = data["room_id"]
    room = rooms[room_id]

    try:
        room.add_player(request.sid)
    except Exception as error:
        emit("kick", {"message": f"エラー：{str(error)}"})
        return

    join_room(room_id)
    session["room_id"] = room_id
    emit("update", room.info(), to=room_id)


@socketio.on("connect")
def on_connect(auth):
    print("接続")


@socketio.on("disconnect")
def on_disconnect():
    print("切断")

    if session.get("room_id") == None:
        return

    room_id = session["room_id"]
    room = rooms[room_id]

    player_name = room.remove_player(request.sid)
    emit("update", room.info(), to=room_id)
    session.pop("room_id")

    if player_name != "":
        emit("receive_message", {"author": "server", "message": f"{player_name}が退室しました"}, to=room_id)


@socketio.on("register_player_name")
def on_register_player_name(data):
    room_id = session["room_id"]
    room = rooms[room_id]
    player_name = data["name"]

    try:
        room.register_player_name(request.sid, player_name)
    except Exception as error:
        emit("receive_message", {"author": "server", "message": f"エラー：{str(error)}"})
        return

    emit("update", room.info(), to=room_id)
    emit("receive_message", {"author": "server", "message": f"{player_name}が入室しました"}, to=room_id)


@socketio.on("update_player_status")
def on_update_player_status(data):
    room_id = session["room_id"]
    room = rooms[room_id]

    try:
        room.update_player_status(request.sid, data["player_status"])
    except Exception as error:
        emit("receive_message", {"author": "server", "message": f"エラー：{str(error)}"})
        return

    emit("update", room.info(), to=room_id)

    if data["player_status"] == 1:
        emit("receive_message", {"author": request.sid, "message": "準備ができました"}, to=room_id)


@socketio.on("draw")
def on_draw(data):
    room_id = session["room_id"]
    room = rooms[room_id]

    try:
        card = room.draw(request.sid, **data)
    except Exception as error:
        emit("receive_message", {"author": "server", "message": f"エラー：{str(error)}"})

    emit("update", room.info(), to=room_id)

    if card != None:
        emit("receive_message", {"author": request.sid, "message": f"{card}を引きました"}, to=room_id)


@socketio.on("pay")
def on_pay(data):
    room_id = session["room_id"]
    room = rooms[room_id]

    try:
        message = room.pay(request.sid, **data)
    except Exception as error:
        emit("receive_message", {"author": "server", "message": f"エラー：{str(error)}"})

    emit("update", room.info(), to=room_id)
    emit("receive_message", {"author": request.sid, "message": message}, to=room_id)


@socketio.on("give_change")
def on_give_change(data):
    room_id = session["room_id"]
    room = rooms[room_id]

    try:
        message = room.give_change(request.sid, **data)
    except Exception as error:
        emit("receive_message", {"author": "server", "message": f"エラー：{str(error)}"})

    emit("update", room.info(), to=room_id)
    emit("receive_message", {"author": request.sid, "message": message}, to=room_id)


@socketio.on("borrow")
def on_borrow(data):
    room_id = session["room_id"]
    room = rooms[room_id]

    try:
        message = room.borrow(request.sid, **data)
    except Exception as error:
        emit("receive_message", {"author": "server", "message": f"エラー：{str(error)}"})

    emit("update", room.info(), to=room_id)
    emit("receive_message", {"author": request.sid, "message": message}, to=room_id)


@socketio.on("repay")
def on_repay(data):
    room_id = session["room_id"]
    room = rooms[room_id]

    try:
        message = room.repay(request.sid, **data)
    except Exception as error:
        emit("receive_message", {"author": "server", "message": f"エラー：{str(error)}"})

    emit("update", room.info(), to=room_id)
    emit("receive_message", {"author": request.sid, "message": message}, to=room_id)


if __name__ == "__main__":
    socketio.run(app, debug=True)
