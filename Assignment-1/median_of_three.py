__author__ = "Supriya Upadhyaya"
__email__ = "supriya.upadhyaya@st.ovgu.de"


def median(a: int, b: int, c: int) -> int:
    arr = [a, b, c]
    sorted_arr = sorted(arr)
    return sorted_arr[1]


def median2(a: int, b: int, c: int) -> int:
    arr = [a, b, c]
    arr.sort()
    return arr[1]


def testing(a: int, b: int, c: int, med: int) -> str:
    if (median(a, b, c) == med) and median2(a, b, c) == med:
        return "PASS"
    else:
        return "FAIL"


if __name__ == "__main__":
    print(testing(25, 11, 33, 25))
    print(testing(1, 1, 2, 1))
    print(testing(5, 5, -5, 5))
    print(testing(-3, -1, 8, -1))
    print(testing(-3, -1, 8, 0))