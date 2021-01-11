from typing import List
from typing import NewType


IndexNum = NewType('IndexNum', int)


def binary_search(numbers: List[int], search_num: int) -> bool:
    def _binary_search(numbers: List[int], left: int, right: int) -> bool:
        if left > right:
            return False

        mid = (left + right) // 2
        if search_num < numbers[mid]:
            return _binary_search(numbers, left, mid-1)
        elif numbers[mid] < search_num:
            return _binary_search(numbers, mid+1, right)
        else:
            return True

    return _binary_search(numbers, 0, len(numbers)-1)


def binary_search_1_by_sakai(numbers: List[int], value: int) -> IndexNum:
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_2_by_sakai(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], value: int, 
        left: IndexNum, right: IndexNum) -> IndexNum:
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid+1, right)
        else:
            return _binary_search(numbers, value, left, mid-1)
        
    return _binary_search(numbers, value, 0, len(numbers)-1)


def binary_search_retry(numbers: List[int], search_num: int) -> bool:
    def _binary_search(numbers: List[int], search_num: int, 
        left: IndexNum, right: IndexNum) -> IndexNum:
        
        if left > right:
            return -1

        mid = (left + right) // 2
        if search_num < numbers[mid]:
            return _binary_search(numbers, search_num, left, mid-1)
        elif numbers[mid] < search_num:
            return _binary_search(numbers, search_num, mid+1, right)
        else:
            #print(mid)
            return mid

    return _binary_search(numbers, search_num, 0, len(numbers)-1) >= 0


if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    search_num = 24
    print(binary_search(nums, search_num))
    print(binary_search_1_by_sakai(nums, search_num))
    print(binary_search_2_by_sakai(nums, search_num))
    print(binary_search_retry(nums, search_num))
