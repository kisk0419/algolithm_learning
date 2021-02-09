from typing import List
import string
import operator


def snake_string(chars: List[str], line_num: int = 3, loop_num: int = 2) -> List[List[str]]:
    lines = [[] for _ in range(line_num)]
    
    dir = -1
    index = line_num // 2
    for _ in range(loop_num):
        for char in chars:
            for line in lines:
                line.append(' ')
            
            lines[index][-1] = char

            if index >= line_num - 1 or index <= 0:
                dir *= -1
            index += dir
    
    return lines


def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    result_idexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_idexes - {insert_index}:
            result[rest_index].append(' ')
    return result


def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = depth // 2

    op = operator.neg

    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')
    
        if insert_index <= 0:
            op = operator.pos
        if insert_index >= depth - 1:
            op = operator.neg
        insert_index += op(1)
    
    return result

def print_lines(lines: List[List[str]]) -> None:
    for line in lines:
        print(''.join(line))


if __name__ == '__main__':
    print_lines(snake_string(string.digits, 3))
    print_lines(snake_string_v2(''.join(string.digits), 3))

    #print_lines(snake_string(string.ascii_lowercase, 10))

