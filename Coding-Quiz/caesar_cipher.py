import string
from typing import Generator

def caesar_cipher(text: str, shift: int) -> str:
    ascii = None
    result = []
    for t in text:
        if t.islower():
            ascii = string.ascii_lowercase
        elif t.isupper():
            ascii = string.ascii_uppercase
        else:
            result.append(t)
            continue
        
        index = (ascii.index(t) + shift) % len(ascii)
        result.append(ascii[index])
    return ''.join(result)


def caesar_cipher_by_sakai(text: str, shift: int) -> str:
    result = ''
    for char in text:
        if char.islower():
            alphabet = string.ascii_lowercase
        elif char.isupper():
            alphabet = string.ascii_uppercase
        else:
            result += char
            continue
        
        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]
    return result


def caesar_cipher_no_use_string(text: str, shift: int) -> str:
    result = ''
    len_alphabet = ord('Z') - ord('A') + 1
    for char in text:
        if char.isupper():
            result += chr(((ord(char) - ord('A') + shift) % len_alphabet) + ord('A'))
        elif char.islower():
            result += chr(((ord(char) - ord('a') + shift) % len_alphabet) + ord('a'))
        else:
            result += char
    return result


def caesar_cipher_hach(text: str) -> Generator[str, None, None]:
    len_alphabet = ord('Z') - ord('A') + 1

    for shift in range(1, len_alphabet + 1):
        result = ''
        for char in text:
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % len_alphabet + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') - shift) % len_alphabet + ord('a'))
            else:
                result += char
        yield result


if __name__ == '__main__':
    text = "ATTACK SILICON VALLY by engineer"
    t = caesar_cipher(text, 3)
    print(t)
    # t = caesar_cipher(t, -3)
    # print(t)
    
    # t = caesar_cipher_by_sakai(text, 3)
    # print(t)
    # t = caesar_cipher_by_sakai(t, -3)
    # print(t)
    for h in caesar_cipher_hach(t):
        print(h)