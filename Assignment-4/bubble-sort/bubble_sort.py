"""
3.  # TODO

"""


def bubble_sort(array: list) -> None:
    """Sorts `array` with bubblesort inplace."""
    length = len(array)
    print(length)
    for i in range(length - 1, 0, -1):
        for j in range(1, i + 1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
        print(i)



if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    bubble_sort(array)
    assert array == [1, 2, 3, 4, 5]