from random import randrange
import random
import numpy as np

class Maze:
    def __init__(self):
        # Initialize instance variables
        self.generator = None
        self.grid = None
        self.start = None
        self.end = None
        self.solver = None
        self.solutions = None
        self.clear = True

    def generate(self):
        # Generate the maze grid
        self.grid = self.generator.generate()
        # Reset start and end points
        self.start = None
        self.end = None
        # Reset solutions
        self.solutions = None

    def generate_entrances(self):
        # Generate entrances/exits for the maze
        self.inner_entrances()
        # If start and end points are too close, regenerate entrances
        if abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1]) < 2:
            self.generate_entrances()

    def inner_entrances(self):
        # Generate start and end points within the inner grid
        H, W = self.grid.shape
        self.start = (randrange(1, H, 2), randrange(1, W, 2))
        end = (randrange(1, H, 2), randrange(1, W, 2))
        # Ensure end point is different from start point
        while end == self.start:
            end = (randrange(1, H, 2), randrange(1, W, 2))
        self.end = end

    def generate_and_solve(self,clear = True):
        # Generate maze, generate entrances, and solve the maze
        self.generate()
        self.generate_entrances()
        self.solve(clear)

    def solve(self, clear = True):
        # Solve the maze
        self.solutions = self.solver.solve(self.grid, self.start, self.end)
        # Optionally clear solutions if set to True
        if clear:
            self.solutions = self.solver.clear_solutions(self.solutions)# delete this to show all paths

    def tostring(self, entrances=False, solutions=False):
        # Convert maze grid to string representation
        if self.grid is None:
            return ""
        txt = []
        # Convert each row of the grid to string representation
        for row in self.grid:
            txt.append("".join(["O" if cell else " " for cell in row]))
        # Mark start and end points if enabled
        if entrances and self.start and self.end:
            r, c = self.start
            txt[r] = txt[r][:c] + "S" + txt[r][c + 1 :]
            r, c = self.end
            txt[r] = txt[r][:c] + "E" + txt[r][c + 1 :]
        # Mark solutions if enabled
        if solutions and self.solutions:
            for r, c in self.solutions[0]:
                txt[r] = txt[r][:c] + "#" + txt[r][c + 1 :]
            # Add a line indicating the length of the solution
            len_solutions = sum(row.count('#') for row in txt)
            txt.append(f"Final length of the solution: {len_solutions}")
        # Join rows with newline characters
        return "\n".join(txt)

    def __str__(self):
        # Return string representation of the maze with entrances and solutions
        return self.tostring(True, True)

    def __repr__(self):
        # Return string representation of the maze with entrances and solutions
        return self.__str__()
