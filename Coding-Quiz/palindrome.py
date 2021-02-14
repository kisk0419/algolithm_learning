from typing import Generator, List


def is_palindrome(word: str) -> bool:
    word_len = len(word)
    if word_len % 2 == 0:
        return False
    if word_len == 1:
        return True
    if word[0] != word[word_len-1]:
        return False
    return is_palindrome(word[1:word_len-1])
 

def is_palindrome_by_sakai(strings: str) -> bool:
    len_strings = len(strings)
    if not len_strings:
        return False
    if len_strings == 1:
        return True
    
    start, end = 0, len_strings-1
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True


def find_palindrome(strings: str) -> List[str]:
    def _find_palindrome(left: int, right: int, result: List[str]) -> List[str]:
        if left >= 0 and right < len(strings) and strings[left] == strings[right]:
            result.append(strings[left: right+1])
            return _find_palindrome(left - 1, right + 1, result)
        else:
            return result

    result = []
    for i in range(1, len(strings)):
        _find_palindrome(i-1, i+1, result)
        _find_palindrome(i-1, i, result)
        
    return result

def find_palindrome2(strings: str) -> Generator[str, None, None]:
    def _find_palindrome(left: int, right: int) -> Generator[str, None, None]:
        if left >= 0 and right < len(strings) and strings[left] == strings[right]:
            yield strings[left: right+1]
            yield from _find_palindrome(left - 1, right + 1)
        

    for i in range(1, len(strings)):
        yield from _find_palindrome(i-1, i+1)
        yield from _find_palindrome(i-1, i)
    

def find_palindrome_by_sakai(strings: str, left: int, right: int) -> Generator[str, None, None]:
    len_strings = len(strings)
    while 0 <= left and right < len_strings:
        if strings[left] != strings[right]:
            break
        yield strings[left: right+1]
        left -= 1
        right += 1
    

def find_all_palindrome_by_sakai(strings: str) -> Generator[str, None, None]:
    len_strings = len(strings)
    if not len_strings:
        yield
    if len_strings == 1:
        yield strings

    for i in range(1, len_strings-1):
        yield from find_palindrome_by_sakai(strings, i-1, i+1)
        yield from find_palindrome_by_sakai(strings, i-1, i)



if __name__ == '__main__':
    # ''.join(reversed(word))
    # word[::-1]
    word1s = ['aba', 'abc', 'racecar']
    for w in word1s:
        #print(is_palindrome(w))
        print(is_palindrome_by_sakai(w))

    word2s = ['abcracecarbda', 'aeea']
    
    for word in word2s:
        for p in find_palindrome2(word):
            print(p)
   
    print('######')
   
    for word in word2s:
        for p in find_all_palindrome_by_sakai(word):
            print(p)
   
        
