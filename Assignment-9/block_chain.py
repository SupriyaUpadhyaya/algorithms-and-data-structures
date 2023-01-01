from dataclasses import dataclass
import hashlib
import random


def bytes_to_bits(arr: bytes,) -> str:
    """
    Converts a byte object to a string containing the individual bits.

    This function pads the resulting string with leading 0s.

        E.g. bytes_to_bits(b'\x11') == "0000000100000001"
    """
    return ''.join(format(byte, '08b') for byte in arr)


@dataclass
class Block:
    def __init__(self, message: str, previousHashCode: bytes) -> None:
        self.message = message
        self.previousHashCode = previousHashCode
        self.proofOfWork = 0

    def hash(self) -> bytes:
        hashing = hashlib.sha256()
        hashing.update(self.__str__().encode('utf-8'))
        return hashing.digest()

    def __str__(self) -> str:
        output = self.message + " " + self.previousHashCode.decode('utf-8') + " " + str(self.proofOfWork)
        return output


def number_of_leading_zeros(block: Block) -> int:
    output = len(str(bytes_to_bits(block.hash())).rsplit("1")[0])
    return output


def verify(block: Block, x: int) -> bool:
    if number_of_leading_zeros(block) == x:
        output = True
    else:
        output = False
    return output


def proof_of_work(block: Block, x: int) -> None:
    while block.proofOfWork == 0:
        block.proofOfWork = random.randint(1, 100000)
        print(block)
        zeros = number_of_leading_zeros(block)
        if zeros != x:
            block.proofOfWork = 0
        print(block)
    return None


if __name__ == "__main__":
    block = Block("Message", b'test')
    print(block)
    block.hash()
    number_of_leading_zeros(block)
    print(block, verify(block, 16))
    proof_of_work(block, 16)
    print(block, verify(block, 16))
