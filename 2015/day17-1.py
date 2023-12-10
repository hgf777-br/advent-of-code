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

data = [int(x) for x in data.splitlines()]

data.sort()

dp = [1] + [0]*150

for d in data:
    for i in reversed(range(d,151)):
        dp[i] += dp[i-d]

print(dp[150])