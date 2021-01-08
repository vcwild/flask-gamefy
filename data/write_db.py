"""This script can be used to populate the database with mock entities
"""
import MySQLdb
from os import environ

conn = MySQLdb.connect(
    user='user',
    passwd=environ["MYSQL_PASSWORD"],
    host='127.0.0.1',
    port=3306
)

print('Connecting...')

conn.cursor().execute("DROP DATABASE `db`;")
print('Removing DATABASE `db`...\n')
conn.commit()

create_tables = '''SET NAMES utf8;
    CREATE DATABASE `db` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `db`;
    CREATE TABLE `game` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) COLLATE utf8_bin NOT NULL,
      `category` varchar(40) COLLATE utf8_bin NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `user` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `password` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(create_tables)
print('Creating DATABASE `db`\n')

cursor = conn.cursor()
cursor.executemany(
    'INSERT INTO db.user (id, name, password) VALUES (%s, %s, %s)',
    [
        ('daniel', 'Daniel Hielts', 'DANIEL'),
        ('john', 'John Doe', 'JOHN'),
        ('zack', 'Zack Bragda', 'ZACK'),
        ('flavio', 'Flávio Carlo', 'FLAVIO')
    ]
)
print('Inserting users into `db`')

cursor.execute('select * from db.user')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

cursor.executemany(
    'INSERT INTO db.game (name, category, console) VALUES (%s, %s, %s)',
    [
        ('God of War 4', 'Action', 'PS4'),
        ('NBA 2k20', 'Sports', 'Xbox One'),
        ('Rayman Legends', 'Indie', 'PS4'),
        ('Super Mario 3', 'Adventure', 'SNES'),
        ('Pokémon Red', 'RPG', 'GBA'),
        ('Super Mario RPG', 'RPG', 'SNES'),
        ('Super Mario Kart', 'Racing', 'SNES'),
        ('Killer Instinct', 'Fight', 'Dreamcast'),
        ('Mortal Kombat', 'Fight', 'SNES'),
        ('Fire Emblem Echoes', 'JRPG', '3DS'),
        ('Tetris', 'Puzzle', 'NES')
    ])
print('\nInserting games into `db`')

cursor.execute('select * from db.game')
print(' -------------  Games:  -------------')
for game in cursor.fetchall():
    print(game[1])

conn.commit()
cursor.close()
