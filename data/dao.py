from models import Game, User

SQL_DELETE_GAME = 'DELETE from game where id = %s'
SQL_GAME_BY_ID = 'SELECT id, name, category, console FROM game WHERE id = %s'
SQL_USER_BY_ID = 'SELECT id, name, password FROM user WHERE id = %s'
SQL_UPDATE_GAME = 'UPDATE game SET name=%s, category=%s, console=%s WHERE id = %s'
SQL_SEARCH_GAME = 'SELECT id, name, category, console FROM game'
SQL_CREATE_GAME = 'INSERT into game (name, category, console) VALUES (%s, %s, %s)'

def unpack_games(games):
    def tuple_n(tuple_n):
        return Game(tuple_n[1], tuple_n[2], tuple_n[3], id=tuple_n[0])
    return list(map(tuple_n, games))

def unpack_user(tuple_n):
    return User(tuple_n[0], tuple_n[1], tuple_n[2])


class GameDao:
    def __init__(self, db):
        self.__db = db

    def save(self, game):
        cursor = self.__db.connection.cursor()

        if game.id:
            cursor.execute(SQL_UPDATE_GAME, (game.name, game.category, game.console, game.id))
        else:
            cursor.execute(SQL_CREATE_GAME, (game.name, game.category, game.console))
            game.id = cursor.lastrowid
        self.__db.connection.commit()
        return game

    def list_games(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SEARCH_GAME)
        games = unpack_games(cursor.fetchall())
        return games

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_GAME_BY_ID, (id,))
        tuple_n = cursor.fetchone()
        return Game(tuple_n[1], tuple_n[2], tuple_n[3], id=tuple_n[0])

    def delete_game(self, id):
        self.__db.connection.cursor().execute(SQL_DELETE_GAME, (id, ))
        self.__db.connection.commit()


class UserDao:
    def __init__(self, db):
        self.__db = db

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USER_BY_ID, (id,))
        data = cursor.fetchone()
        user = unpack_user(data) if data else None
        return user