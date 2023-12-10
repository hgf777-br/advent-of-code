data = '''Henrique would gain 0 happiness units by sitting next to Bob.
Henrique would gain 0 happiness units by sitting next to Carol.
Henrique would gain 0 happiness units by sitting next to David.
Henrique would gain 0 happiness units by sitting next to Eric.
Henrique would gain 0 happiness units by sitting next to Frank.
Henrique would gain 0 happiness units by sitting next to George.
Henrique would gain 0 happiness units by sitting next to Mallory.
Henrique would gain 0 happiness units by sitting next to Alice.
Alice would gain 0 happiness units by sitting next to Henrique.
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 81 happiness units by sitting next to Carol.
Alice would lose 42 happiness units by sitting next to David.
Alice would gain 89 happiness units by sitting next to Eric.
Alice would lose 89 happiness units by sitting next to Frank.
Alice would gain 97 happiness units by sitting next to George.
Alice would lose 94 happiness units by sitting next to Mallory.
Bob would gain 0 happiness units by sitting next to Henrique.
Bob would gain 3 happiness units by sitting next to Alice.
Bob would lose 70 happiness units by sitting next to Carol.
Bob would lose 31 happiness units by sitting next to David.
Bob would gain 72 happiness units by sitting next to Eric.
Bob would lose 25 happiness units by sitting next to Frank.
Bob would lose 95 happiness units by sitting next to George.
Bob would gain 11 happiness units by sitting next to Mallory.
Carol would gain 0 happiness units by sitting next to Henrique.
Carol would lose 83 happiness units by sitting next to Alice.
Carol would gain 8 happiness units by sitting next to Bob.
Carol would gain 35 happiness units by sitting next to David.
Carol would gain 10 happiness units by sitting next to Eric.
Carol would gain 61 happiness units by sitting next to Frank.
Carol would gain 10 happiness units by sitting next to George.
Carol would gain 29 happiness units by sitting next to Mallory.
David would gain 0 happiness units by sitting next to Henrique.
David would gain 67 happiness units by sitting next to Alice.
David would gain 25 happiness units by sitting next to Bob.
David would gain 48 happiness units by sitting next to Carol.
David would lose 65 happiness units by sitting next to Eric.
David would gain 8 happiness units by sitting next to Frank.
David would gain 84 happiness units by sitting next to George.
David would gain 9 happiness units by sitting next to Mallory.
Eric would gain 0 happiness units by sitting next to Henrique.
Eric would lose 51 happiness units by sitting next to Alice.
Eric would lose 39 happiness units by sitting next to Bob.
Eric would gain 84 happiness units by sitting next to Carol.
Eric would lose 98 happiness units by sitting next to David.
Eric would lose 20 happiness units by sitting next to Frank.
Eric would lose 6 happiness units by sitting next to George.
Eric would gain 60 happiness units by sitting next to Mallory.
Frank would gain 0 happiness units by sitting next to Henrique.
Frank would gain 51 happiness units by sitting next to Alice.
Frank would gain 79 happiness units by sitting next to Bob.
Frank would gain 88 happiness units by sitting next to Carol.
Frank would gain 33 happiness units by sitting next to David.
Frank would gain 43 happiness units by sitting next to Eric.
Frank would gain 77 happiness units by sitting next to George.
Frank would lose 3 happiness units by sitting next to Mallory.
George would gain 0 happiness units by sitting next to Henrique.
George would lose 14 happiness units by sitting next to Alice.
George would lose 12 happiness units by sitting next to Bob.
George would lose 52 happiness units by sitting next to Carol.
George would gain 14 happiness units by sitting next to David.
George would lose 62 happiness units by sitting next to Eric.
George would lose 18 happiness units by sitting next to Frank.
George would lose 17 happiness units by sitting next to Mallory.
Mallory would gain 0 happiness units by sitting next to Henrique.
Mallory would lose 36 happiness units by sitting next to Alice.
Mallory would gain 76 happiness units by sitting next to Bob.
Mallory would lose 34 happiness units by sitting next to Carol.
Mallory would gain 37 happiness units by sitting next to David.
Mallory would gain 40 happiness units by sitting next to Eric.
Mallory would gain 18 happiness units by sitting next to Frank.
Mallory would gain 7 happiness units by sitting next to George.'''


from itertools import permutations

data = data.splitlines()
data = [l.split() for l in data]
data = [(data[0], int(data[3]) if data[2] == 'gain' else -int(data[3]), data[10][:-1]) for data in data]

names = set(d[0] for d in data)

class Table:
    def __init__(self, persons):
        self.seats = []
        qtd_persons = len(persons)
        for i in range(qtd_persons):
            left = i-1 if i != 0 else qtd_persons-1
            right = i+1 if i != qtd_persons-1 else 0
            person = Person(persons[i], persons[left], persons[right])
            self.seats.append(person)

    def calculate(self, data):
        total = 0
        for d in data:
            for person in self.seats:
                if person.name == d[0]:
                    if person.left_name == d[2]:
                        person.left += d[1]
                        total += d[1]
                    elif person.right_name == d[2]:
                        person.right += d[1]
                        total += d[1]
                    break
        return total


class Person:
    def __init__(self, name, left_name=None, right_name=None) -> None:
        self.name = name
        self.left = 0
        self.right = 0
        self.left_name = left_name
        self.right_name = right_name

    def __eq__(self, Person):
        return self.name == Person.name

    def __str__(self):
        return self.name

final = 0
for idx, names in enumerate(permutations(names), 1):
    print('mesa: ', idx)
    table = Table(names)
    total = table.calculate(data)
    if final < total:
        final = total
    # for s in table.seats:
    #     print(s, s.left, s.right)
    print('Total da mesa:', total)
    print()

print('final: ', final)