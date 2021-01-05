'''
Not exactly sure what the question as asking here I have to admit, so I had to look up what to do.
- The first number is the time, and each of the integers in the second string is the intervals the number of minutes between stops after 0 for example, 7 would stop at 0,7,14,etc

- when we are past the number, we take the difference and multiply it by the id of the bust for the one closest after the number
'''

# expected 295
example_input = '''\
939
7,13,x,x,59,x,31,19
'''

def parse(raw_data):
    time , buses = raw_data.splitlines()
    buses = buses.split(',')
    buses = [int(i) for i in buses if i.isnumeric()]
    return int(time), buses

puzzle_input = open('D13_data', 'r').read()


time, buses = parse(puzzle_input)

def compute(time, buses):
    
    times = {}

    for i in buses:
        start = 0
        while start < time:
            start += i
        times[i] = start

    return (times[min(times, key = times.get)] - time) * min(times, key = times.get)

print(compute(time, buses))


