import array
from timeit import timeit
import numpy as np


def get_range(num_bytes, signed=True):
    num_bits = num_bytes * 8
    if signed:
        return -2 ** (num_bits - 1), 2 ** (num_bits - 1) - 1
    else:
        return 0, (2 ** num_bits) - 1


typecodes = array.typecodes

for type in typecodes:
    print(type, array.array(type).itemsize, get_range(array.array(type).itemsize, signed=type.islower()))

large_list = list(range(10**6))
large_array = array.array("I", large_list)
large_ndarray = np.array(large_list, dtype=np.int32)

print(timeit(lambda: sum(large_list), number=100))
print(timeit(lambda: sum(large_array), number=100))
print(timeit(lambda: np.sum(large_ndarray), number=100))
