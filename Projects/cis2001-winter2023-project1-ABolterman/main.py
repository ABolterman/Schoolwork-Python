from JumpClass import JumpSolver
from BoardGenerator import CheckerBoard

JumpSolver(CheckerBoard().get_board()).get_max_jumps()

bad_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
             ]
bad = JumpSolver(bad_board)
