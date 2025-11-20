"""
Base class for maze generation algorithms.

This module provides the base class that all maze generation algorithms inherit from.
"""
"""
Base class for maze generation algorithms.

This module provides the base class that all maze generation algorithms inherit from.
"""
import numpy as np
from numpy.random import shuffle
from typing import List, Tuple
try:
    from constants import WALL_MULTIPLIER, WALL_OFFSET
except ImportError:
    # Fallback if constants module is not available
    WALL_MULTIPLIER = 2
    WALL_OFFSET = 1


class genAlgo:
    """
    Base class for maze generation algorithms.
    
    This class provides common functionality for maze generators, including
    neighbor finding and grid dimension calculations.
    
    Attributes:
        h (int): Height of the maze (number of cells)
        w (int): Width of the maze (number of cells)
        H (int): Height of the grid including walls
        W (int): Width of the grid including walls
    """
    
    def __init__(self, h: int, w: int) -> None:
        """
        Initialize the maze generator with given dimensions.
        
        Args:
            h: Height of the maze (must be positive)
            w: Width of the maze (must be positive)
            
        Raises:
            ValueError: If dimensions are not positive integers
        """
        # Validate maze dimensions
        if h <= 0 or w <= 0:
            raise ValueError(f"Maze dimensions must be positive integers, got h={h}, w={w}")
        # Initialize maze dimensions
        self.h = int(h)
        self.w = int(w)
        # Calculate grid dimensions with walls included
        self.H = (WALL_MULTIPLIER * self.h) + WALL_OFFSET
        self.W = (WALL_MULTIPLIER * self.w) + WALL_OFFSET 

    def generate(self) -> np.ndarray:
        """
        Generate a maze grid.
        
        This is a placeholder method that should be implemented in subclasses.
        
        Returns:
            A 2D numpy array representing the maze grid (1 = wall, 0 = passage)
        """
        return None

    def find_neighbours(self, r: int, c: int, grid: np.ndarray, is_wall: bool = False) -> List[Tuple[int, int]]:
        """
        Find neighboring cells with a given condition (e.g., being a wall).
        
        Searches for neighbors two cells away (skipping walls) that match
        the specified condition.
        
        Args:
            r: Row index of the current cell
            c: Column index of the current cell
            grid: The maze grid to search
            is_wall: If True, find wall neighbors; if False, find passage neighbors
            
        Returns:
            List of (row, column) tuples representing valid neighbors
        """
        ns = []

        # Check if the cell above is a wall and is within the grid boundaries
        if r > 1 and grid[r - 2][c] == is_wall:
            ns.append((r - 2, c))
        # Check if the cell below is a wall and is within the grid boundaries
        if r < self.H - 2 and grid[r + 2][c] == is_wall:
            ns.append((r + 2, c))
        # Check if the cell to the left is a wall and is within the grid boundaries
        if c > 1 and grid[r][c - 2] == is_wall:
            ns.append((r, c - 2))
        # Check if the cell to the right is a wall and is within the grid boundaries
        if c < self.W - 2 and grid[r][c + 2] == is_wall:
            ns.append((r, c + 2))

        # Shuffle the list of neighbouring cells randomly
        shuffle(ns)
        return ns
