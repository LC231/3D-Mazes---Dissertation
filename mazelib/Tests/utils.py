"""
Utility functions for maze operations.

This module provides helper functions used across the maze generation
and solving system.
"""
from typing import Tuple, List
import numpy as np


def manhattan_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    """
    Calculate Manhattan distance between two positions.
    
    Args:
        pos1: First position (row, column)
        pos2: Second position (row, column)
        
    Returns:
        Manhattan distance between the two positions
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def is_valid_position(pos: Tuple[int, int], grid_shape: Tuple[int, int]) -> bool:
    """
    Check if a position is within grid bounds.
    
    Args:
        pos: Position to check (row, column)
        grid_shape: Shape of the grid (height, width)
        
    Returns:
        True if position is valid, False otherwise
    """
    row, col = pos
    height, width = grid_shape
    return 0 <= row < height and 0 <= col < width


def count_solution_length(solutions: List[List[Tuple[int, int]]]) -> int:
    """
    Count total length of all solution paths.
    
    Args:
        solutions: List of solution paths
        
    Returns:
        Total number of cells in all solution paths
    """
    return sum(len(path) for path in solutions if path)


def validate_grid_size(height: int, width: int, min_size: int = 3) -> None:
    """
    Validate that grid dimensions meet minimum requirements.
    
    Args:
        height: Grid height
        width: Grid width
        min_size: Minimum required size
        
    Raises:
        ValueError: If dimensions are too small
    """
    if height < min_size or width < min_size:
        raise ValueError(
            f"Grid too small: {height}x{width}, "
            f"minimum size is {min_size}x{min_size}"
        )

