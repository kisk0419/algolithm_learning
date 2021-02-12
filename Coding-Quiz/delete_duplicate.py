from typing import List


def delete_duplicate_v1(numbers: List[int]) -> None:
    i = 0
    j = 1
    while j < len(numbers):
        if numbers[i] != numbers[j]:
            numbers[i+1] = numbers[j]
            i += 1
        j += 1
    numbers[:] = numbers[:i+1]

def delete_duplicate_v1_by_sakai(numbers: List[int]) -> None:
    tmp = []
    for n in numbers:
        if n not in tmp:
            tmp.append(n)
    numbers[:] = tmp


def delete_duplicate_v2_by_sakai(numbers: List[int]) -> None:
    tmp = [numbers[0]]
    i, len_num = 0, len(numbers) - 1
    while i < len_num:
        if numbers[i] != numbers[i+1]:
            tmp.append(numbers[i+1])
        i += 1

    numbers[:] = tmp

def delete_duplicate_v3_by_sakai(numbers: List[int]) -> None:
    i = 0
    while i < len(numbers) - 1:
        if numbers[i] == numbers[i+1]:
            numbers.remove(numbers[i])
            i -= 1
        i += 1
    
def delete_duplicate_v4_by_sakai(numbers: List[int]) -> None:
    i = len(numbers) - 1
    while 0 < i:
        if numbers[i-1] == numbers[i]:
            numbers.pop(i)
        i -= 1

if __name__ == '__main__':
    numbers = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    print(list(set(numbers)))
    print(list(dict.fromkeys(numbers)))
    print([n for i, n in enumerate(numbers) if n not in numbers[:i]])
    delete_duplicate_v4_by_sakai(numbers)
    print(numbers)