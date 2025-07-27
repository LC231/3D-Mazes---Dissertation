from random import choice, random
import numpy as np

from GenAlgo import genAlgo

class Ellers(genAlgo):
    def __init__(self, w, h, xskew=0.5, yskew=0.5):
        super(Ellers, self).__init__(w, h)
        # Initialize x and y skew factors
        self.xskew = 0.0 if xskew < 0.0 else 1.0 if xskew > 1.0 else xskew
        self.yskew = 0.0 if yskew < 0.0 else 1.0 if yskew > 1.0 else yskew

    def generate(self):
        # Initialize sets array with dimensions HxW filled with -1
        sets = np.empty((self.H, self.W), dtype=np.int8)
        sets.fill(-1)

        # Initialize max_set_number to track the maximum set number
        max_set_number = 0

        # Loop through every second row starting from the second row
        for r in range(1, self.H - 1, 2):
            # Initialize the current row with set numbers
            max_set_number = self.init_row(sets, r, max_set_number)
            # Merge cells in the current row horizontally
            self.merge_one_row(sets, r)
            # Merge cells in the next row downward
            self.merge_down_a_row(sets, r)

        # Initialize the last row with set numbers
        max_set_number = self.init_row(sets, self.H - 2, max_set_number)
        # Process the last row to merge remaining sets
        self.process_last_row(sets)

        # Convert sets array to grid
        return self.grid_from_sets(sets)

    def init_row(self, sets, row, max_set_number):
        # Initialize sets in the given row with set numbers
        for c in range(1, self.W, 2):
            if sets[row][c] < 0:
                sets[row][c] = max_set_number
                max_set_number += 1
        return max_set_number

    def merge_one_row(self, sets, r):
        # Merge cells in the given row horizontally with a given skew factor
        for c in range(1, self.W - 2, 2):
            if random() < self.xskew:
                if sets[r][c] != sets[r][c + 2]:
                    sets[r][c + 1] = sets[r][c]
                    self.merge_sets(sets, sets[r][c + 2], sets[r][c], max_row=r)

    def merge_down_a_row(self, sets, start_row):
        # Merge cells in the row below the given start row with a given skew factor
        if start_row == self.H - 2:  # Not meant for the bottom row
            return
        # Count how many cells of each set exist in a row
        set_counts = {}
        for c in range(1, self.W, 2):
            s = sets[start_row][c]
            if s not in set_counts:
                set_counts[s] = [c]
            else:
                set_counts[s] = set_counts[s] + [c]

        # Merge down randomly, but at least once per set
        for s in set_counts:
            c = choice(set_counts[s])
            sets[start_row + 1][c] = s
            sets[start_row + 2][c] = s

        # Merge cells downward with a given skew factor
        for c in range(1, self.W - 2, 2):
            if random() < self.yskew:
                s = sets[start_row][c]
                if sets[start_row + 1][c] == -1:
                    sets[start_row + 1][c] = s
                    sets[start_row + 2][c] = s

    def merge_sets(self, sets, from_set, to_set, max_row=-1):
        # Merge sets from one to another within the specified row range
        if max_row < 0:
            max_row = self.H - 1

        for r in range(1, max_row + 1):
            for c in range(1, self.W - 1):
                if sets[r][c] == from_set:
                    sets[r][c] = to_set

    def process_last_row(self, sets):
        # Process the last row to merge remaining sets
        r = self.H - 2
        for c in range(1, self.W - 2, 2):
            if sets[r][c] != sets[r][c + 2]:
                sets[r][c + 1] = sets[r][c]
                self.merge_sets(sets, sets[r][c + 2], sets[r][c])

    def grid_from_sets(self, sets):
        # Convert sets array to grid
        grid = np.empty((self.H, self.W), dtype=np.int8)
        grid.fill(0)

        for r in range(self.H):
            for c in range(self.W):
                if sets[r][c] == -1:
                    grid[r][c] = 1

        return grid
