'''
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.

. = FLoor
L = Empty seat
occupied seat = #
'''
import pprint, copy

test_case = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''
test_case = test_case.splitlines()
test_case = [list(i) for i in test_case]




AOC = open('D11_data', 'r').read().splitlines()
AOC =  [list(i) for i in AOC]


def convolve(arr):
    # arr[i][j] is current seat
    new = copy.deepcopy(arr)
    for i in range(1, len(arr)-1):
        for j in range(1,len(arr[0])-1):
            seat = arr[i][j]
            adjacent =  arr[i-1][j-1:j+2] + arr[i][j-1:j+2] + arr[i+1][j-1:j+2]
            adjacent.remove(seat)
            if seat == 'L' and '#' not in adjacent:
                new[i][j] = '#'
            elif seat == '#' and adjacent.count('#') >= 4:
                new[i][j] = 'L'
    
    return new, arr


def pad(arr):
    ## pad arr
    
    for i in arr:
        i.insert(0, '.')
        i.insert(len(i), '.')
    arr.insert(0,['.']*len(arr[0]))
    arr.insert(len(arr[0]),['.']*len(arr[0]))

    return arr
    

AOC = pad(AOC)
test_case = pad(test_case)

def compute(arr):

    new, arr = convolve(arr)
    if new == arr:
        print(sum(line.count('#') for line in new))
        return new
    else:
        compute(new)

# This is off by 13 for some reason, on my data. The answer should be 2368, which is what I got when running anthony's code
compute(test_case)




