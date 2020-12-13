'''
I think I will try a brute force approach here
'''

AOC = open('D8_data', 'r').read().split('\n')
AOC = [i for i in AOC if i != '']

def compute(AOC):

    AOC = list(enumerate(AOC))

    acc = 0
    loc = 0
    visited = []
    counter = 0
    # This is going out of range... we have and off by one error
    while AOC[loc] not in visited:
        counter += 1
        if AOC[loc][1].startswith('nop'):
            visited.append(AOC[loc])
            loc +=1
        elif AOC[loc][1].startswith('acc'):
            visited.append(AOC[loc])
            acc += eval(AOC[loc][1].split(' ')[1])
            loc += 1
        elif AOC[loc][1].startswith('jmp'):
            visited.append(AOC[loc])
            loc += eval(AOC[loc][1].split(' ')[1])
    print(loc)
    return acc, counter

def try_all(AOC):
    for i in range(len(AOC)):
        
        if AOC[i].startswith('nop'):
            tmp = AOC[:]
            x = AOC[i]
            x = x.split()
            tmp[i] = f'jmp {x[1]}'
            acc, counter = compute(tmp)
            #print(counter)
            if counter == len(AOC):
                return acc
            #return acc
        
        if AOC[i].startswith('jmp'):
            tmp = AOC[:]
            x = AOC[i]
            x = x.split()
            tmp[i] = f'nop {x[1]}'
            acc, counter = compute(tmp)
            #print(counter)
            if counter == len(tmp):
                return acc
      
print(len(AOC))
print(try_all(AOC))

#print(compute(AOC))

'''
This is so close we are just off by one, doens't seem to meet the last condition.

This is failing to find the solution somwhere we got through all the conditions and do not meet the requirement


'''
