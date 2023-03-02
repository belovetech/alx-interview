#!/usr/bin/python3
"""
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

- grid is a list of list of integers:
  - 0 represents water
  - 1 represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes”
(water inside that isn’t connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """Find the perimeter of island

    Formular for calculating perimeter
        2 * (length + width)
    """
    row = len(grid)
    col = len(grid[0])
    length = 0
    width = 0

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                while grid[r][c] == 1:
                    length += 1
                    r += 1
                r -= 1

                while grid[r][c] == 1:
                    width += 1
                    c += 1
                return (2 * (length + width))
            else:
                continue
