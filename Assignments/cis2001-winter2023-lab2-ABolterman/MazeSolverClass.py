class MazeSolver:
    START = 'S'
    END = 'E'
    WALL = 'X'
    BREAD_CRUMB = '.'
    OPEN = ' '
    DEAD_END = 'D'

    def __init__(self, maze):
        self.maze = maze
        self.solved = False
        self.solutions = {}

    def __str__(self):
        return "\n".join(str(row) for row in self.maze)

    def _can_go(self, row_index, column_index):
        return not ((row_index < 0 or row_index >= len(self.maze)) or
                    (column_index < 0 or column_index >= len(self.maze[row_index])) or
                    (self.maze[row_index][column_index] == MazeSolver.WALL) or
                    (self.maze[row_index][column_index] == MazeSolver.BREAD_CRUMB) or
                    (self.maze[row_index][column_index] == MazeSolver.DEAD_END))

    def _solve(self, row_index, column_index, steps):
        if self.maze[row_index][column_index] == MazeSolver.END:
            # print("Solution found!")
            # print(self)
            # self.solved = True
            self.solutions[steps] = "\n".join(str(row) for row in self.maze)
#        elif not self.solved:
        else:
            steps += 1
            if self.maze[row_index][column_index] != MazeSolver.START:
                self.maze[row_index][column_index] = MazeSolver.BREAD_CRUMB
            # up
            if self._can_go(row_index - 1, column_index):
                self._solve(row_index - 1, column_index, steps)
            # down
            if self._can_go(row_index + 1, column_index):
                self._solve(row_index + 1, column_index, steps)
            # right
            if self._can_go(row_index, column_index + 1):
                self._solve(row_index, column_index + 1, steps)
            # left
            if self._can_go(row_index, column_index - 1):
                self._solve(row_index, column_index - 1, steps)
            if self.maze[row_index][column_index] != MazeSolver.START:
                self.maze[row_index][column_index] = MazeSolver.DEAD_END

    def solve(self):
        for row_index in range(len(self.maze)):
            for column_index in range(len(self.maze[row_index])):
                if self.maze[row_index][column_index] == MazeSolver.START:
                    steps_count = 0
                    self._solve(row_index, column_index, steps_count)
        if self.solutions == {}:
            raise Exception("The maze is unsolvable")
        min_steps = min(self.solutions.keys())
        shortest_path = self.solutions[min_steps].replace("D", " ")
        print(f"The shortest path with {min_steps} steps is:")
        print(shortest_path)
