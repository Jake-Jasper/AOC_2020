

AOC_data = open('D6_data', 'r').read()


def foo(data):
    count = 0
    for group in data.split('\n\n'):
        lines = group.splitlines()
        all_counted = set(lines[0])
        for other in lines[1:]:
            print(other)
            all_counted &= set(other)
        count += len(all_counted)
        print(all_counted)

    return count

    
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

print(foo(s))
