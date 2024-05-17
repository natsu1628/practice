from Snake import Snake
from Ladder import Ladder


class Board(Snake, Ladder):
    def __init__(self, board_size):
        self.ladders = []
        self.snakes = []
        self.board_size = board_size
        self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
        k = 0
        for i in range(board_size):
            for j in range(board_size):
                self.board[i][j] = {
                    "value": k,
                    "object": None
                }
                k += 1

    def print_board(self):
        print("#########################Snake and Ladder Game Board##########################")
        for i in range(self.board_size - 1, -1, -1):
            for j in range(self.board_size - 1, -1, -1):
                if self.board[i][j]["object"] is not None:
                    print(f'({self.board[i][j]["value"]}, {type(self.board[i][j]["object"]).__name__})', end="\t")
                else:
                    print(self.board[i][j]["value"], end="\t\t")
            print()
        # print("Ladders: ", self.ladders)
        # print("Snakes: ", self.snakes)

    def create_snakes(self, start, end):
        try:
            Snake.validate_snake(start, end, self.board_size)
            if self.board[start[0]][start[1]]["object"] is not None:
                raise Exception("Another object already present")
            snake = Snake(start, end)
            self.board[start[0]][start[1]]["object"] = snake
            self.snakes.append(snake)
        except Exception as e:
            print("Snake is not created")

    def create_ladders(self, start, end):
        try:
            Ladder.validate_ladder(start, end, self.board_size)
            if self.board[start[0]][start[1]]["object"] is not None:
                raise Exception("Another object already present")
            ladder = Ladder(start, end)
            self.board[start[0]][start[1]]["object"] = ladder
            self.ladders.append(ladder)
        except Exception as e:
            print("Ladder is not created")

    def check_snakes_ladders(self, r, c):
        cell = self.board[r][c]
        if cell["object"] is None:
            return cell["value"]
        nr, nc = cell["object"].end
        return self.board[nr][nc]["value"]


# board = Board(board_size=5)
