'''
Day 12: Rain risk

format - instruction:units
- Ship starts facing east
- Looking throught the input file all the L/R are in increments of 90 which is useful
'''

test_input = '''\
F10
N3
F7
R90
F11
'''
# expected 25

puzzle_input = open('D12_data', 'r').read()

def parse(s):
    data = []
    for line in s.splitlines():
        data.append((line[0], int(line[1:])))
    return data

data = parse(puzzle_input)

# Will use this for the left and right rotation
DIRECTIONS = [
    (0,1), # north +1 y
    (1,0), # east
    (0,-1), # south
    (-1,0) # west
]


def compute(navigation):
    x = y = 0
    ship_dir = DIRECTIONS[1] # east

    for direction, dist in navigation:
        if direction == 'N':
            y += dist
        elif direction == 'E':
            x += dist
        elif direction == 'S':
            y -= dist
        elif direction == 'W':
            x -= dist
        elif direction == 'L':
            turns = dist // 90
            ship_dir = DIRECTIONS[(DIRECTIONS.index(ship_dir) - turns) % 4]
        elif direction == 'R':
            turns = dist // 90
            ship_dir = DIRECTIONS[(DIRECTIONS.index(ship_dir) + turns) % 4]
        elif direction == 'F':
            x += dist * ship_dir[0]
            y += dist * ship_dir[1]

    return abs(x) + abs(y)

print(compute(data))

