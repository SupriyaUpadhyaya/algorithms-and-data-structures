__author__ = "Supriya Upadhyaya"
__email__ = "supriya.upadhyaya@st.ovgu.de"

import math

# Function returns 'True' if given integer input is a prime number else returns 'False'


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

# Functions return the given integer input 'n' if it is a prime number else returns next possible prime number p


def next_prime(n: int) -> int:
    if n <= 2:
        return 2
    else:
        if n % 2 != 0:
            checkPrime = is_prime(n)
        else:
            checkPrime = False

        if checkPrime is not False:
            return n
        else:
            checkNextPrime = False
            if n % 2 == 0:
                n += 1
            while checkNextPrime is False:
                checkNextPrime = is_prime(n)
                n += 2
            return (n - 2)


def testing(n: int, output: int, is_prime_num: bool) -> str:
    if is_prime(n) == is_prime_num and next_prime(n) == output:
        return "PASS"
    else:
        return "FAIL"


if __name__ == "__main__":
    print(testing(0, 2, False))
    print(testing(1, 2, False))
    print(testing(2, 1, True))
    print(testing(-5, 2, False))
    print(testing(15, 17, False))
