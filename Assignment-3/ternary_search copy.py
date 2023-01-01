from typing import List
from random import randint
import time


def binary_search(a: List[int], item: int) -> int | None:
    """Searches the list for item with binary search. Returns the position of item."""  
    return binary_search_helper(a, item, 0, len(a)-1)

def binary_search_helper(a: List[int], item: int, low: int, high: int) -> int | None:
    mid = (low + high) // 2
    if low > high:
        return None
    elif a[mid] == item:
        return mid
    elif a[mid] < item:
        return binary_search_helper(a, item, (mid + 1), high)
            
    return binary_search_helper(a, item, low, (mid - 1))


def ternary_search_helper(a: List[int], item: int, low: int, high: int) -> int | None:
    oneThird = ((high - low) // 3) + low
    twoThird = ((high - low) // 3) + oneThird
    print(f"{low} {oneThird} {twoThird} {high}")
    if low > high:
        return None
    elif a[oneThird] == item:
        return oneThird
    elif a[twoThird] == item:
        return twoThird
    elif item < a[oneThird]:
        return ternary_search_helper(a, item, low, oneThird - 1)
    elif item > a[oneThird] and item < a[twoThird]:
        return ternary_search_helper(a, item, oneThird + 1, twoThird - 1)

    return ternary_search_helper(a, item, twoThird + 1, high)


def ternary_search(a: List[int], item: int) -> int | None:
    """Searches the list for item with ternary search. Returns the position of item."""
    length = len(a) - 1
    return ternary_search_helper(a, item, 0, length)

def time_binary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    binary_search(arr, item)
    return time.time() - start


def time_ternary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    ternary_search(arr, item)
    return time.time() - start


if __name__ == "__main__":
    # TODO: Test your binary and ternary search implementation here...

    # These constants should be defined here, don't move them!
    # MAX_VALUE = 50_000_000
    # NUM_ITER = 100_000
    # SEARCH_VALUES = [randint(0, MAX_VALUE - 1) for _ in range(NUM_ITER)]
    # ARRAY = list(range(MAX_VALUE))
    # print(f"Searching {NUM_ITER:_} random values in an array of size {MAX_VALUE:_}")
    # time_binary = 0.
    # for value in SEARCH_VALUES:
    #     time_binary += time_binary_search_in_s(ARRAY, value)

    # time_ternary = 0.
    # for value in SEARCH_VALUES:
    #     time_ternary += time_ternary_search_in_s(ARRAY, value)

    # print(f"Total binary search time:    {time_binary:.9f} s")
    # print(f"Total ternary search time:   {time_ternary:.9f} s")
    # print(f"Average binary search time:  {time_binary / NUM_ITER:.9f} s")
    # print(f"Average ternary search time: {time_ternary / NUM_ITER:.9f} s")
    print(ternary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],10))

"""
TODO: Task 3, compare the algorithms.
"""
