import math


data = '''Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70'''

data = data.split('\n')

cities_data = []
cities_names = set()
final_total = math.inf

for d in data:
    d = d.split()
    cities_data.append(((d[0], d[2]), int(d[4])))
    cities_names.add(d[0])
    cities_names.add(d[2])
cities_data.sort(key=lambda x:x[1])

for city_name in cities_names:
    first_city = city_name
    next_city = None
    visited = []
    total = 0
    cities = cities_data.copy()

    for idx, city in enumerate(cities):
        if city[0][0] == first_city or city[0][1] == first_city:
            # print(city)
            total += city[1]
            next_city = city[0][1]
            visited.append(city[0][0])
            cities.pop(idx)
            break
    continua = True
    while continua:
        continua = False
        for idx, city in enumerate(cities):
            if city[0][0] == next_city and city[0][1] not in visited:
                # print(city)
                total += city[1]
                next_city = city[0][1]
                visited.append(city[0][0])
                cities.pop(idx)
                continua = True
                break
            elif city[0][1] == next_city and city[0][0] not in visited:
                # print(city)
                total += city[1]
                next_city = city[0][0]
                visited.append(city[0][1])
                cities.pop(idx)
                continua = True
                break

    final_total = total if total < final_total else final_total
    print(first_city, total)

print('Result:', final_total)

