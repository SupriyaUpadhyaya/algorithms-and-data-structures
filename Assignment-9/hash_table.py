from random import seed
import random

seed(0)
capacity_ = 1249


def h2(x: int) -> int:
    return x << 5


class HashLinQuadDouble:
    def __init__(self, n: int) -> None:
        # Zero indicates an empty slot
        self.table = [0 for _ in range(n)]

    def add_lin(self, obj: int) -> int:
        length = len(self.table)
        index = obj % length

        position_checked = 1

        while self.table[index] != 0:
            if position_checked == (length - 1):
                return position_checked
            position_checked += 1
            index = (index + 1) % length
            
        self.table[index] = obj

        return position_checked

    def add_quad(self, obj: int) -> int:
        length = len(self.table)
        index = obj % length

        position_checked = 1

        while self.table[index] != 0:
            if position_checked == (length - 1):
                return position_checked
            index = (obj + (position_checked * position_checked)) % length
            position_checked += 1

        self.table[index] = obj

        return position_checked

    def add_double_hashing(self, obj: int) -> int:
        length = len(self.table)
        index = obj % length

        position_checked = 1

        while self.table[index] != 0:
            if position_checked == (length - 1):
                return position_checked
            index = (obj + (h2(position_checked))) % length
            position_checked += 1
        self.table[index] = obj

        return position_checked


if __name__ == "__main__":
    linear = HashLinQuadDouble(capacity_)
    quadratic = HashLinQuadDouble(capacity_)
    double = HashLinQuadDouble(capacity_)

    print("Number      l_c    q_c    d_c")

    for i in range(1000):
        num = random.randint(1, 100000)
        linear_collision = linear.add_lin(num)
        quadratic_collision = quadratic.add_quad(num)
        double_collision = double.add_double_hashing(num)
        # print(num.__str__() + "       " + linear_collision.__str__() + 
        #  "      " + quadratic_collision.__str__() 
        # + "      " + double_collision.__str__())
