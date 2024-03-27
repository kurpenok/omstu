from __future__ import annotations, unicode_literals

import enum
from types import resolve_bases
from typing import Any


class RBTNodeColor(enum.Enum):
    RED = "red"
    BLACK = "black"


class RBTNode:
    def __init__(
        self,
        key: Any,
        color: RBTNodeColor,
        parent: RBTNode = None,
        left: RBTNode = None,
        right: RBTNode = None,
    ) -> None:

        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RBTree:
    def __init__(self) -> None:
        self.root: RBTNode = None

    def print(self) -> None:
        pass

    def search(self, key: Any) -> None:
        pass

    def _left_rotate(self, x: RBTNode) -> None:
        y: RBTNode = x.right

        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, y: RBTNode) -> None:
        x: RBTNode = y.left

        y.left = x.right
        if x.right is not None:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.right:
                y.parent.right = x
            else:
                y.parent.left = x

        x.right = y
        y.parent = x

    def insert(self, key: Any) -> None:
        node: RBTNode = RBTNode(key, RBTNodeColor.RED, None, None, None)
        self._insert(node)

    def _insert(self, node: RBTNode) -> None:
        x: RBTNode = self.root
        y: RBTNode = None

        while x is not None:
            y = x
            if node.key > x.key:
                x = x.right
            else:
                x = x.left

        node.parent = y
        if y is not None:
            if node.key > y.key:
                y.right = node
            else:
                y.left = node
        else:
            self.root = node

        node.color = RBTNodeColor.RED
        self._insert_fix_up(node)

    def _insert_fix_up(self, node: RBTNode) -> None:
        parent: RBTNode = node.parent

        while node is not self.root and parent.color == RBTNodeColor.RED:
            gparent: RBTNode = parent.parent
            if gparent.left == parent:
                uncle: RBTNode = gparent.right
                if uncle is not None and uncle.color == RBTNodeColor.RED:
                    gparent.color = RBTNodeColor.RED
                    parent.color = RBTNodeColor.BLACK
                    uncle.color = RBTNodeColor.BLACK
                    node = gparent
                    parent = node.parent
                else:
                    if parent.right == node:
                        self._left_rotate(parent)
                        node, parent = parent, node
                    self._right_rotate(gparent)
                    gparent.color = RBTNodeColor.RED
                    parent.color = RBTNodeColor.BLACK
                    break
            else:
                uncle: RBTNode = gparent.left
                if uncle is not None and uncle.color == RBTNodeColor.RED:
                    gparent.color = RBTNodeColor.RED
                    parent.color = RBTNodeColor.BLACK
                    uncle.color = RBTNodeColor.BLACK
                    node = gparent
                    parent = node.parent
                else:
                    if parent.left == node:
                        self._right_rotate(parent)
                        parent, node = node, parent
                    self._left_rotate(gparent)
                    parent.color = RBTNodeColor.BLACK
                    gparent.color = RBTNodeColor.RED
                    break

        self.root.color = RBTNodeColor.BLACK

    def remove(self, key: Any) -> None:
        pass
