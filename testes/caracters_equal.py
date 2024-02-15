a = '##.#..##..'
b = '##.#..##.#'

sum_caracters = 0
for ci, cj in zip(a, b):
    if ci == cj:
        sum_caracters += 1

print(sum_caracters == len(a) - 1)
