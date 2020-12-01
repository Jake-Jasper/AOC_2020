AOC_list = open('D1_1_data.txt', 'r').read().split('\n')

AOC_list = [i for i in AOC_list if i.isnumeric()]


AOC = [int(i) for i in AOC_list]

for i in range(len(AOC)-2):
    for j in range(1, len(AOC)):
        for k in range(2, len(AOC)):
            if AOC[i] + AOC[j] + AOC[k] == 2020:
                print(AOC[i] * AOC[j] * AOC[k])
