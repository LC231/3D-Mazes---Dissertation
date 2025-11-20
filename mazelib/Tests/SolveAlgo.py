"""
Base class for maze solving algorithms.

This module provides the base class that all maze solving algorithms inherit from.
"""
"""
Base class for maze solving algorithms.

This module provides the base class that all maze solving algorithms inherit from.
"""
import numpy as np
from numpy.random import shuffle
from typing import List, Tuple, Optional
try:
    from constants import MAX_CLEAR_ATTEMPTS_MULTIPLIER
except ImportError:
    # Fallback if constants module is not available
    MAX_CLEAR_ATTEMPTS_MULTIPLIER = 1


class solveAlgo:
    """
    Base class for maze solving algorithms.
    
    This class provides common functionality for maze solvers, including
    neighbor finding, path clearing, and utility methods.
    
    Attributes:
        grid: The maze grid to solve
        start: Starting position tuple (row, column)
        end: Ending position tuple (row, column)
    """
    
    def solve(self, grid: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]) -> List[List[Tuple[int, int]]]:
        """
        Solve the maze from start to end.
        
        Args:
            grid: The maze grid (1 = wall, 0 = passage)
            start: Starting position (row, column)
            end: Ending position (row, column)
            
        Returns:
            List of solution paths, where each path is a list of (row, column) tuples
        """
        self.maze_load(grid, start, end)
        return self._solve()

    def maze_load(self, grid: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Load the maze grid and start/end points.
        
        Args:
            grid: The maze grid to solve
            start: Starting position (row, column)
            end: Ending position (row, column)
        """
        self.grid = grid.copy()
        self.start = start
        self.end = end

    def _solve(self) -> List[List[Tuple[int, int]]]:
        """
        Solve the maze (to be implemented in subclasses).
        
        Returns:
            List of solution paths
        """
        return None

    def available_neighbours(self, posi: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Find available neighboring cells for the given position.
        
        Searches for neighbors two cells away that are accessible (no walls
        between current position and neighbor).
        
        Args:
            posi: Current position (row, column)
            
        Returns:
            List of (row, column) tuples representing accessible neighbors
        """
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

    def midway(self, a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
        """
        Calculate the cell midway between two cells.
        
        Args:
            a: First cell position (row, column)
            b: Second cell position (row, column)
            
        Returns:
            Midway position (row, column)
        """
        return (a[0] + b[0]) // 2, (a[1] + b[1]) // 2

    def move(self, start: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
        """
        Move from a given start cell in a specified direction.
        
        Args:
            start: Starting position (row, column)
            direction: Direction vector (row_delta, column_delta)
            
        Returns:
            New position after moving
        """
        return tuple(map(sum, zip(start, direction)))

    def one_away(self, cell: Optional[Tuple[int, int]], desire: Optional[Tuple[int, int]]) -> bool:
        """
        Check if a cell is one cell away from another desired cell.
        
        Args:
            cell: First cell position (row, column) or None
            desire: Second cell position (row, column) or None
            
        Returns:
            True if cells are adjacent (one cell apart), False otherwise
        """
        if not cell or not desire:
            return False

        if cell[0] == desire[0]:
            if abs(cell[1] - desire[1]) < 2:
                return True
        elif cell[1] == desire[1]:
            if abs(cell[0] - desire[0]) < 2:
                return True
        return False

    def clear_solution(self, solution: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Remove redundant loops from a solution path.
        
        Removes cycles where the path visits the same cell multiple times,
        keeping only the direct path.
        
        Args:
            solution: List of (row, column) tuples representing the path
            
        Returns:
            Cleaned solution path without redundant loops
        """
        if not solution or len(solution) <= 1:
            return solution
        
        found = True
        attempt = 0
        max_attempt = len(solution) * MAX_CLEAR_ATTEMPTS_MULTIPLIER
        solution = list(solution)  # Make a copy to avoid modifying the original

        while found and len(solution) > 2 and attempt < max_attempt:
            found = False
            attempt += 1

            for i in range(len(solution) - 1):
                first = solution[i]
                # Check if this cell appears later in the solution
                for j in range(i + 1, len(solution)):
                    if solution[j] == first:
                        first_i = i
                        last_i = j
                        found = True
                        break
                if found:
                    break

            if found:
                solution = solution[:first_i] + solution[last_i:]

        if len(solution) > 1:
            if solution[0] == self.start:
                solution = solution[1:]
            if len(solution) > 0 and solution[-1] == self.end:
                solution = solution[:-1]

        return solution

    def clear_solutions(self, solutions: List[List[Tuple[int, int]]]) -> List[List[Tuple[int, int]]]:
        """
        Clear redundant parts from multiple solution paths.
        
        Args:
            solutions: List of solution paths to clean
            
        Returns:
            List of cleaned solution paths
        """
        return [self.clear_solution(s) for s in solutions]
