from math import trunc
import numpy as np
from itertools import combinations

data = """...........................#.......#.....................#................#.......................................#.............#...........
..................................................#...........................................#.......................................#.....
........#....................................#....................................#.......................#.................................
........................................................................................................................#...................
#...................#.......................................#...............................................................................
...............#.......................................................................#...........#...........#............#...............
........................................................#...........................................................................#.......
..............................................#.....................#...................................#...................................
.............................#......#.....................................#.................................................................
.......................#...........................#............................................#.................#.........................
.....#.....................................................................................................................................#
...........#......#...............................................#..............................................................#..........
.......................................................................................#...................#................................
..............................#........................#....................................................................#...............
.................................................#..........#......................................#........................................
........#................................#...................................................#..........#.....#......#......................
.........................#.........................................................................................................#........
............#.................................................................#.........#...................................................
....................#.......................................................................................................................
............................................#.............#.................................................................................
..............................#.....#...........................................................#........................................#..
#.........#........................................#............#................................................................#..........
.........................................................................................................#..................................
..................#.....................................#..............................#.............................#.......#..............
...........................#..............................................#.................................................................
...........................................................................................#......#.........................................
.......................#.......#..................#..........#....................................................................#......#..
.....#.............................................................#............................................#...........................
....................................#............................................#......................................#...................
.....................................................................................................................................#......
..............#.............................#.......#....................................#..................................................
.........#......................................................#.................................................#...........#.............
............................................................................................................................................
.#.....................................................................#..........#....................#....................................
..................................#....................................................................................................#....
...........#.........#............................#......#........................................#.........................................
................................................................................................................................#...........
..............................................................................................#.............................................
......................................#..............#.......................................................#...........#..................
....#............#.........................................#................................................................................
............#..............#.............................................................#..................................................
...............................................#...................................................#..........................#............#
..................................#.........................................................................................................
........................................................................#...........#...............................#.....#.................
#.........#..............#..................................................................................................................
.......................................................................................................................................#....
................#..........................................#................#................#.................#..................#.........
...................................................................#........................................................................
................................................#....................................................#......................................
.....................................................#..........................................#...........................................
..........................#.................................................................................................................
.....#.....#.....................................................................#.......#..............................#...................
.....................#........................#...............................................................#................#............
................................#........#............................................................#.....................................
.................................................................................................#................#.........................
..................................................................#.................................................................#.......
............................................................................................................................................
................................................#.....#.................#................#....................................#.............
......................#.....................................................................................#........#..................#...
..........#........................#................................................#.......................................................
....#.............#...................................................................................#...........................#.........
.........................................#..................................................#.....................#.........................
............................................................................................................................................
..........................#..................#..........................#.................................................#.................
.......................................................................................#......................#.............................
................................#......#.....................#................................#......................#..................#...
............................................................................................................................................
........#.........#.................................................................#.......................................#......#........
..........................................#........#........................................................................................
............................................................................................................................................
...............................................................................................#.......................#....................
............................#............................................................................#.................................#
............................................................................................................................................
......#...........#...................................#........#........#...................................................................
....................................................................................#.........................................#.............
.......................................#.........#......................................................................#...................
............................................................................................................................................
..............................#..................................................................................#..........................
.......................#......................................................#................#............................................
........#..........................................................#..................#................#...........................#........
.............#.....#................#.......................................................................................................
.........................................#...............................#.....................................#............................
.#...........................................................#...................#..................#.......................................
...........................#.................#............................................................................#.................
.......................................................#..................................................#.........#.....................#.
......................................................................................#........#............................................
......#.........#.................#............................#................................................................#...........
..........................................................................#.................................................................
...........#.........#.........................................................................................#............................
...........................................#..............#.................................................................#...............
.....................................................#.............#...................................................................#....
....#.........#.................#................................................................................................#..........
.......................#.......................................................#..................#........#............#...................
......................................#..................................#...................#..............................................
.......#.....................................#......................................................................#.......................
..#..........................#...........................#..........................#.......................................................
...........#.............................................................................#......................#......................#....
...............................................................#.........................................#..................#...............
.................#......................#........#...............................#..........................................................
......................#.......................................................................#......#..............................#.......
............................#......#......................#.................................................................................
...........................................#.............................#..........................................#.....#.................
...........#......................................................................................#.....................................#...
.......................................................#..........#....................................#.......#.................#..........
...............................#........................................................#...................................................
..#.....#.............................#................................#....................................................................
..................................................#...........................#.............................#...............................
.............................................................................................#.....#........................................
...............#........................................#.............................................................#.....................
#....................#...........#..........................................................................................................
............................#..............#..............................#.......................................................#.........
.....................................................................................#......................................................
.................#...........................................................................................#..............................
.........#..............#............................................................................................#...................#..
....................................#................#..............................................#.......................................
...............................#.........#.................#...................#.........................#..................#...............
#.............................................#........................................#....................................................
......................................................................#..........................................#..........................
.............#...............................................................................#........#...............................#.....
...#............................................................#............................................#..........#..................#
...................................................#........................................................................................
..........................................#..............................#..................................................#...............
.............................................................#....................#.....................................................#...
.....................#..............#..................#................................................#...................................
.......#.......................#........................................................#.......#..............#.................#..........
..........................................................................................................................#.................
...#.......................................#....................#...................#.......................................................
..................#.........................................................................................................................
...........................#...........#...................................................................#......#.........................
................................#.............#....................#........................................................................
.........................................................................................#.......#..........................................
.......#.....................................................#................................................................#...........#.
..................................................#.......................#.................................................................
.............#...................................................................................................#...................#......
............................#.........#................#.............................#................#.....................................
......................#.......................................................................#...........................#.................
............................................................................................................................................
.............................................................................................................#.......#............#.........
.......#...........#.....#.....#.............................#..............................................................................
.............#...............................#..........#..........................................#......................................#."""

data_test = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


data = data.split('\n')
data = [[c for c in line] for line in data]
data = np.array(data, dtype=object)


def calculate_distance(data, galaxie_pair):
    galaxie_one = np.argwhere(data == galaxie_pair[0])
    galaxie_two = np.argwhere(data == galaxie_pair[1])
    distance = abs(galaxie_one[0, 0] - galaxie_two[0, 0]) + abs(galaxie_one[0, 1] - galaxie_two[0, 1])

    return distance


# Expanding the Universe!
# Expanding rows
max_y, max_x = data.shape
index = 0
while index < max_y:
    if '#' not in data[index, :]:
        data = np.insert(data, index, '.', axis=0)
        index += 1
        max_y += 1
    index += 1
# Expanding columns
max_y, max_x = data.shape
index = 0
while index < max_x:
    if '#' not in data[:, index]:
        data = np.insert(data, index, '.', axis=1)
        index += 1
        max_x += 1
    index += 1
max_y, max_x = data.shape
print('Universe Expanded!')

# Numbering the galaxies
number = 1
for y in range(max_y):
    for x in range(max_x):
        if data[y, x] == '#':
            data[y, x] = number
            number += 1
print('Galaxies numbered!!')
# Creating galaxies pairs
galaxy_pairs = list(combinations(range(1, number), 2))
print(f'Galaxies pairs created!!! ({len(galaxy_pairs)})')

# Calculating distances between galaxies
result = sum(calculate_distance(data, galaxy_pair) for galaxy_pair in galaxy_pairs)

print('day 11 part 1:', result)
# print(data)
# print(max_y, max_x)
# print(galaxy_pairs)
