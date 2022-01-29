import uuid
from flask import Flask, render_template, redirect, url_for, request


class Game:

    def __init__(self, game_id, name):
        self.game_id = game_id
        self.name = name
        self.is_wanted = True


app = Flask(__name__)
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
    if game_id in games:
        if games[game_id].is_wanted:
            return render_template("game.html", game_id=str(game_id), name=games[game_id].name)
        else:
            return render_template("error.html", message="この部屋は現在、プレイヤーを募集していません。")
    else:
        return render_template("error.html", message="存在しない部屋です。")


if __name__ == "__main__":
    app.run()
