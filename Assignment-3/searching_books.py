def search_linear(a: list[str], item: str) -> int | None:
    """Searches the list for item linearly. Returns the position of item."""
    i = 0
    for j in a:
        if j == item:
            return i
        i += 1
    return None


def search_binary(a: list[str], item: str) -> int | None:
    """Searches the list for item binary. Returns the position of item."""
    def helper(a: list[str], item: str, min: int, max: int) -> int | None:
        mid = (min + max) // 2
        if min >= max:
            return None
        elif a[mid] == item:
            return mid
        elif a[mid] < item:
            return helper(a, item, (mid + 1), max)

        return helper(a, item, min, (mid - 1))

    return helper(a, item, 0, len(a))


def search_linear_cmp_count(a: list[str], item: str) -> int:
    """Searches the list for item linearly. Returns the number of comparisions needed."""
    i = 0
    for j in a:
        if j == item:
            return i + 1
        i += 1
    return i


def search_binary_cmp_count(a: list[str], item: str) -> int:
    """Searches the list for item linearly. Returns the number of comparisions needed."""
    def helper(a: list[str], item: str, min: int, max: int, count: int) -> int:
        c = count + 1
        mid = (min + max) // 2
        if min >= max:
            return c
        elif a[mid] == item:
            return c
        elif a[mid] < item:
            return helper(a, item, (mid + 1), max, c)

        return helper(a, item, min, (mid - 1), c)

    return helper(a, item, 0, len(a), 0)


if __name__ == "__main__":
    arr = ["asdsa", "abc", "Neural Networks", "fds", "dfs"]
    ls = search_linear(arr, "Neural Network")
    ls_cmp = search_linear_cmp_count(arr, "Neural Networks")
    bs = search_binary(arr, "Neural Networks")
    bs_cmp = search_binary_cmp_count(arr, "Neural Networks")
    print(f"Linear search output = {ls} and cmp output = {ls_cmp}")
    print(f"binary search output = {bs} and cmp output = {bs_cmp}")
    ls = search_linear(arr, "er")
    ls_cmp = search_linear_cmp_count(arr, "er")
    bs = search_binary(arr, "er")
    bs_cmp = search_binary_cmp_count(arr, "ers")
    print(f"Linear search output = {ls} no of cmp = {ls_cmp}")
    print(f"binary search output = {bs} no of cmp = {bs_cmp}")
