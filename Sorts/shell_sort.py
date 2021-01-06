from typing import List


def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2

    while gap >= 1:
        for i in range(0, len_numbers - gap):
            temp = numbers[i+gap]
            if numbers[i] > temp:
                numbers[i+gap] = numbers[i]
                j = i - gap
                while j >= 0:
                    if numbers[j] > temp:
                        numbers[j+gap] = numbers[j]
                        j = j - gap
                    else:
                        break
                numbers[j+gap] = temp

        gap = gap // 2

    return numbers


def shell_sort_new(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2

    while gap > 0:
        for i in range(0, len_numbers - gap):
            temp = numbers[i+gap]
            if numbers[i] > temp:
                j = i
                while j >= 0 and numbers[j] > temp:
                    numbers[j+gap] = numbers[j]
                    j -= gap
                
                numbers[j+gap] = temp

        gap //= 2

    return numbers


def shell_sort_by_sakai(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2

    while gap > 0:
        for i in range(gap, len_numbers):
            temp = numbers[i]
            if numbers[i-gap] > temp:
                j = i
                while j >= gap and numbers[j-gap] > temp:
                    numbers[j] = numbers[j-gap]
                    j -= gap

                numbers[j] = temp

        gap //= 2

    return numbers


if __name__ == '__main__':
    import random
    nums = [5, 6, 9, 2, 3]
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(shell_sort_new(nums))