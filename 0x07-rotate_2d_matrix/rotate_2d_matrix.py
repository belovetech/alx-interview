#!/usr/bin/python3
""" Given an n x n 2D matrix, rotate it 90 degrees clockwise
    and 90 degrees anti-clockwise.
    Prototype: def right_rotate(matrix):
    Prototype: def left_rotate(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
"""


def right_rotate(matrix):
    """ Rotate 2D matrix by 90 degree clockwise (right rotate)
    """
    N = len(matrix)

    # Transpose of the matrix (main diagonal is unchanged)
    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Swapping the left col with the right col
    for i in range(N):
        low, high = 0, N-1
        while (low < high):
            matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
            low += 1
            high -= 1


def left_rotate(matrix):
    """ Rotate 2D matrix by 90 degree anti_clockwise (left rotate)
    """
    N = len(matrix)

    # Transpose of the matrix (main diagonal is unchanged)
    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Swapping the first row with the last row
    for i in range(N):
        low, high = 0, N-1
        while (low < high):
            matrix[low][i], matrix[high][i] = matrix[high][i], matrix[low][i]
            low += 1
            high -= 1


def print_rotated_matrix(matrix):
    """print rotated 2D amtrix
    """
    row, col = len(matrix), len(matrix[0])

    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end="  ")
        print()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    right_rotate(matrix)
    print_rotated_matrix(matrix)
    print("--------")

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    left_rotate(matrix)
    print_rotated_matrix(matrix)
