import timeit


# recursive solution
def fib1(n: int) -> int:
    if n <= 1:
        return n

    return fib1(n - 1) + fib1(n - 2)


# dynamic programming solution
def fib2(n: int) -> int:
    f = []
    f.append(1)
    f.append(1)
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]


def recursive_time():
    SETUP_CODE = 'from __main__ import fib1'

    TEST_CODE = '''
n = 25
fib1(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print('tempo programa recursivo:', min(times))


def dynamic_time():
    SETUP_CODE = 'from __main__ import fib2'

    TEST_CODE = '''
n = 25
fib2(n)
    '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100)

    print('tempo programa dinamico:', min(times))


if __name__ == '__main__':
    recursive_time()
    dynamic_time()
