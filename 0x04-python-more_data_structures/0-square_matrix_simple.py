#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = []
    for i1 in matrix:
        row = []
        for i2 in i1:
            row.append(i2**2)
        newm.append(row)
    return newm
