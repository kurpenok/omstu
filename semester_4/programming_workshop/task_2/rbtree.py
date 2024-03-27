from __future__ import annotations

import enum
from typing import Any


class RBTNodeColor(enum.Enum):
    RED = "red"
    BLACK = "black"


class RBTNode:
    def __init__(
        self,
        key: Any,
        color: RBTNodeColor,
        parent: RBTNode,
        left: RBTNode,
        right: RBTNode,
    ) -> None:

        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RBTree:
    def __init__(self) -> None:
        self.root: RBTNode

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
        pass

    def remove(self, key: Any) -> None:
        pass
