import itertools
import math
import numpy as np

print(math.gcd(*[5, 9]))

exit()
a = np.array([[1, 2], [3, 4]])
print(a)

b = a

print(b)

b[0, 0] = 9

print(a)

names = ['luisa', 'bruna', 'katia', 'hgf', 'julia', 'heitor', 'marcia', 'mauricio']

permutations = list(itertools.permutations(names))

print(len(permutations))

print(f'fatorial: {math.factorial(len(names))}')

grupo = 'AAAABBBCCDAABBB'

groups = []
uniquekeys = []
for k, g in itertools.groupby(grupo):
    groups.append(list(g))  # Store group iterator as a list
    uniquekeys.append(k)

print(uniquekeys)
print(groups)

c = [(x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]
c = [i for i in c if sum(i) == 5]
print(c)
