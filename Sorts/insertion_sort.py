from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    
    for i in range(1, len_numbers):
        if numbers[i-1] > numbers[i]:
            numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
            
            for j in range(i-1, 0, -1):
                if numbers[j] < numbers[j-1]:
                    numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
                    
                else:
                    break
      
    return numbers


def insertion_sort_by_sakai(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        
        numbers[j+1] = temp
    
    return numbers


if __name__ == '__main__':
    #nums = [2, 5, 1, 8, 4]
    import random
    nums = [random.randint(1, 1000) for _ in range(10)]
    #print(nums)
    print(insertion_sort_by_sakai(nums))