"""
Constants used throughout the maze generation and solving system.
"""

# Grid cell types
WALL = 1
PASSAGE = 0
UNVISITED = -1

# Grid structure constants
WALL_MULTIPLIER = 2  # Multiplier for converting maze dimensions to grid dimensions
WALL_OFFSET = 1  # Offset added to grid dimensions to account for walls

# Minimum grid dimensions
MIN_GRID_SIZE = 3  # Minimum grid size for valid maze (HxW)

# Entrance generation constants
MIN_ENTRANCE_DISTANCE = 2  # Minimum Manhattan distance between start and end points
MAX_ENTRANCE_ATTEMPTS = 1000  # Maximum attempts to generate valid entrances
MAX_END_POINT_ATTEMPTS = 100  # Maximum attempts to generate different end point

# Solution clearing constants
MAX_CLEAR_ATTEMPTS_MULTIPLIER = 1  # Multiplier for max clear attempts (relative to solution length)

# Neighbor direction offsets (for 2-cell jumps in grid)
NORTH = (-2, 0)
SOUTH = (2, 0)
EAST = (0, 2)
WEST = (0, -2)

# Direction indices (used in Wilsons algorithm)
DIRECTION_NORTH = 0
DIRECTION_SOUTH = 1
DIRECTION_EAST = 2
DIRECTION_WEST = 3

# Tremaux algorithm constants
MAX_VISIT_COUNT = 2  # Maximum visit count before treating as dead end

# String representation characters
CHAR_WALL = "O"
CHAR_PASSAGE = " "
CHAR_START = "S"
CHAR_END = "E"
CHAR_SOLUTION = "#"

