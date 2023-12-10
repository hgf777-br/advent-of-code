import re

data = '''Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8'''

# data = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''

pattern = re.compile(r'(\w+):[,\s\w]+(-?\d+)[,\s\w]+(-?\d+)[,\s\w]+(-?\d+)[,\s\w]+(-?\d+)[,\s\w]+(-?\d+)')
data = data.splitlines()
data = [list(pattern.match(data).groups()) for data in data] #type: ignore

fatores = [(x,y,w,z) for x in range(1,100) for y in range(1,100)for w in range(1,100) for z in range(1,100)]
# fatores = [(x,y) for x in range(1,100) for y in range(1,100)]
fatores = [i for i in fatores if sum(i) == 100]
# for f in fatores:
#     print(f)

for line in data:
    print(line)

resposta = 0
for fator in fatores:
    cap = dur = fla = tex = cal = 0
    for i, line in enumerate(data):
        cap += fator[i]*int(line[1])
        dur += fator[i]*int(line[2])
        fla += fator[i]*int(line[3])
        tex += fator[i]*int(line[4])
    cap = cap if cap > 0 else 0
    dur = dur if dur > 0 else 0
    fla = fla if fla > 0 else 0
    tex = tex if tex > 0 else 0
    # print(fator, cap, dur, fla, tex, cal)
    valor = cap*dur*fla*tex
    if valor > resposta:
        resposta = valor

print(resposta)