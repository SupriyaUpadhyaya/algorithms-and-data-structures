class DoublyLinkedNode:
    def __init__(self, item: int = None, prev: "DoublyLinkedNode | None" = None,
                 next: "DoublyLinkedNode | None" = None) -> None:
        self._item = item
        self._prev = prev
        self._next = next

    def get_item(self) -> int:
        return self._item

    def get_prev(self) -> "DoublyLinkedNode":
        return self._prev

    def get_next(self) -> "DoublyLinkedNode":
        return self._next

    def set_item(self, item: int) -> None:
        self._item = item
        return None

    def set_prev(self, prev: "DoublyLinkedNode") -> None:
        self._prev = prev
        return None

    def set_next(self, next: "DoublyLinkedNode") -> None:
        self._next = next
        return None


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = DoublyLinkedNode()
        self._tail = DoublyLinkedNode(prev=self._head)
        self._head.set_next(self._tail)
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def add_first(self, item: int) -> None:
        newnode = DoublyLinkedNode(item)
        if self.is_empty():
            newnode.set_prev(self._head)
            newnode.set_next(self._tail)
            self._tail.set_prev(newnode)
            self._head.set_next(newnode)
        else:
            n = self._head.get_next()
            newnode.set_prev(self._head)
            newnode.set_next(n)
            self._head.set_next(newnode)
            n.set_prev(newnode)
        self._size += 1
        return None

    def get_first(self) -> int:
        if self.is_empty():
            return None
        else:
            x = self._head.get_next()
            return x.get_item()

    def remove_first(self) -> int:
        if self.is_empty():
            return None
        a = self._head.get_next()
        out = a.get_item()
        b = a.get_next()
        self._head.set_next(a.get_next())
        b.set_prev(a.get_prev())
        self._size -= 1
        return out

    def add_last(self, item: int) -> None:
        newnode = DoublyLinkedNode(item)
        if self.is_empty():
            newnode.set_prev(self._head)
            newnode.set_next(self._tail)
            self._tail.set_prev(newnode)
            self._head.set_next(newnode)
        else:
            y = self._tail.get_prev()
            newnode.set_next(self._tail)
            newnode.set_prev(y)
            self._tail.set_prev(newnode)
            y.set_next(newnode)
        self._size += 1
        return None

    def get_last(self) -> int:
        if self.is_empty():
            return None
        x = self._tail.get_prev()
        return x.get_item()

    def remove_last(self) -> int:
        if self.is_empty():
            return None
        c = self._tail.get_prev()
        out = c.get_item()
        d = c.get_prev()
        self._tail.set_prev(d)
        d.set_next(c.get_next())
        self._size -= 1
        return out


if __name__ == "__main__":
    pass