import cProfile


def test(num, n=10000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')

    assert num < len(res)
    return res[num - 1]


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number


cProfile.run('eratosthenes_sieve(30000)')
cProfile.run('search_prime(30000)')
"""
cProfile.run('eratosthenes_sieve(1000)')
cProfile.run('search_prime(1000)')

4289 function calls in 0.022 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.021    0.021    0.022    0.022 002.py:22(eratosthenes_sieve)
        1    0.000    0.000    0.000    0.000 002.py:27(<listcomp>)
        2    0.000    0.000    0.000    0.000 002.py:49(<listcomp>)
        2    0.000    0.000    0.000    0.000 002.py:52(<listcomp>)
        1    0.000    0.000    0.022    0.022 <string>:1(<module>)
        1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
     4278    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


         1003 function calls in 0.028 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.028    0.028    0.028    0.028 002.py:69(search_prime)
        1    0.000    0.000    0.028    0.028 <string>:1(<module>)
        1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


"""
cProfile.run('eratosthenes_sieve(10000)')
cProfile.run('search_prime(10000)')

 48786 function calls in 3.802 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.786    3.786    3.801    3.801 002.py:22(eratosthenes_sieve)
        1    0.003    0.003    0.003    0.003 002.py:27(<listcomp>)
        4    0.002    0.001    0.002    0.001 002.py:49(<listcomp>)
        4    0.006    0.001    0.006    0.001 002.py:52(<listcomp>)
        1    0.000    0.000    3.802    3.802 <string>:1(<module>)
        1    0.000    0.000    3.802    3.802 {built-in method builtins.exec}
    48769    0.005    0.000    0.005    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


         10003 function calls in 2.969 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.967    2.967    2.968    2.968 002.py:63(search_prime)
        1    0.000    0.000    2.969    2.969 <string>:1(<module>)
        1    0.000    0.000    2.969    2.969 {built-in method builtins.exec}
     9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""


"""
cProfile.run('eratosthenes_sieve(30000)')
cProfile.run('search_prime(30000)')

153381 function calls in 21.506 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   21.473   21.473   21.505   21.505 002.py:22(eratosthenes_sieve)
        1    0.006    0.006    0.006    0.006 002.py:27(<listcomp>)
        4    0.004    0.001    0.004    0.001 002.py:49(<listcomp>)
        4    0.012    0.003    0.012    0.003 002.py:52(<listcomp>)
        1    0.000    0.000   21.506   21.506 <string>:1(<module>)
        1    0.000    0.000   21.506   21.506 {built-in method builtins.exec}
   153364    0.011    0.000    0.011    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


         30003 function calls in 19.967 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   19.963   19.963   19.967   19.967 002.py:63(search_prime)
        1    0.000    0.000   19.967   19.967 <string>:1(<module>)
        1    0.000    0.000   19.967   19.967 {built-in method builtins.exec}
    29999    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""