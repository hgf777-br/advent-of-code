import regex as re

total = 0

with open('./day8-data.txt', 'rb') as fb:
    for line in fb.readlines():
        total += len(line[:-1]) - (len(line[:-1].decode('unicode_escape'))-2)

print(total)
