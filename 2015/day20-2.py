from itertools import compress


def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primeslist:
        if p*p > n:
            break
        count = 0
        while not n % p:
            n //= p
            count += 1
        if count > 0:
            pf.append((p, count))
    if n > 1:
        pf.append((n, 1))
    return pf


def divisors_2(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1, e+1) for x in divs]
    return divs


def divisors(n):
    r = set()
    if n != 1:
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                r.add(i)
                r.add(n//i)
    else:
        r.add(1)
    return r


f = 29000000
primeslist = primes(int(f**0.5)+1)
# print(list(divisors_2(f)))
# for i in range(1000000,1000001):
#     l = list(divisors_2(i))
#     print(i,(sum(l))*10)

# exit()
m = 1
small = 0
big = 0
houses = [0 for _ in range(3000000)]
for n in range(m, m+3000000):
    div = [d if houses[d] < 50 else 0 for d in divisors_2(n)]
    for d in div:
        houses[d] += 1
    s = (sum(div))*11
    if s > f:
        print('found:', n, s)
        break
    if s > f:
        small += 1
    else:
        big += 1

print('big:', big)
print('small:', small)
