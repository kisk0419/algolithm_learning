from typing import List, NewType

PhoneNumber = NewType('PhoneNumber', str)

NUM_ALPHABET_MAPPING = {
    0: PhoneNumber('+'),
    1: PhoneNumber('@'),
    2: PhoneNumber('ABC'),
    3: PhoneNumber('DEF'),
    4: PhoneNumber('GHI'),
    5: PhoneNumber('JKL'),
    6: PhoneNumber('MNO'),
    7: PhoneNumber('PQRS'),
    8: PhoneNumber('TUV'),
    9: PhoneNumber('WXYZ')
}

def memonic(phone_num: str) -> List[str]:
    results = []
    stack = []
    def _memonic(index: int):
        if index >= len(phone_num):
            results.append(''.join(stack))
            stack.pop()
            return
        num = phone_num[index]
        if num == '-':
            _memonic(index+1)
            return
        for char in NUM_ALPHABET_MAPPING[int(num)]:
            stack.append(char)
            _memonic(index+1)
        if stack:
            stack.pop()
        
    results = []
    _memonic(0)

    return results

def phone_memonic_by_sakai_v1(phone_number: PhoneNumber) -> List[PhoneNumber]:
    phone_number: List[int] = [int(s) for s in phone_number.replace('-', '')]
    candidate: List[PhoneNumber] = []
    tmp: List[PhoneNumber] = [''] * len(phone_number)

    def find_candidate_alphabet(digit: int = 0) -> None:
        if digit == len(phone_number):
            candidate.append(''.join(tmp))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number[digit]]:
                tmp[digit] = char
                find_candidate_alphabet(digit+1)
    find_candidate_alphabet()
    return candidate


def phone_memonic_by_sakai_v2(phone_number: PhoneNumber) -> List[PhoneNumber]:
    phone_number: List[int] = [int(s) for s in phone_number.replace('-', '')]
    candidate: List[PhoneNumber] = []
    stack: List[PhoneNumber] = ['']
    while len(stack) > 0:
        alphabets = stack.pop()
        if len(alphabets) == len(phone_number):
            candidate.append(alphabets)
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number[len(alphabets)]]:
                stack.append(PhoneNumber(alphabets + char))
    return candidate

if __name__ == '__main__':
    numbers = ['568-379-8466']
    for num in numbers:
        for c in phone_memonic_by_sakai_v2(num):
            if c == 'LOVEPYTHON':
                print(c)
