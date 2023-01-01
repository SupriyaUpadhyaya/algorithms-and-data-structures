def is_triangular(n: int) -> bool:
    i = 1
    while n >= 0:
        if ( n == 0):
            is_t = True
        elif ( n >= i):
            is_t = True
        else:
            is_t = False
        n -= i
        i = i + 1
    return is_t

print(is_triangular(6))