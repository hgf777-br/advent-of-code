import timeit
from functools import cache


# recursive solution
def fat1(n: int) -> int:
    if n == 0:
        return 1

    return n * fat1(n - 1)


# dynamic programming solution
def fat2(n: int) -> int:
    f = []
    f.append(1)
    for i in range(1, n+1):
        f.append(f[i - 1]*i)

    return f[n]


# recursive solution
@ cache
def fat3(n: int) -> int:
    if n == 0:
        return 1

    return n * fat3(n - 1)


def recursive_time():
    SETUP_CODE = 'from __main__ import fat1'

    TEST_CODE = '''
n = 400
fat1(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print(f'tempo programa recursivo: {min(times):.10f}')


def dynamic_time():
    SETUP_CODE = 'from __main__ import fat2'

    TEST_CODE = '''
n = 400
fat2(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print(f'tempo programa dinamico: {min(times):.10f}')


def memoization_time():
    SETUP_CODE = 'from __main__ import fat3'

    TEST_CODE = '''
n = 400
fat3(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print(f'tempo programa recursivo com memorização: {min(times):.10f}')


if __name__ == '__main__':
    print('1:', fat1(6))
    print('2:', fat2(6))
    print('3:', fat3(6))
    recursive_time()
    dynamic_time()
    memoization_time()
