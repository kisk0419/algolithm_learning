from typing import List, Generator
import time


def print_duration(func):
    def _wrapper(number: int) -> List[int]:
        start = time.time()
        result = func(number)
        print(f'duration={time.time() - start}')
        return result
    return _wrapper

@print_duration
def generate_primes_v1(number: int) -> List[int]:
    if number == 1:
        return []
    if number == 2:
        return [2]
    primes = [2]
    for i in range(3, number+1, 2):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            primes.append(i)
    return primes


def generate_primes_v2(number: int) -> Generator[int, None, None]:
    if number == 1:
        return []
    if number == 2:
        return [2]
    primes = [2]
    for i in range(3, number+1, 2):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            yield i
    

@print_duration
def generate_primes_by_sakai_v1(number: int) -> List[int]:
    primes = []
    for x in range(2, number+1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes

@print_duration
def generate_primes_by_sakai_v2(number: int) -> List[int]:
    primes = []
    cache = {}
    for x in range(2, number+1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        primes.append(x)
        for y in range(x*2, number+1, x):
            cache[y] = False
    return primes


def generate_primes_by_sakai_v3(number: int) -> Generator[int, None, None]:
    cache = {}
    for x in range(2, number+1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        for y in range(x*2, number+1, x):
            cache[y] = False

if __name__ == '__main__':
    print(generate_primes_v1(1000))
    print(generate_primes_by_sakai_v1(1000))
    print(generate_primes_by_sakai_v2(1000))

    start = time.time()
    for i in generate_primes_by_sakai_v3(10000):
        pass
    print(f'duration={time.time() - start}')

    start = time.time()
    for i in generate_primes_v2(10000):
        pass
    print(f'duration={time.time() - start}')
