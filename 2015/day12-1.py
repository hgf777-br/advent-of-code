import re

with open('./day12.json', 'rt') as f:
    file = f.read()
    numbers = re.findall(r'(-?\d+)', file)
    numbers = [int(n) for n in numbers]

print(sum(numbers))