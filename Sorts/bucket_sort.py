from typing import List


def bucket_sort(numbers: List[int]) -> List[int]:
    bucket = [[] for _ in range(10)]
    for num in numbers:
        idx = int(num/10)
        if idx >= 10:
            idx = 9
        bucket[idx].append(num)
    
    result = []
    for b in bucket:
        if len(b) > 0:
            result.extend(insertion_sort(b))
    
    return result
    

def bucket_sort_new(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    bucket = [[] for _ in range(size)]
    for num in numbers:
        idx = num // size
        if idx >= size:
            bucket[-1].append(num)
        else:
            bucket[idx].append(num)

    result = []
    for b in bucket:
        result += insertion_sort(b)
    
    return result


def bucket_sort_by_sakai(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    bucket = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            bucket[i].append(num)
        else:
            bucket[size-1].append(num)
    
    for i in range(size):
        insertion_sort(bucket[i])
    
    result = []
    for i in range(size):
        result += bucket[i]
    
    return result


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp < numbers[j]:
            numbers[j+1] = numbers[j]
            j = j - 1
        numbers[j+1] = temp
    
    return numbers


if __name__ == '__main__':
    import random
    #num = [1, 5, 28, 25, 100, 52, 27, 91, 22, 99]
    num = [random.randint(0, 1000) for _ in range(10)]
    print(bucket_sort_new(num))