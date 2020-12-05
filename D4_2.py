'''
Can probably do a regex for the entries here rather than putting them in a dict.
Looking at this problem I cannot see a way to do it without hard coding the correct fields.
I am 100% sure there is a nice way of doing this, but that is above my current level, so I shall hard code it.
'''


import re

AOC_data = open('D4_data.txt', 'r').read()

blank_line_regex = r"(?:\r?\n){2,}"

AOC_data = re.split(blank_line_regex, AOC_data.strip())
AOC_data = [i.replace('\n', ' ') for i in AOC_data]

valid = 0


def check_height(entries):
    if entries['hgt'][:-2].isnumeric():
        if entries['hgt'][-2:] == 'cm':
            if int(entries['hgt'][:-2]) in range(150, 194):
                return True
        elif entries['hgt'][-2:] == 'in':
            if int(entries['hgt'][:-2]) in range(59,77):
                return True
    else:
        return False


def fields_are_valid(entry):
    # need to check all conditions
    split_entry = [s.strip().split(':', 1) for s in entry.split()]
    entries = {k: v for k, v in split_entry}
    if (

    int(entries['byr']) in range(1920,2003) and
    int(entries['iyr']) in range(2010,2021) and
    int(entries['eyr']) in range(2020,2031) and
    entries['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and
    (len(entries['pid']) == 9 and entries['pid'].isnumeric()) and
    (entries['hcl'][0] == '#' and entries['hcl'][1:].isalnum() and len(entries['hcl'][1:]) == 6) and
            check_height(entries) == True):
        return True
    else:
        return False
    # so now how am I going to go through the strings and check?


for entry in AOC_data:

    # Becuase 'cid' is optional all other cases must be there?
    if len(entry.split(' ')) > 7 and fields_are_valid(entry) == True:
        valid += 1
    if len(entry.split(' ')) == 7 and 'cid' not in entry and fields_are_valid(entry) == True:
        valid += 1


print(valid)

