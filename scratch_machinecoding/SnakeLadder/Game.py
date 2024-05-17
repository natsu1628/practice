from Board import Board
from User import User
import random


class Game:
    def __init__(self, board):
        self.board = board
        self.winner = None
        self.total_moves = 0
        self.turn = 0
        self.players = []

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def register_players(self, name, age, sex, rating):
        try:
            user = User(name, age, sex, rating)
            User.validate_user(user, self.players)
            self.players.append(user)
        except Exception as e:
            print("Player already registered.")

    def determine_player_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def play(self):
        user = None
        k = 1
        if len(self.players) > 1:
            print("#######################################################################")
            print("#############################GAME STARTS###############################")
            print("#######################################################################")
            while self.winner is None and k <= 20:
                k += 1
                print("-----------------------------------------------------------------------")
                self.determine_player_turn()
                user = self.players[self.turn]
                print(f"Player {user.name} turn: ")
                print("Rolling die...")
                num = Game.roll_dice()
                print(f"Die cast {num}")
                user.moves += 1
                self.total_moves += 1
                value = user.cell_value + num
                r, c = value // self.board.board_size, value % self.board.board_size
                if r >= self.board.board_size or c >= self.board.board_size:
                    print("Roll a smaller number")
                    print(f"Cell value: {user.cell_value}")
                    continue
                final_value = self.board.check_snakes_ladders(r, c)
                if final_value > value:
                    print("Ladder encountered")
                elif final_value < value:
                    print("Snake encountered")
                user.cell_value = final_value
                print(f"Cell value: {final_value}")
                print(f"Player {user.name} turn over")
                if final_value == self.board.board_size ** 2 - 1:
                    user.winner = True
                    break
            print("-----------------------------------------------------------------------")
            print("------------------------------GAME OVER--------------------------------")
            if user.winner:
                print(f"Winner: {user.name}")
            else:
                print("Game is a tie")
            print()
            print("#######################################################################")
            print("----------------------------PLAYER STATS-------------------------------")
            for player in self.players:
                print(player)
        else:
            print("Not enough players to play the game")

    def print_players(self):
        for player in self.players:
            print(player)
