'''
I do not recognise what the underlying CS structure the puzzle it testing here, but it seems that, part1 at least, is quite simple
'''

AOC = open('D8_data', 'r').read().split('\n')

AOC = list(enumerate(AOC))

acc = 0
loc = 0
visited = []


while AOC[loc] not in visited:
    if AOC[loc][1].startswith('nop'):
        visited.append(AOC[loc])
        loc +=1
        continue
    elif AOC[loc][1].startswith('acc'):
        visited.append(AOC[loc])
        acc += eval(AOC[loc][1].split(' ')[1])
        loc += 1
    elif AOC[loc][1].startswith('jmp'):
        visited.append(AOC[loc][1])
        loc += eval(AOC[loc][1].split(' ')[1])

print(acc)
