from typing import List
from collections import OrderedDict
from collections import Counter
import time


def print_duration(func):
    def _wrapper(x: List[int], y: List[int]) -> None:
        import time
        start = time.time()
        func(x, y)
        print(f'duration: {time.time() - start}')
    return _wrapper

@print_duration
def mini_count_remove(x: List[int], y: List[int]) -> None:
    x_cache = OrderedDict()
    y_cache = OrderedDict()

    for n in x:
        x_cache[n] = x_cache.get(n, 0) + 1
            
    for n in y:
        y_cache[n] = y_cache.get(n, 0) + 1
    
    for key_x, value_x in x_cache.items():
        value_y = y_cache.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]
    
@print_duration
def mini_count_remove_without_order(x: List[int], y: List[int]) -> None:
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]




if __name__ == '__main__':
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]

    print(f'x={x}')
    print(f'y={y}')

    print('###########')

    mini_count_remove(x, y)

    print(f'x={x}')
    print(f'y={y}')

    print('###########')


    mini_count_remove_without_order(x, y)

    print(f'x={x}')
    print(f'y={y}')
