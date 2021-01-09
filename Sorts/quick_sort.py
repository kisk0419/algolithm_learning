from typing import List


def quick_sort(numbers: List[int], start_index: int, end_index: int) -> List[int]:
    if start_index >= end_index:
        return numbers

    pivot = numbers[end_index]
    i = start_index - 1
    for j in range(start_index, end_index):
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i+1], numbers[end_index] = numbers[end_index], numbers[i+1]

    numbers = quick_sort(numbers, start_index, i)
    numbers = quick_sort(numbers, i+1, end_index)

    return numbers


def quick_sort_retry(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], start_index: int, end_index: int) -> List[int]:
        if start_index >= end_index:
            return numbers

        pivot = numbers[end_index]
        i = start_index - 1
        for j in range(start_index, end_index):
            if numbers[j] < pivot:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]

        numbers[i+1], numbers[end_index] = numbers[end_index], numbers[i+1]

        numbers = _quick_sort(numbers, start_index, i)
        numbers = _quick_sort(numbers, i+1, end_index)

        return numbers

    numbers = _quick_sort(numbers, 0, len(numbers)-1)

    return numbers


def partition(numbers: List[int], low: int, high: int) -> int:
    pivot = numbers[high]
    i = low - 1
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1
    

def quick_sort_by_sakai(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    #print(quick_sort(nums, 0, len(nums)-1))
    print(quick_sort_retry(nums))
