from typing import TypeVar, List

T = TypeVar('T')


class MaxHeap:
    def __init__(self, arr: List[T]) -> None:
        self.contents = arr
        for i in self.contents:
            print(i)
        if self.contents is not None:
            self.heapify()

    def __len__(self) -> int:
        return len(self.contents)

    def get_heap(self) -> List[T]:
        return self.contents

    def is_empty(self) -> bool:
        if self.__len__ == 0:
            return False
        else:
            return True

    def insert(self, obj: T) -> None:
        self.contents.append(obj)
        self.float(len(self.contents) - 1)

    def float(self, n: int) -> None:
        to_shift: T = self.contents[n]
        parent = (n - 1) // 2
        while n > 0 and to_shift < self.contents[parent]:
            self.contents[n] = self.contents[parent]
            n = parent
            parent = (n - 1) // 2

    def remove(self) -> T:
        to_return: T = self.contents[0]
        self.contents[0] = self.contents[self.__len__() - 1]
        self.contents = self.contents[:-1]
        self.sink(0)
        return to_return

    def sink(self, n: int) -> None:
        while n <= len(self.contents) - 1:
            new = n
            if (2 * n + 2) <= (len(self.contents) - 1):
                if self.contents[2 * n + 1] > self.contents[2 * n + 2]:
                    if self.contents[2 * n + 1] > self.contents[n]:
                        self.contents[n], self.contents[2 * n + 1] = self.contents[2 * n + 1], self.contents[n]
                        new = 2 * n + 1
                else:
                    if self.contents[2 * n + 2] > self.contents[n]:
                        self.contents[n], self.contents[2 * n + 2] = self.contents[2 * n + 2], self.contents[n]
                        new = 2 * n + 2
            elif (2 * n + 1) <= (len(self.contents) - 1) and (2 * n + 2) >= (len(self.contents) - 1):
                if self.contents[2 * n + 1] > self.contents[n]:
                    self.contents[n], self.contents[2 * n + 1] = self.contents[2 * n + 1], self.contents[n]
                    new = 2 * n + 1
            if new == n:
                n = len(self.contents)
            else:
                n = new

    def heapify(self) -> None:
        last_interval_index = len(self.contents) - 1
        for i in range(last_interval_index, -1, -1):
            self.sink(i)


if __name__ == "__main__":
    array = list("XTOGSMNAERAI")
    h = MaxHeap(array)
    print(h.__len__())
    for i in h.get_heap():
        print(i)
    print("=======")
    h.remove()
    for i in h.get_heap():
        print(i)
    print("======")
    arr = list("1234")
    heap = MaxHeap(arr)
    for i in heap.get_heap():
        print(i)

