AOC_data = open('D2_1_data.txt', 'r').read().split('\n')
AOC_data = [i for i in AOC_data if i != '']

'''
So
1-3 a: abcde should return True because a is in the first position and not the third
1-3 a: abade should return False because a is in the first position and the third

And at this point the data is loaded in as a string.

'1-3 a: cdefg'
'''


def check_string(string):
    num, letter, string = string.split(' ')
    lower, upper = num.split('-')
    letter = letter[0]

    if string[int(lower)-1] == letter and string[int(upper)-1] != letter:
        return True
    elif string[int(lower)-1] != letter and string[int(upper)-1] == letter:
        return True
    else:
        return False
    



count = 0

for string in AOC_data:
    if check_string(string) == True:
        count += 1

print(count)
