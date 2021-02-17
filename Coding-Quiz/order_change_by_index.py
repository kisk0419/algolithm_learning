from typing import List

def order_change_by_index_v1(chars: List[str], indexes: List[int]) -> str:
    tmp = [None] * len(chars)
    for i, index in enumerate(indexes):
        tmp[index] = chars[i]
    
    return ''.join(tmp)


def order_change_by_index_v2(chars: List[str], indexes: List[int]) -> str:
    for i, index in enumerate(indexes):
        if i not in indexes[:i]:
            chars[i], chars[index] = chars[index], chars[i]
    return ''.join(chars)


def order_change_by_index_v2_by_sakai(chars: List[str], indexes: List[int]) -> str:
    len_indexes = len(indexes)
    i = 0
    while i < len_indexes:
        while i != indexes[i]:
            index = indexes[i]
            chars[i], chars[index] = chars[index], chars[i]
            indexes[i], indexes[index] = indexes[index], indexes[i]
        i += 1
    return ''.join(chars)


if __name__ == '__main__':
    w = ['h', 'y', 'n', 'p', 't', 'o']
    i = [3, 1, 5, 0, 2, 4]
    print(order_change_by_index_v2_by_sakai(w, i))
