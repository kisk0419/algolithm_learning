import time


def memoize(func):
    '''
    Slow
    '''
    cache = {}
    def _wrapper(num: int) -> int:
        value = cache.get(num)
        if not value:
            value = func(num)
            cache[num] = value
        return value
    return _wrapper


def memoize_v2(func):
    cache = {}
    def _wrapper(num: int) -> int:
        if num not in cache:
            cache[num] = func(num)
        return cache[num]
    return _wrapper
    

@memoize
def long_func(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


@memoize_v2
def long_func_2(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


if __name__ == '__main__':
    for i in range(10):
        long_func(i)

    start = time.time()

    for i in range(10):
        print(long_func(i))
    
    print(time.time() - start)

    print('############')

    for i in range(10):
        long_func_2(i)

    start_v2 = time.time()

    for i in range(10):
        print(long_func_2(i))
    
    print(time.time() - start_v2)
