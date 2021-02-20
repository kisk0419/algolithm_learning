import math
import time
import random

def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    else:
        return True

def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(6, math.floor(math.sqrt(num)) + 1, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    return True


def is_prime_by_sakai_v1(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_by_sakai_v2(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_prime_by_sakai_v2_no_math(num: int) -> bool:
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def is_prime_by_sakai_v3(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def is_prime_by_sakai_v4(num: int) -> bool:
    # 6k ± 1 < √n
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, math.floor(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num & (i+2) == 0:
            return False
    return True

if __name__ == '__main__':
    numbers = [random.randint(0, 1000) for _ in range(100000)]
    start = time.time()
    for num in numbers:
        is_prime_by_sakai_v1(num)
    print(f'is_prime_by_sakai_v1={time.time() - start}')

    start = time.time()
    for num in numbers:
        is_prime_by_sakai_v2(num)
    print(f'is_prime_by_sakai_v2={time.time() - start}')

    start = time.time()
    for num in numbers:
        is_prime_by_sakai_v3(num)
    print(f'is_prime_by_sakai_v3={time.time() - start}')

    start = time.time()
    for num in numbers:
        is_prime_by_sakai_v4(num)
    print(f'is_prime_by_sakai_v4={time.time() - start}')

    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print(f'is_prime_v1={time.time() - start}')

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print(f'is_prime_v2={time.time() - start}')

    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print(f'is_prime_v3={time.time() - start}')