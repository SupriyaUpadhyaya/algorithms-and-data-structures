"""
1.  # In-Place algorithms do not require any additional space or memory for input manipulation. 
    # They override the input with output. Only small additional space for auxillary variables. 
    # Ex : selection, insertion or bubble sort
    # Out-Of-Place algorithms require considerable additional memory. Ex : Merge sort
    
3.  # TODO

"""


def selection_sort(array: list) -> None:
    """Sorts `array` with selectionsort inplace."""
    length = len(array)
    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    selection_sort(array)
    assert array == [1, 2, 3, 4, 5]