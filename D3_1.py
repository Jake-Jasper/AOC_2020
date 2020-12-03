'''
I think when we move through the matrix we need to wrap around when we go over the length of the first dimension.
'''


AOC_world = open('D3_1_data.txt', 'r').read().split()

row_c = 0  # this needs to wrap around
col_c = 0

tree_count = 0


while row_c < len(AOC_world) -1:
    col_c += 3
    row_c += 1
    
    if col_c > len(AOC_world[0]) - 1:
        # if we are at a position > than the width of the string, we need to wrap around
        col_c = col_c - len(AOC_world[0])

    if AOC_world[row_c][col_c] == '#':
        tree_count += 1
print(tree_count)
    
