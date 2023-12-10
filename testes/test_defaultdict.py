from collections import defaultdict

d = {}

for i in range(10):
    n = d.setdefault(i, 0)
    d[i] = n + 1

print(d)

dd = defaultdict(int)

for i in range(10):
    dd[i] += 1

print(dd)


