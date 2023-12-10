import re

target_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

pattern = re.compile(r'.+?: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
with open('./day16-data.txt', 'rt') as f:
    data = []
    sues = []
    for line in f.readlines():
        line = pattern.match(line).groups() # type: ignore
        data.append({line[0]: line[1], line[2]: line[3], line[4]: line[5]})
    for idx, sue in enumerate(data, 1):
        new_sue = True
        for k in sue:
            if int(sue[k]) != target_sue[k]:
                new_sue = False
        if new_sue:
            sues.append(idx)
    print(sues)
