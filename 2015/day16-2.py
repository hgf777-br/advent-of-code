import re
from operator import lt, gt, eq

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
    data = [{name: int(count)  for name, count in re.findall(r'(\w+): (\d+)', line)} for line in f.readlines()]
    sues = []
    for idx, sue in enumerate(data, 1):
        new_sue = True
        print(idx, sue)
        for k in sue:
            if k in ('cats', 'trees'):
                if int(sue[k]) <= target_sue[k]:
                    if idx == 405:
                        print('ct')
                    new_sue = False
                    break
            elif k in ('pomeranians', 'goldfish'):
                if int(sue[k]) >= target_sue[k]:
                    if idx == 405:
                        print('pg')
                    new_sue = False
                    break
            elif int(sue[k]) != target_sue[k]:
                if idx == 405:
                    print(sue[k], target_sue[k])
                new_sue = False
                break
        if new_sue:
            sues.append(idx)
    print(sues)
    ops = dict(cats=gt, trees=gt, pomeranians=lt, goldfish=lt)
    for i, sue in enumerate(data, start=1):
        if all(ops.get(k, eq)(v, target_sue[k]) for k, v in sue.items()):
            print(i)

