import timeit
from functools import cache


# recursive solution
def fib1(n: int) -> int:
    if n <= 1:
        return n

    return fib1(n - 1) + fib1(n - 2)


# dynamic programming solution
def fib2(n: int) -> int:
    f = []
    f.append(0)
    f.append(1)
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]


# recursive solution with memoization
@cache
def fib3(n: int) -> int:
    if n <= 1:
        return n

    return fib1(n - 1) + fib1(n - 2)


# recursive solution with memoization
def fib4(n: int, r={0: 0, 1: 1}) -> int:
    if n in r:
        return r[n]
    else:
        r[n] = fib4(n - 1, r) + fib4(n - 2, r)
        return r[n]


def recursive_time():
    SETUP_CODE = 'from __main__ import fib1'

    TEST_CODE = '''
n = 30
fib1(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print(f'tempo programa recursivo: {min(times):.10f}')


def dynamic_time():
    SETUP_CODE = 'from __main__ import fib2'

    TEST_CODE = '''
n = 100
fib2(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print(f'tempo programa dinamico: {min(times):.10f}')


def memoization_time():
    SETUP_CODE = 'from __main__ import fib3'

    TEST_CODE = '''
n = 30
fib3(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print(f'tempo programa recursivo com memorização: {min(times):.10f}')


def memoization_dict_time():
    SETUP_CODE = 'from __main__ import fib4'

    TEST_CODE = '''
n = 100
fib4(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print(f'tempo programa recursivo com memorização: {min(times):.10f}')


if __name__ == '__main__':
    # recursive_time()
    # dynamic_time()
    # memoization_time()
    # memoization_dict_time()
    print(fib2(500))
    print(fib4(500))
