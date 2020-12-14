'''
Will loop over relveant numbers sum the combinations and if there isn't a combination that equals the relevant number return the stage in the loop
This gets the correct answer let's transfer it to the real thing, we may run into to some optimisation issues I suspect
'''

AOC = open('D9_data', 'r').read().splitlines()

TEST_S = '''\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''

x = TEST_S.splitlines()
expected = 127

def compute_test(xmas):
    xmas = list(map(int, xmas))
    start = 5
    for i in xmas[start:]:
        tmp = xmas[start-5:start]
        tmp = [sum((tmp[i],tmp[j]))for i in range(len(tmp)) for j in range(len(tmp)) if i !=j]
        if i not in tmp:
            print(i)
        start += 1

compute_test(x)

