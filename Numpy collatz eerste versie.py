import numpy as np
from time import perf_counter
from numba import njit


max=1000000

arr = np.arange(1, max+1)
arr=arr.astype(np.int64)
ones=np.ones(max)


@njit(parallel=True)
def Collatz_algorithm(arr):
    arr = np.arange(1, max+1)
    while (np.array_equal(arr,ones)==False):

          arr = np.where((arr != 1) & (arr % 2 == 0), arr // 2, arr)
          arr = np.where((arr != 1) & (arr % 2 != 0), arr * 3 + 1, arr)

    return arr

if __name__== '__main__':
    start = perf_counter()
    print(Collatz_algorithm(arr))   #Should return an array filled entirely with 1's.
    stop = perf_counter()
    print("Collatz conjecture executed in ", stop - start, " seconds for ", max, ' iterations.')
    start2 = perf_counter()
    print(Collatz_algorithm(arr))  # Should return an array filled entirely with 1's.
    stop2 = perf_counter()
    print("Collatz conjecture executed in ",stop2 - start2," seconds for ",max,' iterations.')


