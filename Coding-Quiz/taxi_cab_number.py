from typing import List, Tuple
from collections import defaultdict


def taxi_cab_number(max_answer_num: int, match_answer_num: int = 2) -> List[Tuple[int, List[Tuple[int, int]]]]:
    result = []
    num = 1
    
    while len(result) < max_answer_num:
        r = (num, [])
        max_param = int(pow(num, 1.0 / 3)) + 1
        for i in range(1, max_param):
            for j in range(i + 1, max_param):
                if  i**3 + j**3 == num:
                    r[1].append((i, j))
                    if len(r[1]) == match_answer_num:
                        result.append(r)
                        break
        num += 1
    return result


def taxi_cab_number_by_sakai(max_answer_num: int, match_answer_num: int = 2, start_answer: int = 1) -> List[Tuple[int, List[Tuple[int, int]]]]:
    result = []
    got_answer_count = 0
    answer = start_answer
    
    while got_answer_count < max_answer_num:
        match_answer_count = 0
        memo = defaultdict(list)

        max_param = int(pow(answer, 1.0 / 3)) + 1
        for i in range(1, max_param):
            for j in range(i + 1, max_param):
                if  i**3 + j**3 == answer:
                    memo[answer].append((i, j))
                    match_answer_count += 1
        if match_answer_count == match_answer_num:
            result.append((answer, memo[answer]))    
            got_answer_count += 1
        answer += 1
    return result

if __name__ == '__main__':
    # Input 1, 2 => [(1729, [(1, 12), (9, 10)])]
    # Input 2, 2 => [(1729, [(1, 12), (9, 10)]), (4104, [(2, 16), (9, 15)])]
    # Input 1, 3 => [(87539319, [(167, 436), (228, 423), (255, 414)])
    print(taxi_cab_number_by_sakai(1, 2))