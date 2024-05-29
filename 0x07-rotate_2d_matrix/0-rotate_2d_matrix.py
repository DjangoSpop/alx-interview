#!/usr/bin/python3
"""module to rotate a marix of x and x."""


def rotate_2d_matrix(matrix):
    """_summary_Args:matrix (_type_): _description_."""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
