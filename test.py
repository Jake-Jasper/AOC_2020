s = '''\
abc

a
b
c

ab
ac

a
a
a
a

b
'''

'''
The &= takes the commen elements in both and sets it to the var

a = set('abc')
b = set('bce')

a &= set(b)

print(a)
'''

def 
counts = 0
for group in s.split('\n\n'):
    lines = group.splitlines()
    all_counted = set(lines[0])
    for other in lines[1:]:
        all_counted &= set(other)
    counts += len(all_counted)

print(counts)
'''


