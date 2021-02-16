from typing import List


def order_even_first_odd_last(numbers: List[int]) -> None:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        if numbers[i] % 2:
            for j in range(i+1, len_numbers):
                if numbers[j] % 2 == 0:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    break
   

def order_even_first_odd_last_v2(numbers: List[int]) -> None:
    len_numbers = len(numbers)
    insert_index = len_numbers
    i = len_numbers - 1
    while 0 <= i:
        if numbers[i] % 2:
            numbers.insert(insert_index, numbers[i])
            numbers.pop(i)
            insert_index -= 1
        i -= 1


def order_even_first_odd_last_by_sakai(numbers: List[int]) -> None:
    i, j = 0, len(numbers)-1

    while i < j:
        if numbers[i] % 2:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1
        else:
            i += 1

if __name__ == '__main__':
    numbers = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    order_even_first_odd_last_by_sakai(numbers)
    print(numbers)