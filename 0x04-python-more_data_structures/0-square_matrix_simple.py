#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    columns = len(matrix[0])
    if columns == 0:
        return matrix
    else:
        sq_matrix = [[0 for i in range(rows)] for j in range(columns)]
        for r in range(rows):
            for c in range(columns):
                sq_matrix[r][c] = matrix[r][c] ** 2
        return sq_matrix
