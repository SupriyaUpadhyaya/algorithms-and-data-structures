from binary_tree import BinaryTree


class MyBinaryTree(BinaryTree):
    def height(self) -> int:
        """Returns the height of this tree."""
        def _height(node):
            if node is None:
                return 0
            left_tree_height = _height(node.get_left())
            right_tree_height = _height(node.get_right())
            return 1 + max(left_tree_height, right_tree_height)
        return _height(self)

    def tree_sum(self, tree) -> int:
        curr_level = [tree]
        sum = 0
        if tree is not None:
            while len(curr_level) > 0:
                node = curr_level[0]
                curr_level.pop(0)
                if node._left is not None:
                    curr_level.append(node.get_left())
                if node._right is not None:
                    curr_level.append(node.get_right())
                sum += node.get_item()
        return sum

    def max_sum(self) -> int:
        """Returns the maximum sum of the left and right sub-tree."""
        return max(self.tree_sum(self.get_left()), self.tree_sum(self.get_right()))

    def max_path(self) -> int:
        self.max_path_sum = self.get_root().get_item()

        def _max_path(node):
            if node is None:
                return 0
            node_item = node.get_item()
            node_left = _max_path(node._left)
            node_right = _max_path(node._right)
            self.max_path_sum = max(
                self.max_path_sum, node_item + node_left + node_right)
            return max(node_item + node_left, node_item + node_right)

        result = _max_path(self.get_root())
        return result

    def max_width(self) -> int:
        max_Width = 0
        nodes = 0
        curr_level = []
        if (self.get_root().get_item() is None):
            return 0
        else:
            curr_level.append(self.get_root())
            while (len(curr_level) != 0):
                nodes = len(curr_level)
                max_Width = max(max_Width, nodes)
                while (nodes > 0):
                    current = curr_level.pop(0)
                    if (current.get_left() != None):
                        curr_level.append(current.get_left())
                    if (current.get_right() != None):
                        curr_level.append(current.get_right())
                    nodes = nodes - 1
        return max_Width


if __name__ == "__main__":
    r2 = MyBinaryTree(88)
    r1 = MyBinaryTree(21, right=r2)
    l1 = MyBinaryTree(58, left=r1)
    tree = MyBinaryTree(0, right=l1)
    print(tree.height())
    print(tree.max_sum())
    print(tree.max_path())
    print(tree.max_width())