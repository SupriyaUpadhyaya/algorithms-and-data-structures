"""
Solution for part 2.
# TODO
"""

number_recursive_calls = 0


def fib1(n: int) -> int:
    """Calculates the `n`th fibonacci number recursively.""" 
    global number_recursive_calls
    if n == 0 or n == 1:
        number_recursive_calls += 1
        return 1
    else:
        number_recursive_calls += 1
        return (fib1(n - 2) + fib1(n - 1))


def fib2(n: int) -> int:
    """Calculates the `n`th fibonacci number iteratively."""
    global number_recursive_calls
    number_recursive_calls = 1
    if n == 0 or n == 1:
        return 1
    else:
        fib = [1, 1]
        i = 2
        while i <= n:
            number_recursive_calls += 1
            prev1: int = fib[i - 1]
            prev2: int = fib[i - 2]
            fib.append(prev1 + prev2)
            i += 1
    return fib[n]
    

if __name__ == "__main__":
    fib_numbers = []
    for i in range(0, 15, 1):
        number_recursive_calls = 0
        fib_numbers.append(fib1(i))
    print(number_recursive_calls)
    print(f"15 Fibonacci numbers using fib1 : {fib_numbers}")
    number_recursive_calls = 0
    print(f"23rd Fibonacchi number using fib1 (recursive) = {fib1(22)}")
    print(f"No of functions calls using fib1 (recursive) for 23rd fibonacchi = {number_recursive_calls}")
    print(f"23rd Fibonacchi number using fib2 (iterative) = {fib2(22)}")
    number_recursive_calls = 0
    fib2(22)
    print(f"No of functions calls using fib2 (iterative) for 23rd fibonacchi = {number_recursive_calls}")


