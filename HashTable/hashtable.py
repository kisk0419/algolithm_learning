from typing import Any
import hashlib


class HashTable(object):
    def __init__(self, size: int = 10):
        self.size = size
        self.table = [[] for _ in range(self.size)]


    def hash(self, key: str) -> int:
        digest = hashlib.md5(key.encode()).hexdigest()
        return int(digest, base=16) % self.size


    def add(self, key: str, value: Any):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])
    

    def get(self, key: str) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
        raise KeyError()


    def __setitem__(self, key: str, value: Any) -> None:
        self.add(key, value)


    def __getitem__(self, key: str) -> Any:
        return self.get(key)


    def print(self):
        for i in range(self.size):
            print(i, end=' ')
            for data in self.table[i]:
                print(f'--> {data}', end=' ')
            print()
    

if __name__ == '__main__':
    hash_table = HashTable()
    hash_table['sns'] = 'Youtube'
    hash_table['pc'] = 'Mac'
    hash_table['car'] = 'Tesla'
    hash_table['car'] = 'Toyota'
    hash_table.print()
    print(hash_table['car'])
    print(hash_table['pc'])
    print(hash_table['hoge'])

