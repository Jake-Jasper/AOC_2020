

AOC_data = open('D6_data', 'r').read().split('\n\n')

AOC_data = [i.replace('\n', '') for i in AOC_data]

print(sum(len(set(i)) for i in AOC_data))

