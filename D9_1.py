'''
yes this did take ages to run

'''
AOC = open('D9_data', 'r').read().splitlines()

def compute_test(xmas):
    xmas = list(map(int, xmas))
    start = 25
    for i in xmas[start:]:
        tmp = xmas[start-start:start]
        tmp = [sum((tmp[i],tmp[j]))for i in range(len(tmp)) for j in range(len(tmp)) if i !=j]
        if i not in tmp:
            print(i)
            break
        start += 1

compute_test(AOC)

