from random import getrandbits
from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    session, 
    flash
)



class Game:
    def __init__(self, name, category, console) -> None:
        self.name = name
        self.category = category
        self.console = console



games_list = [
    Game('Super Mario', 'Adventure', 'SNES'),
    Game('Pokémon', 'RPG', 'GBA'),
    Game('Tetris', 'Puzzle', 'NES'),
    Game('Mortal Kombat', 'Fight', 'SNES')
]

app = Flask(__name__)
app.secret_key = str(getrandbits(128))

@app.route('/')
def index():
    return render_template('list.html', title='Games', games=games_list)

@app.route('/new')
def new_page():
    return render_template('new.html', title='New Game')

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    games_list.append(game)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth_login():
    if 'pass' == request.form['password']:
        session['current_user'] = request.form['user']
        flash('Welcome ' + str.capitalize(request.form['user']) + '!')
        return redirect('/')
    else:
        flash('User ' + str.capitalize(request.form['user']) + ' not found!')
        return redirect('/login')

app.run(debug=True)