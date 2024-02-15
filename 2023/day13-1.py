from time import time

data = """#.###.##..#....
.#.###.....####
...##...###.##.
...######..#..#
##.#..#.##..##.
.#.##..#....##.
##..##.#...####
.####..##.#####
#.####.#....##.
..#.###.#..#..#
##...####...##.
##...####...##.
..#.###.#..#..#
#.###..#....##.
.####..##.#####

##..#.#......#..#
.....#..#.#######
...########...##.
..#.#.#.###...##.
..#.#..#.#.#.#..#
..##...#.##.#.##.
###.####..##.#...
....#..#.#..#.##.
....#.###..##....
..##.#..##.######
...##..#.#.##....
...#.#..#........
###....##..######
..#...##..##.#..#
..#.......#...##.

#####.###
.#.###..#
##...##.#
....###.#
....###.#
##...##.#
.#.###..#
#####.###
..##.#.##
###...##.
.##.#.###
.##.#.#.#
###...##.

..###...#####
#######..#..#
########.#..#
..###...#####
##.###..#####
#.....###.##.
#..###..##..#
.#.#.##...##.
.#.##########
..###.###.##.
####..#.#....
##.##.....##.
###...##.....
...#.#.##....
.##..#.#.#..#

#......#...
.#.#.##....
##..####.##
...##....##
..#...##...
#..#.......
##..#.#..##
###..#.####
###..#.#.##

..#......#...
###.####.####
.#..#..#.##..
.#..#..#..#..
##..####..###
##..####..###
.....##......
.###.##.###..
##..####..###
#.########.##
.##......##..
.#..#..#..#..
#...####...##

#....##.#..#.##
.#..#.##.####.#
.#..#.##.####.#
#....##.#..####
#.##.#..#.####.
......#..#....#
.#..#...#..##.#
.#..#.###.##.##
..##...##...#.#
......#.####.#.
#.##.#..#......
..##...###.#.#.
......#..##.#.#

..##.######
##.....#..#
..#.###.##.
#.###..####
.##.#..#..#
.##....#..#
#.###..####

...#.####.#
##.#..##..#
##.........
..##..##..#
##..#....#.
##....##...
..#........
##..#.##.#.
...#......#
...#.###..#
...########
####..##..#
..#.##..##.
###..####..
..#.######.

##.....###...
##.....###...
##.##.####.##
###..###.##..
........#..#.
#.#..#.#..##.
##.##.###..#.

...##.####.#.#.
..####.#...#...
.....##.#.#..##
##.....###.#.#.
######.###.#...
##.##....#.####
...#.####..####
..###....##.##.
..###..#...#..#
..###..##..#..#
..###....##.##.
...#.####..####
##.##....#.####
######.###.#...
##.....###.#.#.

##.#####.####..
..#.##..#.##.#.
..#.########...
###.###.###....
...#####.##.#..
##.#..#..#...#.
...##....#..#..
##..##...##.##.
##..##..####.#.
##....#.#.##..#
###...#.#.##..#
##..##..####.#.
##..##...##.##.

...#.##.##.##.#..
#....#..##..#....
.#..#.##..##.#..#
.#..#.##..##.#..#
#....#..##..#....
...#.##.##.##.#..
####.##....##.###
.#.##........##.#
######.#..#.#####
#.##...#..#...#..
.#.#....##....#.#
....#.#.##.#.#...
##..###.##.###..#
#.#.#.#....#.#.#.
.######....######

..#..###.
..#.#.###
..#...###
.##....##
....#.#.#
####.##..
####.##..
....#.#.#
.##....##
..#...###
..#.#.###

....##.##
#.##.....
###....#.
###....#.
#.##.....
....##.##
#.#..####
#.#.....#
.##.#.#.#
##...#.#.
##...#.#.
.#..#.#.#
#.#.....#
#.#..####
....##.##
#.##.....
###....#.

###.#........
#.#.#.#.##.#.
##.##.#.##.#.
..##.#.#..#.#
.##...#....#.
.#...##.##.##
.#...##.##.##
.##...#....#.
..##.#.#..#.#
##.##.#.##.#.
#.#...#.##.#.
###.#........
#.....#.##.#.

#.##..###..####
.##...#..###..#
.##...#..#.#..#
.#.######..##.#
#....##.###.###
.###..#.##.##..
...#.#.##..#...
#.........###.#
###.#.....##..#
###.#.....##..#
#.........###.#
...#.#.##..#...
.###..#.##.##..
#....##.###.###
.#.######..##.#
.##...#..#.#..#
.##...#..###..#

.....######....
..#.#..##..#.#.
##.#........#.#
###....##....##
##.....##.....#
..############.
..#...#..#.....

##...##
#..###.
#...#.#
#...#.#
#..###.
##...##
###.##.
#.#..##
..##..#
.#..#..
#.##..#
#....#.
#....#.
#.#...#
.#..#..

#..##.###..
.##....#.#.
......##.#.
#..#.###.##
######.....
######.....
#..#.######

...##..##.#..###.
..#.#..#.#....##.
####.##.####....#
.##.#..#.##..#..#
.#.#....#.#...###
##..####..###..#.
##..####..###..#.
.#.#....#.#...###
.##.#..#.##..#..#
####.##.####....#
..#.#..#.#....##.

####.#...
...#.####
##...##..
###.#....
..#.#.#..
###....##
####.####
..##.#..#
##.###..#
.#.#..#.#
###.###..
###.#.###
######.#.
..#.#.###
####....#
####....#
..#.#.###

#..##..##..##..##
##.#....####....#
##.######..######
...######..######
#..#.##.#..#.##.#
#####.########.##
###..##..##..##..

###....####
####...##.#
##.##.##..#
####..##..#
##.##.#.##.
##.###.####
####.######
####.#..##.
.....#.#..#

..##.#...
..##.##..
..#..##.#
##.######
..#.#..#.
##.#.#.##
...##..#.

....###..###...
.....##..##....
..##..#..#..##.
...###....###..
##.##########.#
##.........#..#
####.#....#.###
..#.###..###.#.
##....#..#....#

.....#.#.####.#
#....##.#..#..#
##..##.#.....#.
#....####......
..##..##..#....
.####.#####.##.
##..##.##.##.##
##..##.#.....#.
######.##.###.#
..##..#.##..#.#
..##..#.##..#.#
######.##.###.#
##..##.#.....#.

.#####...#.
.#..####..#
#####.##.##
#.#.##.###.
.###..####.
#.##.......
..##.##....
..##.##....
#.##.......
.###..####.
#.#.##.###.
.####.##.##
.#..####..#
.#####...#.
##.....####
.#.#..###..
.#.#..###..

#.#.##.....
#..#####..#
..#..#.....
..#..#.....
#..#####..#
#.#.##.....
#......####
##.#.#..##.
.#.####...#
..###.#....
..#...#####
....####..#
#.#.####..#
#..####....
#.#.#.#####
#..#.#.....
...#.######

##..##........#
..##..#..#.#.#.
..##..#..#.#.#.
##..##........#
.####.#.#.#....
..##.....##..##
#....######.#..
.####....##.#..
.####.#.#...#.#
######.###.#..#
.........##....
.####.#..###..#
########..#....
.####......#..#
........#####.#
#...###.....#.#
......#.....##.

#..##...##.
###..####.#
####...####
.##.#..#..#
....##....#
####..#...#
####..#...#
....##....#
.##.#..#..#

.######.#..
#..##..#.##
##.##.##...
.######....
..#..#.....
#########..
.##..##....
##.....#.##
..####.....
#########..
#.####.#.##
.######....
.##..##.###
#......#...
##....##.##
#......#.##
...##...#..

#....###.#.#..#
#....###.###..#
..#..####..####
.###..##.##.##.
...###.##.#....
....###....####
..#..#.#...#..#
.#.####..#..##.
#..#.###..#####
###.#.###..####
..######..##..#

###.##.####
##.####.###
####..#####
##......##.
.#.####.#..
..#.##.#...
..#.##.#..#
...####....
##.#..#.###

.##########
....#...#.#
....#...###
.##########
......###.#
#..#.###.#.
#..#.###.#.

#######..##
##..##.####
##..###.###
.#..#.###..
..##.......
....#.##.##
..##...##..
.#..#.#.#..
..##..##.##
.####.###..
#....######
......#.#..
######.#...

..#..#.##..##
###.#...#..#.
..####.######
...#...#.##.#
#..#.#.......
#.#..##..##..
#.###........
#.#.#........
#.#..##..##..

...####..#..#.#
###....#..#..##
.#....#.#.#.###
.#.....#.......
#.##...##.#..##
####..#......##
#...#.#.#.#.#..
#.##.#####..#..
.....####.#####
.....####.#####
#.##.#####..#..

........##...
########...#.
##########...
#########.#..
#########.#..
#..##..#.#.##
.##..##..####
########..#.#
##.##.##.#.#.

..#...###.####.#.
..#...###.####.#.
#.#......#..#...#
#..#...#######...
##.##...#####.#.#
######...###..##.
#######..###..##.

##..#...###
..###.#.##.
##.#.#.#.#.
..#.##.#...
####.####..
####.#.#...
...#..##.##
...#..#.#..
..####..###
...#.####.#
...######.#

.##..##....##..
.##..##....##.#
##########...#.
#.#..#.##..#.#.
##....##.####.#
#.####.#..#....
#.#..#.#.#..#..

####.....#.##.#
..##...#....###
..##...#....###
####.....#.##.#
#...#..##.#..##
#..##.....#...#
#.##....##.##.#
#.##.##..##..#.
.#....##.#.#.##
##.#.#####...#.
##.#.#####..##.

....#..##
.##...###
....#....
.##.##.#.
.##...#.#
.##...#.#
.##.##.#.
....#....
.##...###
....#..##
.###...#.
#..#.....
.....#..#
#..#.####
........#
######...
####.....

.#....#.#.#..
#.####.###.##
.#####..#..##
########.##..
##.##.##.....
#..##..#...##
#########.#..
##.##.###..##
.#.##.#......

#..###..###
......##...
.....#..#..
##..#....#.
....##..##.
##.#.#..#.#
..####..###
##.##.##.##
..##.####.#
..##.####.#
....#.##.#.
....#....#.
..#........
###........
##.#.####.#

#....#...#...#.##
.#..#...##..#....
.####.##..#..##..
..###.....##..#..
.####..#..##.####
..##..###.#.#.###
##..##.#.###.####
######...#.##....
#######.....##.##
#....##..#.#.....
.#..#.#...#...#..

#.####...##
##..##..#.#
.####......
..##..#....
.#..#..#.##
.####.#....
#....###.#.
##..###.#..
#.##.##.###
.#..#.##..#
.......#...
.####.#..#.
##..###....
##..###....
.####.#..#.

.##...#..##
..##.#.##..
#.#..#..###
.#####.#.##
..#..###...
###..#...##
####.##....
..#..###...
...#.##....
....#....##
.....#..#..
####..#.#..
###.#.#.#..
#..##......
#..#.#..#..
.#.#..#..##
.#.#.##..##

####..#...#..#.
####.....##..##
#..#.....##..##
#..#.##.#..##..
#####..###.##.#
...#...........
.##..#...######
#..#.#.#...##..
#..##.....#..#.
.....#...##..##
#..####...#..#.
.##...#.##....#
.##.####..#..#.
.....####......
.....##...#..#.
####.....##..##
####..#.##....#

...#...##...#
##.##.####.##
##.##..##..##
#######..####
#######..####
##.##..##..##
##.##.####.##
...#...##...#
#......##....
.##.#......#.
#..##.#..#.##
.#.#.######.#
##.#...##.#.#

.#.###.#.
.######.#
##.#...##
#.##....#
####.####
#.##....#
#.##....#
#.##.####
#.##....#
##.#...##
.######.#
.#.###.#.
.#..#...#
.###.#.#.
.###.#.#.

.....##
......#
#.#...#
.#.##.#
.#.##.#
#.#...#
......#
.....##
.####..

.#####.......#..#
#.#.#.#....#....#
...#...#.##....##
######...##.#.#..
#.#..####...##.##
####....##....##.
####....##...###.
#.#..####...##.##
######...##.#.#..
...#...#.##....##
#.#.#.#....#....#
.#####.......#..#
.#.##...#.###...#
..####.###..####.
..#.#..#.##.#....
..#.#..#.##.#....
..####.###..####.

.#..#.#.#.#.#
.#..#.#.#....
..##..#..#.##
##..####...##
##..####...##
..##..#.##.##
.#..#.#.#....
.#..#.#.#.#.#
#.##.##...#.#
..##...##...#
......##.#.#.
######.......
##..#######..
#.##.###.....
######....##.

.###..####.##..#.
..#....##..##.#.#
..#.#.....##.#.#.
..###.##..#..####
.#.#.#.#.#..###.#
......#########.#
.....##########.#
###..##..######..
##.###.......###.
##.###.......###.
###..##..######..
.....##########.#
......#########.#

#.##...
##.####
..##...
...#...
##.##..
.#...##
##...##
.##.#..
..###..
.#.####
#..#...
#####..
.##....
.##....
###.#..

#....##..##..##
#.##.#..####..#
##..###.#..#.##
.........##....
.#..#.##.##.##.
#.##.####..####
..##....#.##...
.#..#..##..##..
#.##.##.#..#.##

###.##....##.
##...........
##.##......##
...##.#..#.##
..####....###
..####....###
...##.#..#.##
##.##......##
##...........
###.##....##.
.####.#..#.##
##.#.#.##.#.#
..##.#....#.#
#...#..##..#.
..#.#..##..#.
##.....##....
.###.######..

#....#.######.#..
##..##.###.##.##.
.#..#.#.####.#.#.
######.#....#.###
######.#....#.###
######.#....#.###
.####.#......#.##

.#.#.##....##.#
...#..##..##..#
..###........##
.#...#.####.#..
..##.##.##.##.#
###...##..##...
..###.##..##.#.
##..##..##..##.
###...#.##.#...
.#..##..##..##.
...###......###
##.###.#..#.###
.####........##
.####........##
##.###.#..#.###

#.##.####.##.
....##..##...
..#.#....#.#.
.###......###
.###......###
..#.#....#.#.
....##..##...
#.##.####.##.
.#.#..#...#.#
...###..###..
....######...

#........##.#
####.#.#.##..
####.#.#..#..
#........##.#
.#.##.#..#.#.
.#.##.#..#.#.
#........##.#
####.#.#..#..
####.#.#.##..
#........##.#
.....##..###.
##...##.###..
..#....##.#.#
....##.#..###
.##....#.#.#.
.########.#.#
#.#####..####

....#.#..#.
....#.#..#.
.#.###..#..
..###......
##...##...#
####.#.###.
..##.......
..##.......
####.#.###.
##...##...#
..###......
.#.###..#.#
....#.#..#.

...##.###.##.
#....#..##.##
.#.#..#..##..
.##....#..##.
###....#..##.
##..#.#.##.##
.#..#..#..#..
.#..#..#..#..
##..#.#.##.##
###....#..##.
.##....#..##.

#.#...#..#...#.
#.#...#..#...#.
...#....#..#..#
###..#.#.####.#
..#.#.##.###...
....###.##.####
#.####...#.##.#
.##.#...##..#.#
.##.##......#.#
.###.#.#....###
..#......###.##
.#.##...#....##
.#..#..#.#.##.#
.#..##.#.#.##.#
.#.##...#....##
..#......###.##
.###.#.#....###

#.####.##..
#..##..####
#......####
#.####.##.#
#.####.#.#.
#.####.###.
..#..#..###
#.#..#.##.#
.#....#.###
.##..##.##.
..#..#....#
.#..#.#.#.#
###..###...
###..#####.
###..#####.

#.##.#.#...
.####..##..
.#..#..####
##..###.###
#....###...
#.##.#...##
.#..#......
.####...###
########.##
#....#..###
.#..#...#..
##..#.#####
##..###.###

............###
#.########.##..
#.#..##..#.#.##
...######...#..
.##########.#..
#.#..##....#...
.##......##....
..#.####.#.....
#..#.##.#..#.##
#..##..##..#.##
.#.######.#.#..

#..##..#.####
#########.##.
#..####.#####
#..##...#####
#######......
.##.##....##.
#..#..##.....
.##......#...
#..#..#...##.
#########.##.
#..####..####
########..##.
.##...##.####

...##..####
...##..###.
##.#.#####.
...#.#..###
##...##....
..#.....##.
..#.##.#.##

.##..#.
####...
...##.#
.##.#..
####..#
.##.#..
....###
....###
.##.#..

#.#.....##..##.
.###.##..#..#.#
##.#...#..#.###
.....#........#
##..#.##...#.##
....#..#####..#
##..#.#..#.###.
##..#.#..#.###.
#...#..#####..#
##..#.##...#.##
.....#........#
##.#...#..#.###
.###.##..#..#.#
#.#.....##..##.
#.#.....##..##.

####...###...#..#
.##.##.#....##..#
.##....##.#.#..##
....##.......##.#
.##.##...#.#.##..
####..###.#.#.#..
#..###.##........
.##..##.#..###...
#..##.#.#..##....
.#...#.#.#.#.####
....#....#.#...##
#..####..###..#.#
#..##...###.##...
.##....#.#.#..###
####.###.#...#...
####.###.#...#...
.##....#.#.#..###

.#...####.#######
.#.#.#..#........
..#.#...#..##..##
..###.#.#.###..##
###......##.####.
#.####..#...####.
...#####...#...##
#...#..#.#.##..##
##.....#.#..####.
##.....#.#..####.
#...#..#.#.##..##

..#....#.
..#.###..
##...####
.....#...
..#...###
..#.##.#.
..#.##.#.
..#...###
.....#...
##...##.#
..#.###..
..#....#.
##.....##
..#...##.
####.....
..#.##.##
...#...#.

#....#...####
#.##.#.#.####
######...##..
##..####..#..
##..###..##..
.#..#..#.#...
......###..#.
.#..#.#######
#######.##.##
######..##.##
##..###.###..
.####.##..#..
.......##..##

.#....##....#
.#....##....#
#...#.##.#...
#....####..#.
..#.######.#.
#..#.#..#.#..
###.#.##.#.##

#....##
.####.#
.####..
#....##
#.##.#.
#....##
#.##.##

..#####.#.###..##
##.#.#..##...#.#.
#..#..#########.#
#..#..#########.#
##.#.#..##...#.#.
..#####.#.###..##
..#.#.###.#.#...#
..#.#...#.#......
.#####......#.##.
.#..#.###.##..###
.####..##...#..#.
.####..##...#..#.
.#..#.#.#.##..###

#####...#
#.##..##.
...#.#..#
..##.#.#.
..####.#.
...#.#..#
#.##..##.
#####...#
.......#.
##..###.#
..#.#.#..
#...#...#
###..##.#
.#..##..#
.#..##..#

###....#####.##.#
###....#####.##.#
.########..#.####
...#..#....#.#..#
#.#.##.#.###.####
.#.####.#.#.##...
#.#....#.#..##...
...#..#..#.#.....
##..##..#####.###
.###..###.#...#..
..######...##....
.###..###....#..#
....##.....#####.
#........###.#..#
#...##...##.#####

###.##.
##.#..#
##.#..#
###.##.
.##....
.##..#.
#..####

######.
###.#..
..###.#
..###.#
###.#..
######.
#.#.#..
..###.#
......#
####..#
##.####
##.####
####..#
......#
..#.#.#
#.#.#..
######.

...##.......#.#..
..#..#.#...#..##.
...##.......#.##.
............#.#.#
###########.###..
#.#..#.##..#...#.
..#..#.......##..
..####...###.....
..####...###.....
..#..#.......##..
#.#..#.##..#...#.

.####...#..##
#.##..####.##
.#####.#.##..
##..###...###
.##.##.######
#..#####...##
##.#..#.#.##.
#..#...#...##
.##..#..#.###
#.##....#.###
...#####.#...
#.###.....#..
#.###.....#..
...#####.#...
#.##....#.###

.#.##.#..
#..##..##
..#..#.##
##.##.###
.#.##.#..
.######..
##.##.###

..##..##..#
.###.#..#..
....#....##
....#....##
.###....#..
..##..##..#
#.##..#.#..
#.##..#.#..
..##..##..#
.###....#..
....#....##

##.#..#
..#....
...#..#
##..##.
...####
....##.
...#.##

#.##.#...
######.##
..##.....
.####..##
.####..#.
.#..#....
..##..###
#....##..
......###
#.##.##..
#....#...

..#.#......#.#...
###..##..##..####
.#.##########.#..
.#...######.#.#..
.####.#..#.####..
##.###....###.###
#..##########..##
.###.#....#.###..
...#.#....#.#....
###....##....####
.#...##..##...#..
###.##.##.##.####
##.###.##.###.###
####...##...#####
####..#..#..#####
##.#..#..#..#.###
....##.##.##.....

#..########..##
..#.#....#.#...
#..#..##..#..##
##.#.####.#.###
....##..##.....
##.####.###.###
#.###....###.##
..#.##..##.#...
...##....##....
.##.#....#.##..
##....##....###
..#.######.#...
##..######..###

....#..#.
###.####.
...######
.#.#.##.#
#.###..##
..#######
#.#######
#.#......
.#.#....#
#..#.#..#
.####..##
#.#..##..
#.#..##..

..####..##..####.
...##.#.##.#.##..
..#...##..##...#.
##.##..#####.##.#
....##.#..#.##...
..#.##.#..#.##.#.
##.####....####.#
...##.######.##..
##.##..#..#..##.#
###.#.######.#.##
##.#.###..###.#.#
....#........#...
..###.#....#.###.

#.##.#......#..#.
......###.##...##
#....#....##....#
#.##.#...####..##
..##..#.#.#......
..##...###...##..
.#..#..###.......

####.##.#..##.#
..#...##..#####
.##..#.......#.
.##..#.......#.
..#...##..#####
####.##.#..##.#
####...#..#....
....###.###.###
..###.#.#.##.##
.####.#.######.
.####.#.###.##.
..###.#.#.##.##
....###.###.###
####...#..#....
####.##.#..##.#

#####...##..#..
...#.#.#.#.##.#
.#.####..#.####
#...##.#.#..##.
....##.#.#####.
##..#....###.#.
#######.....##.
##..#####..#...
##..#####..#...
#######.....##.
##..#....###.#.
....##.#.#####.
#...##.#.#..##.
.#.####..#.####
...#.#.#.#.#..#
#####...##..#..
#####...##..#..

..#......#..#....
.###.##.###..#..#
.##..##..##..####
##.##..##.##.####
#.##.##.##.##.##.
.##.####.##......
#..#.##.#..#.####
..###..###.......
..##.##.##...#..#
.#..#..#..#.#.##.
#..#####...#..##.
##.######.###.##.
.#.##..##.#...##.
##........##.#..#
.##.#..#.##.##..#

..#.########.#.
...#.######.#..
##.#.#....#.#.#
##....####....#
..#######.####.
###.#......#.##
##..#..##..#..#

.#.##..
.##.###
##.##..
##.....
..#####
..#.###
###.#..
.#.#...
....#..
#..#.##
#....##
..#.###
..#.###
#.#..##
#..#.##
....#..
.#.#..."""

data_test_1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

data_test_2 = """..#......#...
###.####.####
.#..#..#.##..
.#..#..#..#..
##..####..###
##..####..###
.....##......
.###.##.###..
##..####..###
#.########.##
.##......##..
.#..#..#..#..
#...####...##"""

data_test_3 = """..####..##..##..#
...#..##.####.##.
.##.#.##..##..##.
...#..##.####.##.
.##..#..#....#..#
##.##.##########.
#########.##.####"""

data_test_4 = """###.##.##
##.####.#
##.#..#.#
####..###
....##...
##.#..#.#
...#..#..
##..###.#
##......#
##......#
..#.##.#.
...#..#..
##.####.#
....##...
...####..
....##...
##.####.#

.##.##...##...##.
#####..##..##..##
.....##..##..##..
.##.#.#.####.#.#.
.##...#.#..#.#...
....#..........#.
#..#..#......#..#
....###.....####.
.##...#.#..#.#...
.....#..####..#..
#..#...##..##...#
....#...#..#...#.
#..#.##########.#
#..##...####...##
#####.##.##.##.##"""

time_start = time()

lines = data.splitlines()

data = []
tmp = []
for line in lines:
    if line != "":
        tmp.append(line)
    else:
        data.append(tmp)
        tmp = []
data.append(tmp)


def transpose(pattern):
    new_pattern = [''] * len(pattern[0])
    for line in pattern:
        for idx, c in enumerate(line):
            new_pattern[idx] += c

    return new_pattern


def check_equal_lines(pattern):
    pos = None
    size = len(pattern)
    for idx, (i, j) in enumerate(zip(pattern, pattern[1:])):
        if i == j:
            pos = idx
            for k in range(1, size // 2 + 1):
                if pos - k < 0 or pos + k + 1 > size - 1:
                    return pos, True
                if pattern[pos - k] != pattern[pos + k + 1]:
                    break

    return pos, False


def check_equal_columns(pattern):
    pattern = transpose(pattern)

    return check_equal_lines(pattern)


result = 0
for pattern in data:
    pos_columns, equal_columns = check_equal_columns(pattern)
    pos_lines, equal_lines = check_equal_lines(pattern)
    if equal_lines and pos_lines is not None:
        result += (pos_lines + 1) * 100
    if equal_columns and pos_columns is not None:
        result += pos_columns + 1

print('day 13 part 1:', result)
print(f'time elapsed: {(time() - time_start)}')