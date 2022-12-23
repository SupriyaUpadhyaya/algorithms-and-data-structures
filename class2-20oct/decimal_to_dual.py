__author__ = "Supriya Upadhyaya"
__email__ = "supriya.upadhyaya@st.ovgu.de"


def transform_to_dual(dec: int) -> str:
    if dec <= 0:
        return ("Please enter a number greater than 0")
    else:
        bin = ""
        while dec > 0:
            rem = dec % 2
            bin = bin + str(rem)
            dec = int(dec / 2)
        return (bin[::-1])


def testing(dec: int, bin_op: str) -> str:
    if transform_to_dual(dec) == bin_op:
        return "PASS"
    else:
        return "FAIL"


if __name__ == "__main__":
    print(testing(13, "1101"))
    print(testing(3, "100"))
    print(transform_to_dual(-3))