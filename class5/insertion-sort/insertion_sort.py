"""
2.  # TODO

"""


def insertion_sort(array: list) -> None:
    """Sorts `array` with insertionsort inplace."""
    length = len(array)
    for i in range(1, length):
        element = array[i]
        j = i
        while j > 0 and element < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = element


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    insertion_sort(array)
    assert array == [1, 2, 3, 4, 5]