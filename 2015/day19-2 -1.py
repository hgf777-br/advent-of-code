import re
import time
from collections import defaultdict
from re import search, finditer

inicio = time.time()

replacements = '''Al => ThF
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
e => OMg'''

molecule = '''ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'''

# replacements = '''e => H
# e => O
# H => HO
# H => OH
# O => HH'''

# molecule = 'HOHOHO'

elements_string = replacements
molecule_string = molecule

replacements = replacements.splitlines()
replacements = [line.split() for line in replacements]
# replacements.sort(key=lambda x: len(x[2]), reverse=True)
r = {}
for k,_,v in replacements:
    if k not in r:
        r[k] = [v]
    else:
        r[k].append(v)

print(r)


elements: dict[str, list[str]] = defaultdict(list)
for e in elements_string.splitlines():
    element, product_string = e.split(" => ")
    elements[element].append(product_string)

print(elements)


products = set()
molecule = defaultdict(int)
for m in finditer(r"[A-Z][a-z]?", molecule_string):
    element = m.group()
    for product_string in elements[element]:
        products.add(molecule_string[:m.start()] + product_string + molecule_string[m.end():])

print(f"p1: {len(products)}")

c = 0
possible = {molecule_string}
while molecule_string != "e":
    for element, replacements in elements.items():
        for replacement in replacements:
            while (m:=search(replacement, molecule_string)):
                molecule_string = molecule_string[:m.start()] + element + molecule_string[m.end():]
                c += 1

print(f"p2: {c}")
