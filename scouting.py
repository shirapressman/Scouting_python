#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__, debug=True)


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        team = None
        game = None
        color = None
        number = None

        try:
            team = int(request.form["team"])
        except ValueError:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["team"])

        try:
            game = int(request.form["game"])
        except ValueError:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["game"])


        color = request.form["color"]

        number = int(request.form["number"])

        if team is not None and game is not None and color is not None and number is not None:
            return '''
                <html>
                    <body>
                        <p>Team number {team},</p>
                        <p>Playing in station {color} {number}, </p>
                        <p>Game number {game}</p>
                        <p><a href="/">Click here for new game</a>
                    </body>
                </html>
            '''.format(team=team, game=game, color=color, number=number)
    return '''
        <html>
            <body>
                {errors}
                <p>Enter your details:</p>
                <form method="post" action=".">
                    <p>Team number:</p>
                    <p><input name="team" /></p>
                    <p>Game number:</p>
                    <p><input name="game" /></p>
                    <p>Station color:</p>
                    <input type="radio" name="color" value="red" checked> Red<br>
                    <input type="radio" name="color" value="blue"> Blue<br>
                    <p>Station number:</p>
                    <input type="radio" name="number" value="1" checked> 1<br>
                    <input type="radio" name="number" value="2"> 2<br>
                    <input type="radio" name="number" value="3"> 3<br>
                    <p><input type="submit" value="Start" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

