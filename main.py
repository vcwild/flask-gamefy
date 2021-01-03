from lib.games import Game, games_list
from lib.users import User, users_list
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
if environ.get('SECRET_KEY') is None:
    raise KeyError('SECRET_KEY not defined in current environment # export SECRET_KEY=value')
else:
    app.secret_key = environ['SECRET_KEY']


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
    if request.form['user'] in users_list:
        user = users_list[request.form['user']]
        if user.password == request.form['password']:
            session['current_user'] = user.id
            flash('Welcome ' + str.capitalize(user.id) + '!')
            next_page = request.form['next']
            return redirect(next_page)
        else:
            flash(u'Invalid user or password!', category='error')
            return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['current_user'] = None
    flash('User logged out successfully!')
    return redirect(url_for('index'))


app.run(debug=True)