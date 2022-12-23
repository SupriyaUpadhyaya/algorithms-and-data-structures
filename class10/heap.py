from typing import TypeVar, List

T = TypeVar('T')


class MaxHeap:
    def __init__(self, arr: List[T]) -> None:
        self.contents = arr
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
        self.float(len(self.contents)-1)

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
        self.sink(0)
        self.contents = self.contents[:-1]
        return to_return

    def sink(self, n: int) -> None:
        while 2 * n + 1 <= len(self.contents) - 1:
            child = 2 * n + 1
            if child < (len(self.contents) - 1):
                if self.contents[child] > self.contents[child + 1]:
                    child = child + 1
            if self.contents[n] <= self.contents[child]:
                break
            self.contents[n], self.contents[child] = self.contents[child], self.contents[n]
            n = child

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
    a1 = [2, 1, 2]
    print(f"Creating heap from {a1}")
    heap = MaxHeap(a1)
    for i in heap.contents:
        print(i)
    heap.remove()
    print("========")
    for i in heap.contents:
        print(i)