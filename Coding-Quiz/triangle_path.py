from typing import List
import random
import sys

def get_triangle(depth: int, max_num: int) -> List[List[int]]:
    result = [[random.randint(0, max_num) for _ in range(i + 1)] for i in range(depth)]
    return result

def show_triangles(triangles: List[List[int]]) -> None:
    max_digit = len(str(max([max(triangle) for triangle in triangles])))
    width = max_digit * 2 + max_digit % 2
    for i, triangle in enumerate(triangles):
        print(' ' * (width // 2) * (len(triangles[-1]) - i), ''.join([str(t).center(width, ' ') for t in triangle]))


def find_min_path_v1(triangles: List[List[int]]) -> int:
    def _search(index: int, depth: int, sum: int, min_path: int):
        if index < 0 or index > depth:
            return min_path
        
        current_path = sum + triangles[depth][index]
        if depth == len(triangles) - 1:
            if current_path < min_path:
                return current_path
            else:
                return min_path
        min_path = _search(index, depth + 1, current_path, min_path)
        min_path = _search(index + 1, depth + 1, current_path, min_path)
        return min_path
    
    min_path = _search(0, 0, 0, sys.maxsize)
    return min_path


def sum_min_path_by_sakai(triangle: List[List[int]]) -> int:
    sum_triangle = triangle[:]
    j, len_triangle = 1, len(triangle)
    while j < len_triangle:
        line = triangle[j]
        line_min_path = []
        for i, value in enumerate(line):
            if i == 0:
                sum_value = value + sum_triangle[j - 1][i]
            elif i == len(triangle[j]) - 1:
                sum_value = value + sum_triangle[j - 1][i - 1]
            else:
                min_path = min(sum_triangle[j - 1][i - 1], sum_triangle[j - 1][i])
                sum_value = value + min_path
            line_min_path.append(sum_value)
        sum_triangle[j] = line_min_path
        j += 1
    return min(sum_triangle[-1])


if __name__ == '__main__':
    triangles = get_triangle(5, 20)
    print(triangles)
    show_triangles(triangles)
    import time
    print('find_min_path_v1')
    start = time.time()
    print(f'min path = {find_min_path_v1(triangles)}')
    print(time.time() - start)

    print('find_min_path_v1')
    start = time.time()
    print(f'min path = {sum_min_path_by_sakai(triangles)}')
    print(time.time() - start)
