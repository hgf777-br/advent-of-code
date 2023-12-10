import re
import time

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

replacements = replacements.splitlines()
replacements = [line.split() for line in replacements]
r = {}
for k,_,v in replacements:
    if k not in r:
        r[k] = [v]
    else:
        r[k].append(v)
print(r)

initial = 'e'

total = []

def solve(mol, count):
    total.append(count)
    for k in r:
        for c in re.finditer(f'{k}', mol):
            for i in r[k]:
                s,e = c.span()
                f = mol[:s] + i + mol[e:]
                print(f, len(f))
                if f == molecule:
                    print(f, count)
                    return(count)
                if len(f) >= len(molecule) or f not in molecule:
                    return(-1)
                solve(f,count+1)
    return count


print(solve(initial,1))
print(len(total))
final = time.time()
print(final-inicio)