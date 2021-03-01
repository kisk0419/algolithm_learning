from typing import List


def generate_pascal_triangle(depth: int) -> List[List[int]]:
    traiangles = [[1] * (i + 1) for i in range(depth)]
    for i in range(depth):
        if i <= 1:
            continue
        len_triangle = len(traiangles[i])
        for j in range(len_triangle):
            if j == 0 or j == (len_triangle - 1):
                continue
            traiangles[i][j] = traiangles[i - 1][j - 1] + traiangles[i - 1][j]
    return traiangles


def generate_pascal_triangle_by_sakai(depth: int) -> List[List[int]]:
    data = [[1] * (i + 1) for i in range(depth)]
    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line - 1][i - 1] + data[line - 1][i]
    return data


def print_formatted_triangle(traiangles: List[List[int]]) -> None:
    if not traiangles:
        return
    last_triangle_len = len(traiangles[-1])
    for triangle in traiangles:
        print('  ' * (last_triangle_len - len(triangle)), end='')
        for t in triangle:
            print(t, end=(' ' * (4 - len(str(t)))))
        print('')
    

def print_pascal(data: List[List[int]]) -> None:
    max_digit = len(str(max(data[-1])))
    width = max_digit + (max_digit % 2) + 2

    for index, line in enumerate(data):
        numbers = ''.join([str(i).center(width, ' ') for i in line])
        print(' ' * (width // 2 * (len(data) - index)), numbers)

if __name__ == '__main__':
    print_pascal(generate_pascal_triangle_by_sakai(8))