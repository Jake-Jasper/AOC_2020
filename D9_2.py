'''
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

3199139634

There must be a nice way of dion this, but all I can think of is doing the bubble sort way which is very slow.
This only took a second for me I am actually suprised.
'''
AOC = open('D9_data', 'r').read().splitlines()
'''
def compute_test(xmas):
    goal = 3199139634
    xmas = list(map(int, xmas))
    
    for i in range(len(xmas)):
        for j in range(i+1, len(xmas)):
            contig = xmas[i: j+1]
            if sum(contig) == goal:
                return min(contig) + max(contig)


print(compute_test(AOC))
'''

# Found a slidng window approach that was much faster

def sliding_window(xmas):
    xmas = list(map(int, xmas))
    goal = 3199139634 
    start = 0
    end = 0
    total = xmas[0]

    while True:
        if total < goal:
            end += 1
            total += xmas[end]
        elif total > goal:
            total -= xmas[start]
            start += 1
        else:
            contig = xmas[start:end +1]
            return min(contig) + max(contig)
print(sliding_window(AOC))



