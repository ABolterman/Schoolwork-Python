from MazeSolverClass import MazeSolver

maze = [
    ['S', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', 'X', ' ', ' ', 'E']
]

solver = MazeSolver(maze)
solver.solve()

