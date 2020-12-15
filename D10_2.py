'''
Part 2 seems easier to understand, with the numbers you're given, how many combinations of chains can be made?

It is interesting that the problem is much harder to solve but easier, for me, to understand.

I did not think of a solution for this at the time, but saw a clever solutions that I thought I would keep for later
'''
import collections


AOC = open('D10_data', 'r').read().splitlines()

AOC = sorted(list(map(int, AOC)))


'''
You needed to look at the data and realise that it was a tribonacci sequence somehow

How someone figured this out is amazing to me

Figure out how many combinations of the previous numbers you can have to get to the current number. So to get to zero, you can have -3, -2 and -1
'''




def compute(AOC):
    combs = collections.defaultdict(int, {0: 1})
    for i in AOC:
        combs[i] = combs[i -1] + combs[i - 2] + combs[i- 3]

    return combs[AOC[-1]]

print(compute(AOC))
