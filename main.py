from lib.games import Game, games_list
from os import environ
from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    session, 
    flash,
    url_for
)


app = Flask(__name__)
app.secret_key = environ['SECRET_KEY'] # % export SECRET_KEY=secret_key

@app.route('/')
def index():
    return render_template('list.html', title='Games', games=games_list)

@app.route('/new')
def new():
    if 'current_user' not in session or session['current_user'] == None:
        return redirect(url_for('login', next=url_for('new')))
    return render_template('new.html', title='New Game')

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    games_list.append(game)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    next = request.args.get(key='next')
    return render_template('login.html', title="Login", next=next)

@app.route('/auth', methods=['POST'])
def auth():
    if environ['SECRET_KEY'] == request.form['password']:
        session['current_user'] = request.form['user']
        flash('Welcome ' + str.capitalize(request.form['user']) + '!')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash(u'Invalid password provided!', category='error')
        return redirect(url_for('login'), title="Login")

@app.route('/logout')
def logout():
    session['current_user'] = None
    flash('User logged out successfully!')
    return redirect(url_for('index'))

app.run(debug=True)