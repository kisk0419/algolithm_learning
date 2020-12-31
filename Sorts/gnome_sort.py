from typing import List


def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    i = 0
    while i < len_numbers-1:
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1

    return numbers


def gnome_sort_by_sakai(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0

    while index < len_numbers:
        if index == 0:
            index += 1
        if numbers[index] >= numbers[index-1]:
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1

    return numbers


if __name__ == '__main__':
    #nums = [7, 5, 3, 1, 2, 8]
    import random
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(gnome_sort_by_sakai(nums))
    