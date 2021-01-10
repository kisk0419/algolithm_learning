from typing import List


def divide(numbers: List[int], start: int, end: int) -> List[int]:
    if start >= end:
        return numbers[start:end+1]
    
    mid = (start + end) // 2
    left_nums = divide(numbers, start, mid)
    right_nums = divide(numbers, mid+1, end)
    return merge(left_nums, right_nums)


def merge(left_nums: List[int], right_nums: List[int]) -> List[int]:
    left_len = len(left_nums)
    right_len = len(right_nums)
    total_len = (left_len + right_len)
    i = j = k = 0
    result = [0] * total_len
    while i < left_len and j < right_len:
        if left_nums[i] < right_nums[j]:
            result[k] = left_nums[i]
            i += 1
        else:
            result[k] = right_nums[j]
            j += 1
        k += 1

    if k < total_len and i < left_len:
        result[k:] = left_nums[i:]
    elif k < total_len and j < right_len:
        result[k:] = right_nums[j:]
    return result

def merge_sort(numbers: List[int]) -> List[int]:
    return divide(numbers, 0, len(numbers)-1)
    

def merge_sort_retry(numbers: List[int]) -> List[int]:
    def _merge(numbers: List[int], left: List[int], right: List[int]) -> List[int]:
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        if i < len(left):
            numbers[k:] = left[i:]
        elif j < len(right):
            numbers[k:] = right[j:]

        return numbers


    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    merge_sort_retry(left)
    merge_sort_retry(right)

    _merge(numbers, left, right)

    return numbers


def merge_sort_by_sakai(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort_by_sakai(left)
    merge_sort_by_sakai(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers

if __name__ == '__main__':
    nums = [5, 4, 1, 8, 7, 3, 2, 9]
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(merge_sort_by_sakai(nums))
    print(merge_sort(nums))
    print(merge_sort_retry(nums))
