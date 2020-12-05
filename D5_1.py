
'''
Although it was clear that there is a need for conversion to binary and working with that. I know nothing about Binary and therefore cannot do it
without learning a few things - which will take a lot of time I assume. So for now I shall do it my own way and see how far I get. If I get stuck I shall
look at the binary but I will probably have to look at someone else's solution and I shall disqualify myself for that.
'''

AOC_data = open('D5_data', 'r').read().split('\n')

def find_seat(seat_ID):

    row = list(range(0,128))
    col = list(range(0,8))
    mid_row = len(row) // 2
    mid_col = len(col) // 2
    for i in seat_ID:

        if i == 'F':
            row = row[:mid_row]
            mid_row = len(row) // 2
        elif i == 'B':
            row = row[mid_row:]
            mid_row = len(row) // 2
        elif i == 'R':
            col = col[mid_col:]
            mid_col = len(col) // 2
        elif i == 'L':
            col = col[:mid_col]
            mid_col = len(col) // 2


    return row[0] * 8 + col[0]

highest = 0

for i in AOC_data:
    if find_seat(i) > highest:
        highest = find_seat(i)

print(highest)