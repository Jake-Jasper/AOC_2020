# Can probably do a regex for the entries here rather than putting them in a dict.

import re

AOC_data = open('D4_data.txt', 'r').read()

blank_line_regex = r"(?:\r?\n){2,}"

AOC_data = re.split(blank_line_regex, AOC_data.strip())
AOC_data = [i.replace('\n', ' ') for i in AOC_data]

valid = 0

for entry in AOC_data:

    entry = entry.replace('\n', ' ')
    if len(entry.split(' ')) == 8:
        valid += 1
    # Becuase 'cid' is optional all other cases must be there?
    elif len(entry.split(' ')) == 7 and 'cid' not in entry:
        valid += 1

print(valid)

