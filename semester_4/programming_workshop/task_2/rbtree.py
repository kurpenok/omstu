from __future__ import annotations, unicode_literals

import enum
from typing import Any

import pygraphviz as pgv


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
        if self.root is None:
            print("[+] Red-Black tree is empty")
        else:
            self._print(self.root)

    def _print(self, node: RBTNode) -> None:
        if node is None:
            return

        if node.parent is None:
            print(f"[+] {node.key} ({node.color.value}) is root")
        elif node.parent.left == node:
            print(f"[+] {node.key} ({node.color}) is {node.parent.key}'s left child")
        else:
            print(f"[+] {node.key} ({node.color}) is {node.parent.key}'s right child")

        self._print(node.left)
        self._print(node.right)

    def search(self, key: Any) -> RBTNode:
        return self._search(self.root, key)

    def _search(self, node: RBTNode, key: Any) -> RBTNode:
        if node is None or node.key == key:
            return node
        elif key > node.key:
            return self._search(node.right, key)
        else:
            return self._search(node.left, key)

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
        to_delete_node: RBTNode = self.search(key)
        if to_delete_node is not None:
            self._remove(to_delete_node)

    def _remove(self, node: RBTNode) -> None:
        if node.left is not None and node.right is not None:
            replace: RBTNode = node.right

            while replace.left is not None:
                replace = replace.left

            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = replace
                else:
                    node.parent.right = replace
            else:
                self.root = replace

            child = replace.right
            parent = replace.parent
            color = replace.color

            if parent == node:
                parent = replace
            else:
                if child is not None:
                    child.parent = parent
                parent.left = child
                replace.right = node.right
                node.right.parent = replace
            replace.parent = node.parent
            replace.color = node.color
            replace.left = node.left
            node.left.parent = replace

            if color == RBTNodeColor.BLACK:
                self._remove_fix_up(child, parent)
            return

        if node.left is not None:
            child = node.left
        else:
            child = node.right

        parent = node.parent
        color = node.color
        if child:
            child.parent = parent

        if parent:
            if node == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child

        if color == RBTNodeColor.BLACK:
            self._remove_fix_up(child, parent)

    def _remove_fix_up(self, node: RBTNode, parent: RBTNode) -> None:
        while not node or node.color == RBTNodeColor.BLACK and node != self.root:
            if parent.left == node:
                othernode = parent.right
                if othernode.color == RBTNodeColor.RED:
                    othernode.color = RBTNodeColor.BLACK
                    parent.color = RBTNodeColor.RED
                    self._left_rotate(parent)
                    othernode = parent.right
                else:
                    if (
                        not othernode.right
                        or othernode.right.color == RBTNodeColor.BLACK
                    ):
                        othernode.left.color = RBTNodeColor.BLACK
                        othernode.color = RBTNodeColor.RED
                        self._right_rotate(othernode)
                        othernode = parent.right
                    othernode.color = parent.color
                    parent.color = RBTNodeColor.BLACK
                    othernode.right.color = RBTNodeColor.BLACK
                    self._left_rotate(parent)
                    node = self.root
                    break
            else:
                othernode = parent.left
                if othernode.color == RBTNodeColor.RED:
                    othernode.color = RBTNodeColor.BLACK
                    parent.color = RBTNodeColor.RED
                    self._right_rotate(parent)
                    othernode = parent.left
                if (
                    not othernode.left or othernode.left.color == RBTNodeColor.BLACK
                ) and (
                    not othernode.right or othernode.right.color == RBTNodeColor.BLACK
                ):
                    othernode.color = RBTNodeColor.RED
                    node = parent
                    parent = node.parent
                else:
                    if not othernode.left or othernode.left.color == RBTNodeColor.BLACK:
                        othernode.right.color = RBTNodeColor.BLACK
                        othernode.color = RBTNodeColor.RED
                        self._left_rotate(othernode)
                        othernode = parent.left
                    othernode.color = parent.color
                    parent.color = RBTNodeColor.BLACK
                    othernode.left.color = RBTNodeColor.BLACK
                    self._right_rotate(parent)
                    node = self.root
                    break

        if node:
            node.color = RBTNodeColor.BLACK

    def rbt_to_image(self) -> None:
        graph = pgv.AGraph()

        self._post_order(graph, self.root)

        graph.layout("dot")
        graph.draw("graph.jpg")

    def _post_order(self, graph: pgv.AGraph, node: RBTNode) -> None:
        graph.add_node(str(node.key))
        if node.color == RBTNodeColor.RED:
            graph.get_node(str(node.key)).attr["style"] = "filled"
            graph.get_node(str(node.key)).attr["fillcolor"] = "red"

        if node is not None:
            if node.left is not None:
                graph.add_edge(str(node.key), str(node.left.key))
                self._post_order(graph, node.left)
            if node.right is not None:
                graph.add_edge(str(node.key), str(node.right.key))
                self._post_order(graph, node.right)
