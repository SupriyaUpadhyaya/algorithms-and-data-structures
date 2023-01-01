import random

def create_random(n: int) -> list[int]:
    return [random.randint(5,99) for i in range(n)]


def to_string(a: list[int]) -> str:
    output = ""
    for i in a :
        output = output + str(i)
    return output


def pos_min(a: list[int]) -> int:
    d = {i: a[i] for i in range(0, len(a), 1)}
    for i in range(len(a)):
        if( a[i] < a[0] ):
            a[0], a[i] =  a[i], a[0]
    for key, val in d.items():
        if val == a[0]:
            return int(key)


def swap(a: list[int]) -> None:
    a[0], a[len(a)-1] = a[len(a)-1], a[0]

op = create_random(6)
print(op)
print(pos_min(op))