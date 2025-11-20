"""
Maze class for generating and solving mazes.

This module provides the main Maze class that coordinates maze generation
and solving using various algorithms.
"""
from random import randrange
from typing import Optional, Tuple, List
import numpy as np
try:
    from constants import (
        MIN_GRID_SIZE, MIN_ENTRANCE_DISTANCE, MAX_ENTRANCE_ATTEMPTS,
        MAX_END_POINT_ATTEMPTS, CHAR_WALL, CHAR_PASSAGE, CHAR_START,
        CHAR_END, CHAR_SOLUTION
    )
except ImportError:
    # Fallback if constants module is not available
    MIN_GRID_SIZE = 3
    MIN_ENTRANCE_DISTANCE = 2
    MAX_ENTRANCE_ATTEMPTS = 1000
    MAX_END_POINT_ATTEMPTS = 100
    CHAR_WALL = "O"
    CHAR_PASSAGE = " "
    CHAR_START = "S"
    CHAR_END = "E"
    CHAR_SOLUTION = "#"


class Maze:
    """
    Main class for maze generation and solving.
    
    This class coordinates the use of maze generators and solvers to create
    and solve mazes. It provides methods for generating mazes, creating
    entrances/exits, solving mazes, and converting them to string representations.
    
    Attributes:
        generator: The maze generation algorithm to use
        grid: The generated maze grid (numpy array)
        start: Starting position tuple (row, column)
        end: Ending position tuple (row, column)
        solver: The maze solving algorithm to use
        solutions: List of solution paths found by the solver
        clear: Whether to clear redundant paths from solutions
    """
    
    def __init__(self) -> None:
        """Initialize a new Maze instance with default values."""
        # Initialize instance variables
        self.generator = None
        self.grid = None
        self.start = None
        self.end = None
        self.solver = None
        self.solutions = None
        self.clear = True

    def generate(self) -> None:
        """
        Generate the maze grid using the assigned generator.
        
        Raises:
            ValueError: If generator is not set or generation fails
        """
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

    def generate_entrances(self, max_attempts: int = MAX_ENTRANCE_ATTEMPTS) -> None:
        """
        Generate start and end points for the maze.
        
        Attempts to place start and end points with minimum distance between them.
        If unable to find suitable positions after max_attempts, uses the last
        generated positions.
        
        Args:
            max_attempts: Maximum number of attempts to find valid entrances
        """
        attempts = 0
        while attempts < max_attempts:
            self.inner_entrances()
            # If start and end points are far enough apart, we're done
            if abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1]) >= MIN_ENTRANCE_DISTANCE:
                return
            attempts += 1
        # If we couldn't find suitable entrances after max_attempts, use the last generated ones
        # This prevents infinite recursion in edge cases

    def inner_entrances(self) -> None:
        """
        Generate start and end points within the inner grid cells.
        
        Raises:
            ValueError: If grid is not generated or too small
        """
        if self.grid is None:
            raise ValueError("Grid must be generated before creating entrances")
        H, W = self.grid.shape
        # Check if there are valid cells for entrances
        if H < MIN_GRID_SIZE or W < MIN_GRID_SIZE:
            raise ValueError(f"Grid too small for entrances: {H}x{W}, need at least {MIN_GRID_SIZE}x{MIN_GRID_SIZE}")
        # Generate start point (must be on odd row/column indices)
        self.start = (randrange(1, H, 2), randrange(1, W, 2))
        # Generate end point, ensuring it's different from start
        attempts = 0
        end = (randrange(1, H, 2), randrange(1, W, 2))
        while end == self.start and attempts < MAX_END_POINT_ATTEMPTS:
            end = (randrange(1, H, 2), randrange(1, W, 2))
            attempts += 1
        self.end = end

    def generate_and_solve(self, clear: bool = True) -> None:
        """
        Generate maze, create entrances, and solve it in one call.
        
        Args:
            clear: Whether to clear redundant paths from solutions
        """
        self.generate()
        self.generate_entrances()
        self.solve(clear)

    def solve(self, clear: bool = True) -> None:
        """
        Solve the maze using the assigned solver.
        
        Args:
            clear: Whether to remove redundant paths from solutions
            
        Raises:
            ValueError: If solver, grid, or entrances are not set
        """
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
            self.solutions = self.solver.clear_solutions(self.solutions)

    def tostring(self, entrances: bool = False, solutions: bool = False) -> str:
        """
        Convert maze grid to string representation.
        
        Args:
            entrances: Whether to mark start (S) and end (E) positions
            solutions: Whether to mark solution paths (#)
            
        Returns:
            String representation of the maze
        """
        if self.grid is None:
            return ""
        txt = []
        # Convert each row of the grid to string representation
        for row in self.grid:
            txt.append("".join([CHAR_WALL if cell else CHAR_PASSAGE for cell in row]))
        # Mark start and end points if enabled
        if entrances and self.start and self.end:
            r, c = self.start
            txt[r] = txt[r][:c] + CHAR_START + txt[r][c + 1 :]
            r, c = self.end
            txt[r] = txt[r][:c] + CHAR_END + txt[r][c + 1 :]
        # Mark solutions if enabled
        if solutions and self.solutions and len(self.solutions) > 0:
            # Mark all solution paths (typically just the first one)
            for solution_path in self.solutions:
                if solution_path:  # Check if solution path is not empty
                    for r, c in solution_path:
                        if 0 <= r < len(txt) and 0 <= c < len(txt[r]):
                            txt[r] = txt[r][:c] + CHAR_SOLUTION + txt[r][c + 1 :]
            # Add a line indicating the length of the solution
            len_solutions = sum(row.count(CHAR_SOLUTION) for row in txt)
            txt.append(f"Final length of the solution: {len_solutions}")
        # Join rows with newline characters
        return "\n".join(txt)

    def __str__(self) -> str:
        """
        Return string representation with entrances and solutions.
        
        Returns:
            String representation of the maze
        """
        return self.tostring(True, True)

    def __repr__(self) -> str:
        """
        Return string representation with entrances and solutions.
        
        Returns:
            String representation of the maze
        """
        return self.__str__()
