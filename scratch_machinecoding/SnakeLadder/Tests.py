from Board import Board
from Game import Game


board = Board(board_size=5)
game = Game(board)


def test_user():
    game.register_players("Sanjay", 29, "M", 1200)
    game.register_players("Shweta", 29, "F", 1200)
    # game.register_players("Sanjay", 29, "M", 1200)
    # game.print_players()

def test_board():
    board.create_snakes([4, 2], [0, 3])
    board.create_ladders([0, 3], [3, 4])
    game.board.print_board()


if __name__ == "__main__":
    test_user()
    test_board()
    game.play()
