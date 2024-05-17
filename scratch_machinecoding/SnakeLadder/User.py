class User(object):
    def __init__(self, name, age, sex, rating):
        self.name = name
        self.age = age
        self.sex = sex
        self.rating = rating
        self.moves = 0
        self.winner = False
        self.cell_value = 0

    @staticmethod
    def validate_user(user, players):
        for player in players:
            if player.name == user.name:
                raise Exception("Player already registered")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Sex: {self.sex}, Rating: {self.rating}, Moves: {self.moves}," \
               f"Winner: {self.winner}"
