class Member(object):
    def __init__(self, name, member_id, superCoins):
        self.name = name
        self.member_id = member_id
        self.superCoins = superCoins

    def __str__(self):
        return f"Name: {self.name}, id: {self.member_id}, supercoins: {self.superCoins}"
