import regex as re

total = 0

with open('./day8-data.txt', 'rt') as fb:
    for line in fb.readlines():
        s = re.findall(r'"|\\', line[:-1])
        total += (len(line[:-1]) + len(s) + 2) - len(line[:-1])

print(total)
