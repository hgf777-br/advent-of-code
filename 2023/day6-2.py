data = """40829166
277133813491063"""

data_test = """71530
940200"""
race = (71530, 940200)
race = (40829166, 277133813491063)

total = 1
speed = 1
count = 0
for time in range(1, race[0]):
    distance = speed * (race[0] - time)
    speed += 1
    if distance > race[1]:
        count += 1
total *= count

print('ganhas', total)
