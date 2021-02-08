from typing import List

def print_duration(func) -> int:
    import time
    def _wrapper(*argv):
        start = time.time()
        ret = func(*argv)
        print(f'duration={time.time() - start}')
        return ret
    return _wrapper


def list_to_int(number: List[int]) -> int:
    sum_number = 0
    for i, num in enumerate(reversed(number)):
        sum_number += (num * 10**i)
    return sum_number


@print_duration
def list_to_int_plus_one(number: List[int]) -> int:
    i = len(number) - 1
    while i >= 0:
        last_num = number[i]
        if last_num + 1 < 10:
            number[i] += 1
            break
        number[i] = 0
        i -= 1
    else:
        number.insert(0, 1)

    while len(number) > 0 and number[0] == 0:
        number.pop(0)

    return list_to_int(number)

def remove_zero(numbers: List[int]) -> None:
    while numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)

@print_duration
def list_to_int_plus_one_by_sakai(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] < 10:
            remove_zero(numbers)
            break
        numbers[i] = 0
        numbers[i-1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)


if __name__ == '__main__':
    numbers = [
        [1],
        [2, 3],
        [8, 9],
        [9, 9],
        [1, 2, 3],
        [7, 8, 9],
        [9, 9, 9],
        [9, 9, 9, 9],
        [0, 0, 0, 9, 9, 9, 9]
    ]

    for number in numbers:
        print(list_to_int_plus_one_by_sakai(number))
        #print(list_to_int_plus_one(number))

    
