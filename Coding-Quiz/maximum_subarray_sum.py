from typing import List
import sys

def print_duration(func):
    import time
    def _wrapper(*argv, **kwargv):
        start = time.time()
        result = func(*argv, **kwargv)
        print(f'duration={time.time() - start}')
        return result
    return _wrapper

@print_duration
def get_max_sequence_sum(numbers: List[int]) -> int:
    max_num = -1 * sys.maxsize

    for i in range(len(numbers)):
        sum_num = numbers[i]
        max_num = max(sum_num, max_num)
        
        for j in range(i+1, len(numbers)):
            sum_num += numbers[j]
            max_num = max(sum_num, max_num)
    
    return max_num

@print_duration
def get_max_sequence_sum_by_sakai(numbers: List[int]) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        sum_sequence = max(num, sum_sequence + num)
        result_sequence = max(result_sequence, sum_sequence)
        
    return result_sequence

@print_duration
def find_max_circular_sequence_sum(numbers: List[int]) -> int:
    result_sequence, sum_sequence, start_index = 0, 0, 0
    while start_index < len(numbers):
        i = start_index + 1
        if i >= len(numbers):
            i = 0
        sum_sequence = numbers[start_index]
        while i != start_index:
            sum_sequence = max(sum_sequence + numbers[i], numbers[i])
            result_sequence = max(result_sequence, sum_sequence)
            i += 1
            if i >= len(numbers):
                i = 0
        start_index += 1
    return result_sequence


@print_duration
def get_max_min_sequence_sum_by_sakai(numbers: List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        sum_sequence = operator(num, sum_sequence + num)
        result_sequence = operator(result_sequence, sum_sequence)
        
    return result_sequence


@print_duration
def find_max_circular_sequence_sum_by_sakai(numbers: List[int]) -> int:
    # 周りこまないとけないパターン
    # ex) [-500, 1, -2, 3, 6, -1, 2, 4, -5, 2, -500]
    max_sequence_sum = get_max_min_sequence_sum_by_sakai(numbers)
    max_wrap_sequence_sum = sum(numbers) - get_max_min_sequence_sum_by_sakai(numbers, operator=min)
    return max(max_sequence_sum, max_wrap_sequence_sum)



if __name__ == '__main__':
    numbers = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    print(get_max_sequence_sum(numbers))
    print(get_max_sequence_sum_by_sakai(numbers))
    print(find_max_circular_sequence_sum(numbers))
    print(find_max_circular_sequence_sum_by_sakai(numbers))
