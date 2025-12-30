class JumpSolver:
    WHITE = 'W'
    BLACK = 'B'
    OPEN = ' '

    def __init__(self, board):
        same_diff = 9
        for row_index in range(len(board)):
            for column_index in range(len(board[row_index])):
                if board[row_index][column_index] == JumpSolver.WHITE or \
                        board[row_index][column_index] == JumpSolver.BLACK:
                    if same_diff == 9:
                        if row_index % 2 == column_index % 2:
                            same_diff = 0  # Modulo's the same, thus both row&col are the same (even or odd)
                        else:
                            same_diff = 1  # Mod's different, so either row or col is even or odd, not both
                    if same_diff == 0:
                        if row_index % 2 != column_index % 2:
                            raise Exception("Board is not valid")
                    if same_diff == 1:
                        if row_index % 2 == column_index % 2:
                            raise Exception("Board is not valid")
        self.board = board
        self.number_of_jumps = 0
        self.possible_jumps = {}
        self.taken_jumps = []

    def get_max_jumps(self):
        for row_index in range(len(self.board)):
            for column_index in range(len(self.board[row_index])):
                if self.board[row_index][column_index] == JumpSolver.WHITE:
                    self.number_of_jumps = 0
                    self.board[row_index][column_index] = '0'
                    self._find_jumps(row_index, column_index)
        if self.possible_jumps == {}:
            raise Exception("No jumps available")
        max_jumps = max(self.possible_jumps.keys())
        max_jumps_path = self.possible_jumps[max_jumps]
        print(f"The maximum number of jumps is {max_jumps} with the following path(s):")
        print(max_jumps_path)

    def _find_jumps(self, row_index, col_index):
        # Up-right
        if self._can_jump(row_index - 1, row_index - 2, col_index + 1, col_index + 2):
            self.board[row_index - 1][col_index + 1] = ' '
            self.number_of_jumps += 1
            self.board[row_index - 2][col_index + 2] = self.label_jump(row_index - 2, col_index + 2)
            self.taken_jumps.append("UR")
            self._find_jumps(row_index - 2, col_index + 2)
        # Up-Left
        if self._can_jump(row_index - 1, row_index - 2, col_index - 1, col_index - 2):
            self.board[row_index - 1][col_index - 1] = ' '
            self.number_of_jumps += 1
            self.board[row_index - 2][col_index - 2] = self.label_jump(row_index - 2, col_index - 2)
            self.taken_jumps.append("UL")
            self._find_jumps(row_index - 2, col_index - 2)
        # Down-Left
        if self._can_jump(row_index + 1, row_index + 2, col_index - 1, col_index - 2):
            self.board[row_index + 1][col_index - 1] = ' '
            self.number_of_jumps += 1
            self.board[row_index + 2][col_index - 2] = self.label_jump(row_index + 2, col_index - 2)
            self.taken_jumps.append("DL")
            self._find_jumps(row_index + 2, col_index - 2)
        # Down-Right
        if self._can_jump(row_index + 1, row_index + 2, col_index + 1, col_index + 2):
            self.board[row_index + 1][col_index + 1] = ' '
            self.number_of_jumps += 1
            self.board[row_index + 2][col_index + 2] = self.label_jump(row_index + 2, col_index + 2)
            self.taken_jumps.append("DR")
            self._find_jumps(row_index + 2, col_index + 2)

        if self.number_of_jumps != 0:
            if self.number_of_jumps not in self.possible_jumps.keys():
                self.possible_jumps[self.number_of_jumps] = "\n".join(str(row) for row in self.board)
            else:
                other_path = "\n---OR---\n"
                other_path += "\n".join(str(row) for row in self.board)
                self.possible_jumps[self.number_of_jumps] += other_path

        self.remove_number(row_index, col_index)
        self.number_of_jumps -= 1
        self.replace_black(row_index, col_index)

    def _can_jump(self, row_index1, row_index2, col_index1, col_index2):
        if 0 <= row_index2 <= 7 and 0 <= col_index2 <= 7:
            if self.board[row_index1][col_index1] == JumpSolver.BLACK and \
                    (self.board[row_index2][col_index2] != JumpSolver.BLACK and
                     self.board[row_index2][col_index2] != JumpSolver.WHITE):
                return True
            else:
                return False
        else:
            return False

    def label_jump(self, row_index, col_index):
        label = ''
        if self.board[row_index][col_index] != JumpSolver.OPEN:
            label += str(self.board[row_index][col_index])
            label += ','
        label += str(self.number_of_jumps)
        return label

    def remove_number(self, row_index, col_index):
        if self.board[row_index][col_index] == '0':
            self.board[row_index][col_index] = JumpSolver.WHITE
        if self.board[row_index][col_index] != '0' and self.board[row_index][col_index] != JumpSolver.WHITE:
            if ',' in self.board[row_index][col_index]:
                self.board[row_index][col_index] = \
                    self.board[row_index][col_index][0: len(self.board[row_index][col_index]) - 2]
            else:
                self.board[row_index][col_index] = JumpSolver.OPEN

    def replace_black(self, row_index, col_index):
        if len(self.taken_jumps) != 0:
            if self.taken_jumps[-1] == "UR":
                self.board[row_index + 1][col_index - 1] = JumpSolver.BLACK
            if self.taken_jumps[-1] == "UL":
                self.board[row_index + 1][col_index + 1] = JumpSolver.BLACK
            if self.taken_jumps[-1] == "DL":
                self.board[row_index - 1][col_index + 1] = JumpSolver.BLACK
            if self.taken_jumps[-1] == "DR":
                self.board[row_index - 1][col_index - 1] = JumpSolver.BLACK
            self.taken_jumps.pop()
