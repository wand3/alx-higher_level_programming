#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    sq = [[j * j for j in i] for i in matrix]
    return sq
