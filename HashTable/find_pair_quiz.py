"""
1. Input: [11, 2, 5, 9, 10, 3], 12 => Output: (2, 10) or None
2. Input: [11, 2, 5, 9, 10, 3] => Output: (11, 9) or None ex) 11 + 9 = 2 + 5 + 10 + 3
"""

from typing import List, Tuple, Optional
from hashtable import HashTable


def search_pair_1(numbers: List[int], sum_num: int) -> Optional[Tuple[int, int]]:
    hash_table = HashTable()
    
    for num in numbers:
        key = sum_num - num
        try:
            hash_table[str(key)]
            return (num, key)
        except:
            hash_table[str(num)] = True

    return None


def search_pair_2(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_num = sum(numbers)
    if sum_num % 2:
        return 'None'
    
    hash_table = HashTable()
    even_num = sum_num // 2
    for num in numbers:
        key = even_num - num
        try:
            hash_table[str(key)]
            return (num, key)
        except:
            hash_table[str(num)] = True
    return None


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return num, val
        cache.add(num)
    return None


def get_pair_half_num(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_number = sum(numbers)
    half_number, remains = divmod(sum_number, 2)
    if remains % 2:
        return None
    
    cache = set()
    for num in numbers:
        val = half_number - num
        if val in cache:
            return val, num
        cache.add(num)
    return None


if __name__ == '__main__':
    print(search_pair_1([11, 2, 5, 9, 10, 3], 12))
    print(search_pair_2([11, 2, 5, 9, 10, 3]))

    print(get_pair([11, 2, 5, 9, 10, 3], 12))
    print(get_pair_half_num([11, 2, 5, 9, 10, 3]))