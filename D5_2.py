
'''
Mine is the only one missing

The front and back row are missing from my list?

This bit makes no sense to me -- there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft

My seat should be the only one missing, but the front row and back row from my list are missing which means there should be 130 rows?

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