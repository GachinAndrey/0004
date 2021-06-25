import timeit
from random import random



def myArr():
    n = 10
    arr = []
    for i in range(n):
        arr.append(int(random() * 100))

    index_min = arr.index(min(arr))
    index_max = arr.index(max(arr))
    min_my = min(arr)
    max_my = max(arr)

    arr[index_min] = max_my
    arr[index_max] = min_my
    return arr


def myArr2():
    n = 10
    arr = []
    for i in range(n):
        arr.append(int(random() * 100))
    arr.sort()

    min_my = arr[0]
    max_my = arr[-1]

    arr[0] = max_my
    arr[-1] = min_my
    return arr


print(timeit.timeit(myArr))
print(timeit.timeit(myArr2))
