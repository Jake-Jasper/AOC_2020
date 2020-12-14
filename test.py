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
    start = 4
    for i in xmas[start:]:
        tmp = xmas[start-5:start]
        tmp =[sum((tmp[i],tmp[j])) for i in range(len(tmp)) for j in range(len(tmp)) if i != j]
        start += 1
        if i not in tmp:
            print(i)

        
        


compute_test(x)