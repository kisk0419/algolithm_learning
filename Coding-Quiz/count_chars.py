from collections import Counter
from typing import Tuple
import operator


def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    
    # l = []
    # for char in strings:
    #     if not char.isspace():
    #         l.append((char, strings.count(char)))
    
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]
    return max(l, key=operator.itemgetter(1))


def count_chars_v2(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = dict()

    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1

    max_key = max(d, key=d.get)
    return max_key, d[max_key]    


def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter()

    for char in strings:
        if not char.isspace():
            d[char] += 1

    max_key = max(d, key=d.get)
    return max_key, d[max_key]    


def count_chars(word: str) -> Tuple[str, int]:
    counter = Counter(word.lower().replace(' ', ''))
    return counter.most_common(1)[0]


if __name__ == '__main__':
    word = 'This is a pen. This is an apple. Applepen'

    print(count_chars(word))
    print(count_chars_v1(word))
    print(count_chars_v2(word))
    print(count_chars_v3(word))
