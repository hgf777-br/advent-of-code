data = 'cqjxjnds'
# data = 'ghijklmn'
data = 'cqjyxyzz'

data_num = [ord(c) for c in data]

def inc_letter(n):
    t = n+1 if n+1 < 122 else 97
    return (t == 97, t)

for i,n in enumerate(data_num[:3]):
    if n in [105,108,111]:
        data_num[i] = data_num[i] + 1
        for j in range(i+1,8):
            data_num[j] = 97

for i in range(7,2,-1):
    r, data_num[i] = inc_letter(data_num[i])
if data_num[3] >= 121
if data_num[3] != data_num[4]:
    data_num[4] = data_num[3]
    for i in range(5,8):
        data_num[i] = 97

data_num[5] = inc_letter(data_num[4])
data_num[6] = data_num[7] = inc_letter(data_num[5])

response = ''.join([chr(n) for n in data_num])
print(response)
