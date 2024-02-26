"""
1.  # TODO

2.  # TODO

"""


def merge_sort(array: list[int]) -> list[int]:
    """Sorts `array` with merge-sort"""
    length = len(array) // 2
    m, n = array[:length], array[length:]
    if len(m) > 1:
        m = merge_sort(m)
    if len(n) > 1:
        n = merge_sort(n)
    output = merge(m, n)
    return output


def merge(m: list[int], n: list[int]) -> list[int]:
    i, j = 0, 0
    k = len(m) + len(n)
    out = [0 for z in range(k)]
    for x in range(k):
        if i >= len(m):
            out[x] = n[j]
            j += 1
            
        elif j >= len(n):
            out[x] = m[i]
            i += 1
            
        elif m[i] <= n[j]:
            out[x] = m[i]
            i += 1
            
        else:
            out[x] = n[j]
            j += 1
            
    return out


if __name__ == "__main__":
    input = [3, 2, 4, 1, 5, 7]
    array1 = merge_sort(input)
    print(array1)
    assert array1 == [1, 2, 3, 4, 5, 7]