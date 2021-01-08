from os import environ, path

# check for env vars
if environ.get('SECRET_KEY') is None:
    raise KeyError('SECRET_KEY is not defined in environment # export SECRET_KEY=[value]')
if environ.get('MYSQL_PASSWORD') is None:
    raise KeyError('MYSQL_PASSWORD is not defined in environment # export MYSQL_PASSWORD=[value]')

SECRET_KEY = environ['SECRET_KEY']
UPLOAD_PATH = path.dirname(path.abspath(__file__))+'/uploads'
MYSQL_HOST = "0.0.0.0"
MYSQL_USER = "root"
MYSQL_PASSWORD = environ["MYSQL_PASSWORD"]
MYSQL_DB = "db"
MYSQL_PORT = 3306
