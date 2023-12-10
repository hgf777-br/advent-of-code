import re

data = '3113322113'


for i in range(50):
    response = ''
    last = data[0]
    counter = 0
    for d in data:
        if d == last:
            counter += 1
        else:
            response += str(counter) + last
            counter = 1
            last = d
    response += str(counter) + last
    data = response
    print(i, len(response))
