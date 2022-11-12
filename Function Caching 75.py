# Saves the previously returned values

import time
from functools import lru_cache


@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("running some work")
    some_work(3)
    print("done")
    some_work(3)
    print("done 1")
    some_work(3)
    print("done 2")
    some_work(3)
    print("done 3")
