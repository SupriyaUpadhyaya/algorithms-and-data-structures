"""
2.  # TODO

3.  # TODO

"""


def partition(array: list, first: int, last: int) -> int:
    pivot = array[last]
    m = first - 1

    for n in range(first, last):
        if array[n] <= pivot:
            m += 1
            array[m], array[n] = array[n], array[m]
    
    array[m + 1], array[last] = array[last], array[m + 1]
    return m + 1


def quick_sort(array: list) -> None:
    """Sorts `array` with quick-sort in-place."""
    _qsort(array, 0, len(array) - 1)
    return None


def _qsort(array: list, left: int, right: int) -> None:
    if left < right:
        p = partition(array, left, right)
        _qsort(array, left, p - 1)
        _qsort(array, p + 1, right)
    return None


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    quick_sort(array)
    assert array == [1, 2, 3, 4, 5]