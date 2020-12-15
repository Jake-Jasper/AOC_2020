'''
Reading this one I would be lying if I understood what it wants me to do. But looking at the example given, it would seem that It wants us to count the number of 1 nad 3 gaps between the numbers and multiply them together?
'''


AOC = open('D10_data', 'r').read()



def compute(test_case):
    test_case = test_case.splitlines()
    data = sorted(list(map(int, test_case)))
    # starts from 1 because th difference from element 1 to the adapter is one and the end +3 because the joltage is max +3
    ones = 1 #
    threes = 1
    for i in range(1,len(data)):
        if data[i] - data[i-1] == 1:
            ones += 1
        elif data[i] - data[i-1] == 3:
            threes += 1

    return ones * threes

test_case = '''\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''

print(compute(AOC))
