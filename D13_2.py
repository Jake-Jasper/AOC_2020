'''
I had no Idea how to do this one
'''

# expected 3417
example_input = '''\
17,x,13,19
'''

def parse(raw_data):
    time , buses = raw_data.splitlines()
    buses = buses.split(',')
    buses = [int(i) for i in buses if i.isnumeric()]
    return int(time), buses

puzzle_input = open('D13_data', 'r').read()


time, buses = parse(puzzle_input)



