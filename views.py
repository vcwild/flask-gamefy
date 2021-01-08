from app import app, db
from config import UPLOAD_PATH
from utils.helpers import recover_image, delete_file
from models import Game
from data.dao import UserDao, GameDao
from flask import (
    render_template, 
    request, redirect, 
    session, flash,url_for, 
    send_from_directory
)
from time import time
import werkzeug


game_dao = GameDao(db)
user_dao = UserDao(db)

@app.route('/')
def index():
    games_list = game_dao.list_games()
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
    saved_game = game_dao.save(game)
    if request.files['game_image']:
        game_image = request.files['game_image']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time()
        game_image.save(f'{upload_path}/img_{saved_game.id}_{timestamp}.jpg')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    if 'current_user' not in session or session['current_user'] == None:
        return redirect(url_for('login', next=url_for('edit')))

    game = game_dao.search_by_id(id)
    image_name = recover_image(id)
    try:
        return render_template(
            'edit.html',
            title='Edit Game',
            game=game,
            game_image=image_name
        )
    except werkzeug.routing.BuildError:
        return render_template(
            'edit.html',
            title='Edit Game',
            game=game
        )

@app.route('/update', methods=['POST'])
def update():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console, id=request.form['id'])
    saved_game = game_dao.save(game)
    if request.files['game_image']:
        game_image = request.files['game_image']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time()
        delete_file(saved_game.id)
        game_image.save(f'{upload_path}/img_{saved_game.id}_{timestamp}.jpg')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    game_dao.delete_game(id)

    flash('The game was deleted successfully!')
    return redirect(url_for('index'))
    
@app.route('/login')
def login():
    next = request.args.get(key='next')
    return render_template('login.html', title="Login", next=next)

@app.route('/auth', methods=['POST'])
def auth():
    user = user_dao.search_by_id(request.form['user'])
    if user:
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

@app.route('/uploads/<game_image>')
def image(game_image):
    return send_from_directory('uploads', game_image)
