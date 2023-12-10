from collections import Counter

data = '''43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38'''

# data = '''20
# 15
# 10
# 5
# 5
# '''

volume = 150

data = [int(x) for x in data.splitlines()]

dp = [1] + [0]*volume
dt = {d:[] for d in range(1,151)}
print(dt)
for d in data:
    for i in reversed(range(d,volume+1)):
        if i-d == 0:
            dt[i].append(1)
        elif dp[i-d] != 0:
            for x in dt[i-d]:
                dt[i].append(x+1)
        dp[i] += dp[i-d]

count = Counter(dt[volume])

count = sorted(count.most_common(), key=lambda x:x[0])

print(count[0])