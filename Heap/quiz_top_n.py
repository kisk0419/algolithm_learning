import heapq
from collections import defaultdict
from collections import Counter
from typing import List, Tuple


def top_n_with_count(words: List[str], n: int) -> List[Tuple[int, str]]:
    couted_words = Counter(words)
    couted_words = [(-v, k) for k, v in couted_words.items()]
    n = min(n, len(couted_words))
    result = [heapq.heappop(couted_words) for _ in range(n)]
    return [(-r[0], r[1]) for r in result]


def top_n_with_heap(words: List[str], n: int) -> List[str]:
    counter_words = Counter(words)
    counter_words = [(-counter_words[word], word) for word in counter_words]
    heapq.heapify(counter_words)
    n = min(n, len(counter_words))
    return [heapq.heappop(counter_words)[1] for _ in range(n)]
    

if __name__ == '__main__':
    words = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    # top_words = top(2, words)
    # for word in top_words:
    #     print(word)
    print(top_n_with_count(words, 5))

