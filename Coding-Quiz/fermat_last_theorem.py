from typing import List, Tuple
import sys
import time

def duration(func):
    def _wrapper(*args):
        start = time.time()
        result = func(*args)
        print(f'duration={time.time() - start}')
        return result
    return _wrapper

@duration
def fermat_last_theorem_v1(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
    result = []

    if squire_num < 2:
        return result

    for x in range(1, max_num):
        for y in range(x+1, max_num+1):
            z = x**squire_num + y**squire_num
            z = pow(z, 1.0 / squire_num) 
            if z == int(z):
                result.append((x, y, int(z)))
    return result

@duration
def fermat_last_theorem_v2(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
    result = []

    if squire_num < 2:
        return result

    for x in range(1, max_num):
        for y in range(x+1, max_num+1):
            pow_sum = pow(x, squire_num) + pow(y, squire_num)
            z = pow(pow_sum, 1.0 / squire_num) 
            if not z.is_integer():
                continue
            z = int(z)
            pow_z = pow(z, squire_num)
            if pow_z == pow_sum:
                result.append((x, y, z))
    return result

@duration
def fermat_last_theorem_by_sakai_v1(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
    result = []

    if squire_num < 2:
        return result

    max_z = int(pow((max_num - 1)**squire_num + max_num ** squire_num, 1.0 / squire_num))

    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            for z in range(y + 1, max_z):
                if x ** squire_num + y ** squire_num == z ** squire_num:
                    result.append((x, y, z))
    return result

@duration
def fermat_last_theorem_by_sakai_v2(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
    result = []

    if squire_num < 2:
        return result
    
    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            pow_sum = pow(x, squire_num) + pow(y, squire_num)
            
            if pow_sum > sys.maxsize:
                raise ValueError(x, y, z, squire_num, pow_sum)

            z = pow(pow_sum, 1.0 / squire_num)
            if not z.is_integer():
                continue
            z = int(z)
            pow_z = pow(z, squire_num)
            if pow_sum == pow_z:
                result.append((x, y, z))
    return result


if __name__ == '__main__':
    print(fermat_last_theorem_v1(20, 2))
    print(fermat_last_theorem_v2(20, 2))
    print(fermat_last_theorem_by_sakai_v1(20, 2))
    print(fermat_last_theorem_by_sakai_v2(20, 2))

