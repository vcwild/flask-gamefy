from lib.classes import Game, User

SQL_DELETE_GAME = 'delete from game where id = %s'
SQL_GAME_BY_ID = 'SELECT id, name, category, console from game where id = %s'
SQL_USER_BY_ID = 'SELECT id, name, password from user where id = %s'
SQL_UPDATE_GAME = 'UPDATE game SET name=%s, category=%s, console=%s where id = %s'
SQL_SEARCH_GAME = 'SELECT id, name, category, console from game'
SQL_CREATE_GAME = 'INSERT into game (name, category, console) values (%s, %s, %s)'


class gameDao:
    def __init__(self, db):
        self.__db = db

    def save(self, game):
        cursor = self.__db.connection.cursor()

        if (game.id):
            cursor.execute(SQL_UPDATE_GAME, (game.name, game.category, game.console, game.id))
        else:
            cursor.execute(SQL_CREATE_GAME, (game.name, game.category, game.console))
            game.id = cursor.lastrowid
        self.__db.connection.commit()
        return game

    def list_games(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SEARCH_GAME)
        games = translate_games(cursor.fetchall())
        return games

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_GAME_BY_ID, (id,))
        tuple_n = cursor.fetchone()
        return Game(tuple_n[1], tuple_n[2], tuple_n[3], id=tuple_n[0])

    def delete_game(self, id):
        self.__db.connection.cursor().execute(SQL_DELETE_GAME, (id, ))
        self.__db.connection.commit()


class userDao:
    def __init__(self, db):
        self.__db = db

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USER_BY_ID, (id,))
        data = cursor.fetchone()
        user = translate_user(data) if data else None
        return user


def translate_games(games):
    def tuple_n(tuple_n):
        return Game(tuple_n[1], tuple_n[2], tuple_n[3], id=tuple_n[0])
    return list(map(tuple_n, games))

def translate_user(tuple_n):
    return User(tuple_n[0], tuple_n[1], tuple_n[2])