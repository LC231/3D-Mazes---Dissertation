import numpy as np
from numpy.random import shuffle

class solveAlgo:
    def solve(self, grid, start, end):
        # Load the maze and solve it
        self.maze_load(grid, start, end)
        return self._solve()

    def maze_load(self, grid, start, end):
        # Load the maze grid, start, and end points
        self.grid = grid.copy()
        self.start = start
        self.end = end

    def _solve(self):
        # Placeholder method for solving the maze, to be implemented in subclasses
        return None

    def available_neighbours(self, posi):
        # Find available neighbouring cells for the given position
        r, c = posi
        ns = []

        if r > 1 and not self.grid[r - 1, c] and not self.grid[r - 2, c]:
            ns.append((r - 2, c))
        if (
            r < self.grid.shape[0] - 2
            and not self.grid[r + 1, c]
            and not self.grid[r + 2, c]
        ):
            ns.append((r + 2, c))
        if c > 1 and not self.grid[r, c - 1] and not self.grid[r, c - 2]:
            ns.append((r, c - 2))
        if (
            c < self.grid.shape[1] - 2
            and not self.grid[r, c + 1]
            and not self.grid[r, c + 2]
        ):
            ns.append((r, c + 2))
        shuffle(ns)
        return ns

    def midway(self, a, b):
        # Calculate the cell midway between two cells
        return (a[0] + b[0]) // 2, (a[1] + b[1]) // 2

    def move(self, start, direction):
        # Move from a given start cell in a specified direction
        return tuple(map(sum, zip(start, direction)))

    def one_away(self, cell, desire):
        # Check if a cell is one cell away from another desired cell
        if not cell or not desire:
            return False

        if cell[0] == desire[0]:
            if abs(cell[1] - desire[1]) < 2:
                return True
        elif cell[1] == desire[1]:
            if abs(cell[0] - desire[0]) < 2:
                return True
        return False

    def clear_solution(self, solution):
        # Clear redundant parts of a solution path
        found = True
        attempt = 0
        max_attempt = len(solution)

        while found and len(solution) > 2 and attempt < max_attempt:
            found = False
            attempt += 1

            for i in range(len(solution) - 1):
                first = solution[i]
                if first in solution[i + 1 :]:
                    first_i = i
                    last_i = solution[i + 1 :].index(first) + i + 1
                    found = True
                    break

            if found:
                solution = solution[:first_i] + solution[last_i:]

        if len(solution) > 1:
            if solution[0] == self.start:
                solution = solution[1:]
            if solution[-1] == self.end:
                solution = solution[:-1]

        return solution

    def clear_solutions(self, solutions):
        # Clear redundant parts of multiple solution paths
        return [self.clear_solution(s) for s in solutions]
