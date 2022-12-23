class DoublyLinkedNode:
    def __init__(
        self,
        item: int = None,
        prev: "DoublyLinkedNode | None" = None,
        next: "DoublyLinkedNode | None" = None
    ) -> None:
        self._item = item
        self._prev = prev
        self._next = next

    def get_item(self) -> Any:
        return self._item

    def get_next(self) -> Any:
        return self._next

    def get_prev(self) -> Any:
        return self._prev

    def set_item(self, item: Any) -> Any:
        self._item = item

    def set_next(self, next: Any) -> Any:
        self._next = next

    def set_prev(self, prev: Any) -> Any:
        self._prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = DoublyLinkedNode()
        self._tail = DoublyLinkedNode(prev=self._head)
        self._head.set_next(self._tail)
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return (self._size == 0)

    def add_first(self, item: int) -> None:
        if (self.is_empty):
            self._head = DoublyLinkedNode(item, None, None)
            self._head = self._tail
        self._size += 1

    def get_first(self) -> int | None:
        if self.is_empty:
            return None
        else:
            return self._head.get_item()
    
    def remove_first(self) -> int | None:
        if self.is_empty:
            return None
        out = self._head.get_item()
        self._head = self._head.get_next()
        self._head.get_prev = None
        _size -= 1
        return out

    def add_last(self, item: int) -> None:
        if (self.is_empty):
            self._head = DoublyLinkedNode(item, self._head.get_prev, None)
            self._head = self._tail
        self._size += 1
        
        


if __name__ == "__main__":
    pass