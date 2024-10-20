#!/usr/bin/env python3


from rbtree import RedBlackTree


def main() -> None:
    rbtree = RedBlackTree()

    rbtree.insert(3)
    rbtree.insert(0)
    rbtree.insert(-3)
    rbtree.print()


if __name__ == "__main__":
    main()
