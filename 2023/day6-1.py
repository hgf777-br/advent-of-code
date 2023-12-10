data = """40     82     91     66
277   1338   1349   1063"""

data_test = """7  15   30
9  40  200"""
data = data.split('\n')
races = [(time, distance) for time, distance in zip((int(t) for t in data[0].split()), (int(d) for d in data[1].split()))]

total = 1
for race in races:
    speed = 1
    count = 0
    for time in range(1, race[0]):
        distance = speed * (race[0] - time)
        speed += 1
        if distance > race[1]:
            count += 1
    total *= count

print('ganhas', total)
