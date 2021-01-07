from typing import List


def counting_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    max_num = max(numbers)
    
    counts = [0 for _ in range(max_num+1)]
    for num in numbers:
        counts[num] += 1
    
    sums = [0 for _ in range(max_num+1)]
    for i in range(1, len(counts)):
        sums[i] = sums[i-1] + counts[i]

    results = [None for _ in range(len_numbers)]
    for num in numbers:
        index = sums[num] - 1
        results[index] = num
        sums[num] -= 1
    
    return results


def counting_sort_retry(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    counts = [0 for _ in range(max_num+1)]
    results = [0 for _ in range(len(numbers))]

    for num in numbers:
        counts[num] += 1
    
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(numbers)-1, -1, -1):
        index = numbers[i]
        results[counts[index]-1] = numbers[i]
        counts[index] -= 1
    
    return results


def counting_sort_by_sakai(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1
    
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    
    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1
    
    return result


if __name__ == '__main__':
    import random
    nums = [4, 3, 6, 2, 3, 4, 7]
    nums = [random.randint(0, 1000) for _ in range(10)]
    #print(counting_sort(nums))
    print(counting_sort_retry(nums))
