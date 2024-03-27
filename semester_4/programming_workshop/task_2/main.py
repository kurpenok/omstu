#!/usr/bin/env python3


from rbtree import RBTree


def main() -> None:
    rbtree = RBTree()

    rbtree.insert(3)
    rbtree.insert(4)
    rbtree.insert(5)
    rbtree.insert(12)
    rbtree.insert(17)
    rbtree.print()
    rbtree.rbt_to_image()

    # rbtree.remove(4)
    # rbtree.remove(12)
    # rbtree.rbt_to_image()


if __name__ == "__main__":
    main()
