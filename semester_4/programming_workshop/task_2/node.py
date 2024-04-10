from __future__ import annotations

from enum import Enum
from typing import Any


class TreeNodeColor(Enum):
    RED = "red"
    BLACK = "black"


class TreeNode:
    def __init__(
        self,
        key: Any,
        parent: TreeNode | None = None,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
        color: TreeNodeColor = TreeNodeColor.RED,
    ) -> None:
        self.key: Any = key
        self.parent: TreeNode | None = parent
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right
        self.color: TreeNodeColor = color

    def is_red(self) -> bool:
        return self.color == TreeNodeColor.RED
