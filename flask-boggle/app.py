from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle
from random import sample

app = Flask(__name__)
boggle_game = Boggle()

app.config['SECRET_KEY'] = "farts"
app.debug = True
debug = DebugToolbarExtension(app)


@app.route('/')
def main_page():
    my_words = boggle_game.words
    rando_words = sample(my_words, 10)
    return render_template('home.html', words=rando_words)

@app.route('/board')
def board():
    board_tiles = [tile for tile in boggle_game.make_board()]
    return render_template('board.html', board=board_tiles)


if __name__ == '__main__':
    app.run(debug=True)