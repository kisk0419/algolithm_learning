# from itertools import permutations

# for r in permutations([1, 2, 3, 4]):
#     print(r)

from typing import List, Iterator


def all_perms(elements: List[int]) -> List[List[int]]:
    results = []
    def _all_perms(perm: List[int]):
        if len(elements) == len(perm):
            results.append(perm)
            return
        for elem in elements:
            if elem not in perm:
                _all_perms(perm[:] + [elem])
    for e in elements:
        _all_perms([e])
    return results


def all_perms_by_sakai(elements: List[int]) -> Iterator[List[int]]:
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms_by_sakai(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
    

if __name__ == '__main__':
    elems = [1, 2, 3]
    for r in all_perms_by_sakai(elems):
        print(r)
    
