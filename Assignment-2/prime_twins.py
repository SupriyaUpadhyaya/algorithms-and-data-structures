import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        squareRootN = round(math.sqrt(n)) + 1
        isPrime = True
        for i in range(2, squareRootN, 1):
            if (n % i == 0):
                isPrime = False
        return isPrime


def prime_twins(n: int) -> list[tuple[int, int]]:
    mat: list[tuple[int, int]] = []
    a = 2
    if n >= 1:
        while len(mat) < n:
            p_is_prime = is_prime(a)
            q_is_prime = is_prime(a + 2)
            if (p_is_prime is True and q_is_prime is True):
                if mat == []:
                    mat = [(a, a + 2)]
                else:
                    mat = mat + [(a, a + 2)]
            a += 1
        return mat
    else:
        mat = []
        return mat


def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    mat: list[tuple[int, int, int]] = []
    a = 2
    if n >= 1:
        while len(mat) < n:
            p_is_prime = is_prime(a)
            p2_is_prime = is_prime(a + 2)
            p4_is_prime = is_prime(a + 4)
            p6_is_prime = is_prime(a + 6)
            if p_is_prime is True and p2_is_prime is True and p6_is_prime is True:
                if mat == []:
                    mat = [(a, a + 2, a + 6)]
                else:
                    mat = mat + [(a, a + 2, a + 6)]
            elif p_is_prime is True and p4_is_prime is True and p6_is_prime is True:
                if mat == []:
                    mat = [(a, a + 4, a + 6)]
                else:
                    mat = mat + [(a, a + 4, a + 6)]
            a += 1
        return mat
    else:
        mat = []
        return mat


op = prime_twins(2)
print(op)
op1 = prime_triplets(2)
print(op1)
