import re
from collections import defaultdict

data = '''Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'''

sym_to_fruit = defaultdict(list("🍅🍇🍈🍉🍊🍋🍌🍍🍎🍐🍑🍒🍓🥑🥝🥭").pop)
raw_fruit = re.sub(r"[A-Z][a-z]*", lambda m: sym_to_fruit[m[0]], data)
print(sym_to_fruit)

print(raw_fruit)

productions, FRUITS = raw_fruit.split("\n\n")

PRODUCE = defaultdict(list)
for a, b in re.findall(r"(.) => (.*)", productions):
    PRODUCE[a].append(b)

print(PRODUCE)


def part_one():
    return len({
        FRUITS[:i] + produce + FRUITS[i + 1:]
        for i, fruit in enumerate(FRUITS)
        for produce in PRODUCE[fruit]
    })


def part_two():
    return len(FRUITS) - 2 * FRUITS.count("🍒") - 2 * FRUITS.count("🍋") - 1


print('part one:', part_one())
print('part two:', part_two())
