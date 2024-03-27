from __future__ import annotations

import enum
from typing import Any, Optional


class RBTNodeColor(enum.Enum):
    RED = "red"
    BLACK = "black"


class RBTNode:
    def __init__(
        self,
        key: Any,
        color: RBTNodeColor,
        parent: Optional[RBTNode] = None,
        left: Optional[RBTNode] = None,
        right: Optional[RBTNode] = None,
    ) -> None:

        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RBTree:
    def __init__(self) -> None:
        self.root: Optional[RBTNode] = None

    def print(self) -> None:
        pass

    def search(self, key: Any) -> None:
        pass

    def _left_rotate(self, x: RBTNode) -> None:
        pass

    def _right_rotate(self, y: RBTNode) -> None:
        pass

    def insert(self, key: Any) -> None:
        pass

    def remove(self, key: Any) -> None:
        pass
