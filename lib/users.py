class User:
    def __init__(self, id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = password



users = [
    User('daniel', 'Daniel Hielts', 'DANIEL'),
    User('john', 'John Doe', 'JOHN'),
    User('zack', 'Zack Bragda', 'ZACK'),
    User('flavio', 'Flávio Carlo', 'FLAVIO')
]
users_list = {user.id: user for user in users}
