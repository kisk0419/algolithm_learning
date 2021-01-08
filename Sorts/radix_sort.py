from typing import List


def get_radix_numbers(numbers: List[int], shift) -> List[int]:
    result = [0] * len(numbers)
    for i, num in enumerate(numbers):
        r = num
        for _ in range(shift-1):
            r //= 10
        result[i] = r % 10
    
    print('raidx', result)
    return result


def counting_sort(numbers: List[int], shift=1) -> List[int]:
    radix_numbers = get_radix_numbers(numbers, shift)
    max_num = 9
    counts = [0] * (max_num + 1)
    result = [0] * len(radix_numbers)

    for num in radix_numbers:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    
    for i in range(len(radix_numbers)-1, -1, -1):
        index = radix_numbers[i]
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
    
    return result


def radix_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    digit_num = 0
    while max_num > 0:
        max_num //= 10
        digit_num += 1
    
    for i in range(digit_num):
        numbers = counting_sort(numbers, i+1)
    
    return numbers


def counting_sort_by_sakai(numbers: List[int], place: int) -> List[int]:
    counts = [0] * 10
    result = [0] * len(numbers)

    for num in numbers:
        index = (num // place) % 10
        counts[index] += 1

    for i in range(1, 10):
        counts[i] += counts[i-1]
    
    for i in range(len(numbers)-1, -1, -1):
        index = (numbers[i] // place) % 10
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
    
    return result


def radix_sort_by_sakai(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    place = 1
    
    while max_num > place:
        numbers = counting_sort_by_sakai(numbers, place)
        place *= 10
    
    return numbers


if __name__ == '__main__':
    nums = [24, 10, 11, 324, 201, 101, 55]
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(radix_sort_by_sakai(nums))