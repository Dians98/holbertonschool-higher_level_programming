#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [row[:] for row in matrix]
    for item in range(len(new)):
        for i in range(len(new[item])):
            new[item][i] = new[item][i] ** 2
    return new
