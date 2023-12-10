data = '''Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.'''

# data = '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''

data = data.splitlines()
data = [line.split() for line in data]
data = [(line[0], int(line[3]), int(line[6]), int(line[13])) for line in data]

winner = ('', 0)
time = 2503
for reindeer in data:
    factor = reindeer[2] + reindeer[3]
    distance = (time//factor)*reindeer[1]*reindeer[2]
    remainig_time = time - (time//factor)*factor
    if remainig_time >= reindeer[2]:
        distance += reindeer[1]*reindeer[2]
    else:
        distance += reindeer[1]*remainig_time
    print(reindeer[0], distance)
    if winner[1] < distance:
        winner = (reindeer[0], distance)

print(winner)
