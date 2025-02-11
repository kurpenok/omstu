from typing import Any

from node import TreeNode, TreeNodeColor, is_red


class RedBlackTree:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def print(self) -> None:
        if self.root is None:
            print("[+] Red-Black tree is empty!")
        else:
            self._print(self.root)

    def search(self, key: Any) -> TreeNode | None:
        return self._search(key, self.root)

    def insert(self, key: Any) -> None:
        node: TreeNode = TreeNode(key)
        self._insert(node)

        if self.root is not None:
            self.root.color = TreeNodeColor.BLACK

    def remove(self, key: Any) -> None:
        node: TreeNode | None = self.search(key)
        if node is not None:
            self._remove(node)

    def _left_rotate(self, x: TreeNode) -> None:
        if x.right is None:
            raise Exception("[-] On turning left - node right child must be exist!")

        y: TreeNode = x.right

        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            raise Exception("[-] Error when exchange parents on turning left!")
        y.left = x
        x.parent = y

        y.color = x.color
        x.color = TreeNodeColor.RED

    def _right_rotate(self, y: TreeNode) -> None:
        if y.left is None:
            raise Exception("[-] On turning right - node left child must be exist!")

        x: TreeNode = y.left

        y.left = x.right
        if x.right is not None:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            raise Exception("[-] Error when exchange parents on turning right!")
        x.right = y
        y.parent = x

        x.color = y.color
        y.color = TreeNodeColor.RED

    def _swap_colors(self, node: TreeNode, left: TreeNode, right: TreeNode) -> None:
        node.color = TreeNodeColor.RED
        left.color = TreeNodeColor.BLACK
        right.color = TreeNodeColor.BLACK

    def _print(self, node: TreeNode | None) -> None:
        if node is None:
            return

        if node.parent is None:
            print(f"{node.key} ({node.color.value}) is root")
        elif node == node.parent.left:
            print(f"{node.key} ({node.color.value}) is left child {node.parent.key}")
        elif node == node.parent.right:
            print(f"{node.key} ({node.color.value}) is right child {node.parent.key}")
        else:
            raise Exception("[-] Undefined error in tree output!")

        self._print(node.left)
        self._print(node.right)

    def _search(self, key: Any, node: TreeNode | None) -> TreeNode | None:
        if node is None or key == node.key:
            return node
        elif key < node.key:
            return self._search(key, node.left)
        elif key > node.key:
            return self._search(key, node.right)
        else:
            raise Exception("[-] Undefined error when searching node!")

    def _insert(self, node: TreeNode) -> None:
        current: TreeNode | None = self.root
        parent: TreeNode | None = None

        while current is not None:
            parent = current
            if node.key == current.key:
                print("[+] Key already exist!")
                return
            elif node.key < current.key:
                current = current.left
            elif node.key > current.key:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        elif node.key > parent.key:
            parent.right = node
        else:
            raise Exception("[-] Undefined error when adding node!")

        self._insert_fix_up(node)

    def _insert_fix_up(self, node: TreeNode) -> None:
        current: TreeNode = node

        while True:
            if is_red(current.right) and not is_red(current.left):
                self._left_rotate(current)
            elif (
                current.left is not None
                and is_red(current.left)
                and is_red(current.left.left)
            ):
                self._right_rotate(current)
            elif (
                current.left is not None
                and current.right is not None
                and is_red(current.left)
                and is_red(current.right)
            ):
                self._swap_colors(current, current.left, current.right)
            elif current.parent is not None:
                current = current.parent
            else:
                break

    def _remove(self, node: TreeNode) -> None:
        pass
