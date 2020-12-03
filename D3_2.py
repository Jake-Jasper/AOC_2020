'''
I think when we move through the matrix we need to wrap around when we go over the length of the first dimension.
'''

import math

AOC_world = open('D3_1_data.txt', 'r').read().split()



right = [1,3,5,7,1]
down  = [1,1,1,1,2]

slopes = []


def toboggan(right, down):
    row_c = 0
    col_c = 0
    tree_count = 0
    while row_c < len(AOC_world) -1:
        col_c += right
        row_c += down

        if col_c > len(AOC_world[0]) - 1:
            # if we are at a position > than the width of the string, we need to wrap around
            col_c = col_c - len(AOC_world[0])

        if AOC_world[row_c][col_c] == '#':
            tree_count += 1
    return tree_count

for i in range(len(right)):
    slopes.append(toboggan(right[i],down[i]))

# Only works in python3.8+
print(math.prod(slopes))


