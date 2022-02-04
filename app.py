import os
import uuid
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for, request, session
from flask_socketio import SocketIO, emit, join_room


class Game:

    def __init__(self, game_id, name):
        self.game_id = game_id
        self.name = name
        self.num = 0
        self.status = "募集中"


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=1)
socketio = SocketIO(app)
games = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/newgame")
def newgame():
    name = request.args.get("name")
    game_id = uuid.uuid1()

    if name in ["", None]:
        name = "名無し"

    games[game_id] = Game(game_id, name)
    return redirect(f"/{game_id}")


@app.route("/<uuid:game_id>")
def game(game_id):
    if game_id not in games:
        return render_template("error.html", message="存在しない部屋です。")

    if games[game_id].status != "募集中":
        return render_template("error.html", message="この部屋は現在、プレイヤーを募集していません。")

    name = games[game_id].name
    status = games[game_id].status
    num = games[game_id].num
    game_id = str(game_id)
    return render_template("game.html", name=name, status=status, num=num, game_id=game_id)


@socketio.on("connect")
def on_connect(auth):
    print("接続")


@socketio.on("disconnect")
def on_disconnect():
    print("切断")


@socketio.on("join")
def join(data):
    session["game_id"] = data["game_id"]
    join_room(data["game_id"])


@socketio.on("message")
def on_message(data):
    emit("message", {"message": data["message"]}, to=session["game_id"])


if __name__ == "__main__":
    socketio.run(app)
