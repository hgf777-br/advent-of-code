import math
from itertools import permutations

data = '''Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70'''

data = data.split('\n')

cities = {}

for line in data:
    line = line.split()
    cities.setdefault(line[0], {})[line[2]] = int(line[4])
    cities.setdefault(line[2], {})[line[0]] = int(line[4])

for city in cities:
    print(cities[city])

print('-'*40)

print(len(list(permutations(cities))))

totals = [sum(cities[p[i]][p[i+1]] for i in range(len(p)-1)) for p in permutations(cities)]

part1 = min(totals)
part2 = max(totals)
