"""
3D Maze Generation and Solving Library

This package provides implementations of various maze generation algorithms
and solving algorithms for procedural maze generation and solving.
"""

from maze import Maze
from GenAlgo import genAlgo
from SolveAlgo import solveAlgo
from BackTrackingGenerator import BacktrackingGenerator
from BackTrackingSolver import BacktrackingSolver
from BinaryTree import BinaryTree
from Ellers import Ellers
from Wilsons import Wilsons
from Tremaux import Tremaux
from RandomMouse import RandomMouse
from ShortestPath import ShortestPath

__all__ = [
    'Maze',
    'genAlgo',
    'solveAlgo',
    'BacktrackingGenerator',
    'BacktrackingSolver',
    'BinaryTree',
    'Ellers',
    'Wilsons',
    'Tremaux',
    'RandomMouse',
    'ShortestPath',
]

__version__ = '1.0.0'

