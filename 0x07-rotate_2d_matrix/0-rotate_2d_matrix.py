#!/usr/bin/python3
""" Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """ Rotate 2D matrix by 90 degree clockwise (right rotate)
    """
    N = len(matrix)

    # Transpose of the matrix (main diagonal is unchanged)
    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Swapping the leftmost and rightmost
    for i in range(N):
        for j in range(N//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N-j-1]
            matrix[i][N-j-1] = temp
