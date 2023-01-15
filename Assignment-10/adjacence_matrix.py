from typing import List


def in_degree(k: int, m: List[List[int]]) -> int:
    """Returns the number of nodes that directly connect to `k`."""
    count = 0
    for i in m:
        if i[k] == 1:
            count += 1
    return count


def out_degree(k: int, m: List[List[int]]) -> int:
    """Returns the number of nodes that `k` directly connects to."""
    count = 0
    for i in m[k]:
        count = count + i
    return count


def adjacent(k: int, m: List[List[int]]) -> List[int]:
    """Returns the nodes that `k` directly connects to."""
    adj = []
    i = 0   
    while i < len(m[k]):
        if m[k][i] == 1:
            adj.append(i)
        i += 1
    return adj


def has_triangle(m: List[List[int]]) -> bool:
    """Returns `True` if and only if m has a cycle of length 3."""
    is_triangle = False
    k = 0
    while k < len(m):
        i = 0
        while i < len(m[k]):
            if m[k][i] == 1:
                j = 0
                while j < len(m[i]):
                    if m[i][j] == 1 and m[j][k] == 1:
                        is_triangle = True
                    j += 1
            i += 1  
        k += 1      
    return is_triangle


if __name__ == "__main__":
    test = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    print(in_degree(1, test))
    print(has_triangle(test))
                
