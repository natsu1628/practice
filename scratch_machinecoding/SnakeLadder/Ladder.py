class Ladder(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def validate_ladder(start, end, board_size):
        if start[0] > end[0] or start[0] >= board_size or start[1] >= board_size \
                or (start[0] == board_size - 1 and start[1] == board_size - 1) \
                or (start[0] == 0 and start[1] == 0):
            raise Exception("Ladder validation failed")
        return True

    def __str__(self):
        return f"Ladder details: Start: {self.start}, End: {self.end}"