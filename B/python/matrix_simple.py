# simple matrix manipulation 
# from CareerCup Ch1

import sys 
import os
import commands
import re
from sets import Set

def show(m):
    for row in m:
        print row


# rotate a N*N matrix by 90 degrees in place
def rotate_right_90(m):
    if len(m) != len(m[0]):
        raise ValueError('not N*N')

    show(m)
    n = len(m)
    # rotate layer by layer, from outmost
    for layer in range(n / 2):
        print 'layer ' + str(layer) + '****'
        start = layer
        end = n - 1 - layer
        j = start
        while j < end:
            offset = j - start
            tmp = m[start][j]
            m[start][j] = m[end -offset][start] # left bottom->top
            m[end - offset][start] = m[end][end - offset] # right bottom->left bottom
            m[end][end - offset] = m[j][end] # right top->bottom
            m[j][end] = tmp
            j += 1
        show(m)


    return m

# if an element in an MxN matrix is 0, its entire row and col
# is set to 0
def set_zero(m):
    show(m)
    rows = Set()
    cols = Set()
    # 1st loop flag the row & col index 
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                rows.add(i)
                cols.add(j)
    # 2nd loop set 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (i in rows) or (j in cols):
                m[i][j] = 0
    print
    show(m)

def main():
    matrix = [ [1, 2, 3, 3],
               [4, 5, 6, 3],
               [7, 8, 9, 0],
               [0, 1, 2, 3] ]
    try:
        set_zero(matrix)
        #result = rotate_right_90(matrix)
        #show(result)
    except ValueError, e:
        print 'Illegal argument: ' + str(e)


if __name__ == '__main__':
    main()
