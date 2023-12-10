from itertools import groupby

def compress(text: str):
    for a, b in groupby(text):
        yield f"{len([*b])}{a}"

def part1(data):
    for _ in range(40):
        data = ''.join(compress(data))
        print(data)
    return len(data)

def part2(data):
    for _ in range(50):
        data = ''.join(compress(data))
    return len(data)

data = '3113322113'

# for a,b in groupby(data):
#     print(*b)

print(part1(data))