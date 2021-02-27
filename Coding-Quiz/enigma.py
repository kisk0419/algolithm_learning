import string
from typing import Dict, List
import random

class Base(object):
    def __init__(self, words: str, map_word: str):
        self.forwards = {}
        self.backwards = {}
        self.words = words
        self.mapping(self.words, map_word)

    def mapping(self, words, map_words) -> None:
        for x, y in zip(words, map_words):
            self.forwards[x] = y
            self.backwards[y] = x

    def _conver(self, index: int, word_dict: Dict[str, str]) -> int:
        if len(self.words) <= index:
            raise ValueError()
        char = self.words[index]
        
        if char not in word_dict:
            raise ValueError()
        #print(f'  {char} -> ', end='')
        char = word_dict[char]
        #print(f'{char}')
        return self.words.index(char)

    def forward(self, index: int) -> int:
        return self._conver(index, self.forwards)

    def backward(self, index: int) -> int:
        return self._conver(index, self.backwards)
    

class Plugboard(Base):
    def forward(self, char: str) -> int:
        if char not in self.words:
            raise ValueError()

        index = self.words.index(char)
        return super().forward(index)


    def backward(self, index: int) -> str:
        i = super().backward(index)
        return self.words[i]


class Reflector(object):
    def __init__(self, words: str, reflect_words: str):
        self.words = words
        self.reflects = dict(zip(words, reflect_words))
        for k, v in self.reflects.items():
            if k != self.reflects[v]:
                raise ValueError()
    
    def reflect(self, index: int) -> int:
        char = self.words[index]
        char = self.reflects[char]
        return self.words.index(char)


class Roter(Base):
    def __init__(self, shift: int, words: str, map_words: str):
        super().__init__(words, map_words)
        self.shift = shift
        self.rotate_count = 0
        self.org_words = words
    
    def reset_rotate(self) -> None:
        self.rotate_count = 0
        self.words = self.org_words

    def rotate(self) -> int:
        ##print(f' rotate {self.words} ->', end=' ')
        self.words = self.words[self.shift:] + self.words[0:self.shift]
        ##print(f' {self.words}')
        self.rotate_count += self.shift
        return self.rotate_count
    

class Roters(object):
    def __init__(self, words):
        self.words = words
        self.roters = [
            Roter(
                2, 
                words, 
                ''.join(random.sample(words, len(words)))
            ),
            Roter(
                3, 
                words, 
                ''.join(random.sample(words, len(words)))
            ),
            Roter(
                2, 
                words, 
                ''.join(random.sample(words, len(words)))
            ),
        ]

    def reset_rotate(self) -> None:
        for roter in self.roters:
            roter.reset_rotate()

    def rotate(self) -> None:
        for roter in reversed(self.roters):
            if roter.rotate() % len(self.words) != 0:
                self.reset_rotate()
                return

    def forward(self, index: int) -> int:
        for roter in self.roters:
            #print(f' roter: {index}')
            index = roter.forward(index)
            #print(f'  -> {index}')
        return index

    def backward(self, index: int) -> int:
        for roter in reversed(self.roters):
            #print(f' roter: {index}')
            index = roter.backward(index)
            #print(f'  -> {index}')
        return index


class Enigma(object):
    def __init__(self, words):
        self.words = words
        self.plugboard = Plugboard(
            words, 
            ''.join(random.sample(words, len(words)))
        )
        indexes = [i for i in range(len(words))]
        word_list = list(words)
        for _ in range(len(indexes) // 2):
            i = indexes.pop(random.randint(0, len(indexes) - 1))
            j = indexes.pop(random.randint(0, len(indexes) - 1))
            word_list[i], word_list[j] = word_list[j], word_list[i]
        
        self.reflector = Reflector(
            words, 
            ''.join(word_list)
        )
        self.roters = Roters(
            words
        )
    
    def encrypt(self, text: str) -> str:
        encrypted = []
        for char in text:
            encrypted.append(self.get_through(char))
        return ''.join(encrypted)

    def decrypt(self, text: str) -> str:
        self.roters.reset_rotate()
        decrypted = []
        for char in text:
            decrypted.append(self.get_through(char))
        return ''.join(decrypted)

    
    def get_through(self, char: str) -> str:
        char = char.upper()
        if char not in self.words:
            return char
        #print(f'plugboard:')
        index = self.plugboard.forward(char)
        #print(f'index= {index}')
        #print(f'roters:')
        index = self.roters.forward(index)
        #print(f'index= {index}')
        #print(f'reflector:')
        index = self.reflector.reflect(index)
        #print(f'index= {index}')
        #print(f'roters:')
        index = self.roters.backward(index)
        self.roters.rotate()
        #print(f'index= {index}')
        return self.plugboard.backward(index)


if __name__ == '__main__':
    enigma = Enigma(string.ascii_uppercase)
    words = 'ATTACK SILICON VALLEY'
    e = enigma.encrypt(words)
    print(e)
    d = enigma.decrypt(e)
    print(d)