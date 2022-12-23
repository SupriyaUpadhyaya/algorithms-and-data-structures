from typing import Any, List, Optional

from icse_queue import Queue


class RandomQueue(Queue):
    # TODO: Implement the missing methods.

    def __init__(self) -> None:
        super().__init__()
        self.__queue: List[str] = []

    def __str__(self) -> str:
        output = ""
        for i in self.__queue:
            output = output + i + " , "
        return output

    def dequeue(self) -> Optional[Any]:
        """Remove and return one random item from the queue (or `None` if the queue is empty)."""
        length = len(self.__queue)
        if self.is_empty():
            return None
        else:
            d = self.__queue[length - 1]
            del self.__queue[length - 1]
            return d

    def sample(self) -> Optional[Any]:
        """Returns a random element from the queue (or `None` if the queue is empty)."""
        if self.is_empty():
            return None
        else:
            return self.__queue[0]

    def is_empty(self) -> bool:
        """Returns `True` if the queue contains no elements, `False` otherwise."""
        return len(self.__queue) == 0
    
    def enqueue(self, item: str) -> bool:
        """Adds `item` to the end of the queue. Return `True` for success."""
        self.__queue += [item]
        return True


if __name__ == "__main__":
    q1 = RandomQueue()
    print(q1.__str__())
    print(q1.sample())
    print(q1.is_empty())
    q1.enqueue("abc")
    print(q1.__str__())
    print(q1.is_empty())
    q1.enqueue("pqr")
    q1.enqueue("xyz")
    print(q1.__str__())
    print(q1.dequeue())
    print(q1.__str__())
    print(q1.sample())