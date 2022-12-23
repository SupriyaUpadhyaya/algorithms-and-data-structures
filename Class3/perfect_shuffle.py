def interleave(a: list[int], b: list[int]) -> list[int]:
    c = []
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    return c


def perfect_shuffle(a: list[int]) -> list[int]:
    b = []
    c = []
    i = 0
    while i < round(len(a)/2):
        b.append(a[i])
        c.append(a[i + round(len(a)/2)])
        i += 1
    op = interleave(b, c)
    return op


def shuffle_number(n: int) -> int:
    a = []
    for i in range(n):
        a.append(i + 1)
    b = perfect_shuffle(a)
    j = 1
    while ( a != b ):
        b = perfect_shuffle(b)
        j += 1
    return j

if __name__ == "__main__":
    print(shuffle_number(52))