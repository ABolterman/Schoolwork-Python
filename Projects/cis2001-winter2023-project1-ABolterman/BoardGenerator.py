import random


class CheckerBoard:

    def __init__(self):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                      ]
        self.white_count = 0
        self.black_count = 0
        for i in range(0, 7, 2):
            for j in range(0, 7, 2):
                piece = random.randint(1, 3)
                if piece == 1:
                    self.white_count += 1
                    if self.white_count < 12:
                        self.board[i][j] = 'W'
                if piece == 2:
                    self.black_count += 1
                    if self.black_count < 12:
                        self.board[i][j] = 'B'
        for i in range(1, 8, 2):
            for j in range(1, 8, 2):
                piece = random.randint(1, 3)
                if piece == 1:
                    self.white_count += 1
                    if self.white_count < 12:
                        self.board[i][j] = 'W'
                if piece == 2:
                    self.black_count += 1
                    if self.black_count < 12:
                        self.board[i][j] = 'B'

    def get_board(self):
        return self.board

    def print_board(self):
        print("\n".join(str(row) for row in self.board))