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


class Reindeer:
    def __init__(self, name, speed, fly, rest):
        self.name = name
        self.speed = speed
        self.fly = fly
        self.rest = rest
        self.factor = 1
        self.timer = fly
        self.distance = 0
        self.points = 0

    def __str__(self):
        return self.name

    def update(self):
        self.distance += self.factor * self.speed
        self.timer -= 1
        if self.timer == 0:
            if self.factor == 1:
                self.timer = self.rest
                self.factor = 0
            else:
                self.timer = self.fly
                self.factor = 1


data = data.splitlines()
data = [line.split() for line in data]
data = [(line[0], int(line[3]), int(line[6]), int(line[13])) for line in data]

reindeers = []
for d in data:
    reindeers.append(Reindeer(*d))

time = 2503  # 2503
for reindeer in reindeers:
    print(reindeer.name, reindeer.distance, reindeer.points)

for t in range(1, time + 1):
    winner = ('', 0)
    for reindeer in reindeers:
        reindeer.update()
        if reindeer.distance > winner[1]:
            winner = (reindeer.name, reindeer.distance)
    for reindeer in reindeers:
        if reindeer.name == winner[0]:
            reindeer.points += 1
            break

winner = ('', 0)
for reindeer in reindeers:
    if reindeer.points > winner[1]:
        winner = (reindeer.name, reindeer.points)
    print(reindeer.name, reindeer.distance, reindeer.points)

print('winner is ', winner)
