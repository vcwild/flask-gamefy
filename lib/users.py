from lib.models import User

users = [
    User('daniel', 'Daniel Hielts', 'DANIEL'),
    User('john', 'John Doe', 'JOHN'),
    User('zack', 'Zack Bragda', 'ZACK'),
    User('flavio', 'Flávio Carlo', 'FLAVIO')
]
users_list = {user.id: user for user in users}
