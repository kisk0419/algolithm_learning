from typing import List, Tuple, Iterator


def symmetric(paris: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for pair in paris:
        first, second = pair
        l = cache.get(second, [])
        if first in l:
            yield pair
        else:
            l.append(second)
        cache[first] = l
    

def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for pair in pairs:
        first, second = pair
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif first == value:
            yield pair


if __name__ == '__main__':
    pairs = [(1, 2), (4, 2), (3, 6), (6, 3), (3, 5), (2, 6), (4, 7), (5, 3), (7, 4)]
    #pairs = [(1, 2), (3, 1), (1, 3), (2, 1)]
    for pair in symmetric(pairs):
        print(pair)

    print('#####')
    #pairs = [(1, 2), (4, 2), (3, 6), (6, 3), (3, 5), (2, 6), (4, 7), (5, 3), (7, 4)]
    #pairs = [(1, 2), (3, 1), (1, 3), (2, 1)]
    for pair in find_pair(pairs):
        print(pair)

