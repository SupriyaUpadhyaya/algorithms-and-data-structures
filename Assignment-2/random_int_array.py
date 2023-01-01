import random

def create_random(n: int) -> list[int]:
    return [random.randint(5,99) for i in range(n)]


def to_string(a: list[int]) -> str:
    output = ""
    for i in a :
        output = output + str(i)
    return output


def pos_min(a: list[int]) -> int:
    b = [i for i in a]
    for n in range(len(b)-1):
        i = 0
        while i < len(b)-1:
            if( b[i] > b[i+1] ):
                b[i], b[i+1] = b[i+1], b[i]
            i = i + 1
    for n in range(0, len(a)-1, 1):
        if a[n] == b[0]:
            return n

        
def swap(a: list[int]) -> None:
    a[0], a[len(a)-1] = a[len(a)-1], a[0]

op = create_random(-7)
print(op)
print(pos_min(op))