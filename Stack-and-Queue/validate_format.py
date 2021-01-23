
def validate_format(chars: str) -> bool:
    marks = {'{': '}', '[': ']', '(': ')'}
    stack = []
    
    if not chars:
        return True

    for char in chars:
        if char in marks.keys():
            stack.append(marks[char])
        elif char in marks.values():
            if not stack:
                return False
            last_mark = stack.pop()
            if char != last_mark:
                return False
    return len(stack) == 0
    
    


if __name__ == '__main__':
    """
    Input {'key1': 'value1, 'key2': [1, 2, 3], 'key3': (1, 2, 3)}} Output True
    Input {'key1': ['value1, 'key2': [1, 2, 3], 'key3': (1, 2, 3)}} Output False
    """

    print(validate_format("{'key1': 'value1, 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"))
    print(validate_format("{'key1': ['value1, 'key2': [1, 2, 3], 'key3': (1, 2, 3)}}"))
    print(validate_format("]{'key1': 'value1, 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"))
    print(validate_format("{'key1': 'value1, 'key2': [1, 2, 3], 'key3': (1, 2, 3)}["))