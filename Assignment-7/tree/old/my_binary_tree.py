from argparse import OPTIONAL
from typing import Optional
from binary_tree import BinaryTree


class MyBinaryTree(BinaryTree):
    def __init__(self, item: int, left: "OPTIONAL[BinaryTree]" = None, right: "Optional[BinaryTree]" = None) -> None:
        super().__init__(item, left, right)
    
    def get_item(self) -> int:
        return self._item
        
    def height(self) -> int:
        """Returns the height of this tree."""
        if self.get_parent() is None:
            return 0
        elif (self.get_left() and self.get_right()) is not None:
            return 1 + max(self.get_left().height(), self.get_right().height())
        elif self.get_left() is not None:
            return 1 + self.get_left().height()
        elif self.get_right() is not None:
            return 1 + self.get_right().height()
        else:
            return 1

    def max_sum(self) -> int:
        sum = 0
        """Returns the maximum sum of the left and right sub-tree."""
        if self.get_left() and self.get_right() is not None:
            sum += self.get_item() + self.get_left().max_sum() + self.get_right().max_sum()
        elif self.get_right() is not None:
            sum += self.get_item() + self.get_right().max_sum()
        elif self.get_left() is not None:
            sum += self.get_item() + self.get_left().max_sum()
        else:
            sum += self.get_item()
        return sum

    def max_path(self) -> int:
        """Returns the value of the biggest path from self to a leaf."""
        raise NotImplementedError()  # TODO: Add implementation        

    def max_width(self) -> int:
        """Returns the value of the biggest level."""
        raise NotImplementedError()  # TODO: Add implementation

if __name__ == "__main__":
    tree = MyBinaryTree(-8, MyBinaryTree(4), MyBinaryTree(1))
    tree.get_left().set_left(MyBinaryTree(6))
    tree.get_left().get_left().set_left(MyBinaryTree(10))
    tree.get_left().set_right(MyBinaryTree(-1))
    tree.get_right().set_left(MyBinaryTree(5))
    tree.get_right().set_right(MyBinaryTree(7))

    print(tree.get_item())
    print(tree.get_left().get_item())
    print(tree.get_right().get_item())
    print(tree.get_parent())
    print("Height:")
    print(tree.height())
    print(tree.get_right().height())
    print(tree.get_left().height())
    print("item")
    print(tree.get_left().get_item() + 2)
    print("Max sum:")
    print(tree.max_sum())
    print(tree.get_right().max_sum())
    print(tree.get_left().max_sum())
    print("max path:")

    tree1 = MyBinaryTree(item=0, right=MyBinaryTree(46))
    print(tree1.get_item())
    #print(tree1.get_left().get_item())
    print(tree1.get_right().get_item())
    print(tree1.get_parent())
    print(tree1.get_right().height())