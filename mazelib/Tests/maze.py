from random import randrange
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
        # Validate generator is set
        if self.generator is None:
            raise ValueError("Generator must be set before generating maze")
        # Generate the maze grid
        self.grid = self.generator.generate()
        if self.grid is None:
            raise ValueError("Generator failed to generate a maze")
        # Reset start and end points
        self.start = None
        self.end = None
        # Reset solutions
        self.solutions = None

    def generate_entrances(self, max_attempts=1000):
        # Generate entrances/exits for the maze
        attempts = 0
        while attempts < max_attempts:
            self.inner_entrances()
            # If start and end points are too close, regenerate entrances
            if abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1]) >= 2:
                return
            attempts += 1
        # If we couldn't find suitable entrances after max_attempts, use the last generated ones
        # This prevents infinite recursion in edge cases

    def inner_entrances(self):
        # Generate start and end points within the inner grid
        if self.grid is None:
            raise ValueError("Grid must be generated before creating entrances")
        H, W = self.grid.shape
        # Check if there are valid cells for entrances
        if H < 3 or W < 3:
            raise ValueError(f"Grid too small for entrances: {H}x{W}, need at least 3x3")
        # Generate start point
        self.start = (randrange(1, H, 2), randrange(1, W, 2))
        # Generate end point, ensuring it's different from start
        max_attempts = 100
        attempts = 0
        end = (randrange(1, H, 2), randrange(1, W, 2))
        while end == self.start and attempts < max_attempts:
            end = (randrange(1, H, 2), randrange(1, W, 2))
            attempts += 1
        self.end = end

    def generate_and_solve(self,clear = True):
        # Generate maze, generate entrances, and solve the maze
        self.generate()
        self.generate_entrances()
        self.solve(clear)

    def solve(self, clear = True):
        # Validate solver and grid are set
        if self.solver is None:
            raise ValueError("Solver must be set before solving maze")
        if self.grid is None:
            raise ValueError("Maze must be generated before solving")
        if self.start is None or self.end is None:
            raise ValueError("Start and end points must be set before solving")
        # Solve the maze
        self.solutions = self.solver.solve(self.grid, self.start, self.end)
        # Optionally clear solutions if set to True
        if clear and self.solutions:
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
        if solutions and self.solutions and len(self.solutions) > 0:
            # Mark all solution paths (typically just the first one)
            for solution_path in self.solutions:
                if solution_path:  # Check if solution path is not empty
                    for r, c in solution_path:
                        if 0 <= r < len(txt) and 0 <= c < len(txt[r]):
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
