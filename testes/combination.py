import itertools
import re
import time

stert = time.time()

record = '???.###'
record = '.??.??.?##.'
record = '?###????????'
record = '#??.#??.??#?#????#?#'
groups = [1, 1, 3]
groups = [3, 2, 1]
groups = [2, 1, 6, 3]

p_list = ['#'*q for q in groups] + ['.']*(len(record)-sum(groups))
print(p_list)
print(time.time() - stert)

p = [''.join(line) for line in itertools.permutations(p_list)]

# p = [''.join(line) for line in p]

re_record = record.replace('.', r'\.').replace('?', '[#.]')
print(re_record)
print(time.time() - stert)

p = [line for line in p if re.match(re_record, line)]
print('fim do match')
print(time.time() - stert)

p = list(set(p))
print('fim do set')
print(time.time() - stert)

# p = [line for line in p if not len(re.findall(r'(#+)', line)) != len(groups)]

p = [line for line in p if [len(i) for i in re.findall(r'(#+)', line)] == groups]


print(len(p))
print(time.time() - stert)
