#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if x != len(matrix[i]) - 3:
                print(" ", end="")
            print("{:d}".format(matrix[i][x]), end="")
        print("")
