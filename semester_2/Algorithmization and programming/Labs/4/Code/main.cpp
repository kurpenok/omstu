#include <iostream>

#include "RedBlackTree.h"

int main() {
  RBTree<int> rbtree{};

  rbtree.insert(3);
  rbtree.insert(4);
  rbtree.insert(5);
  rbtree.insert(12);
  rbtree.insert(17);
  rbtree.print();

  std::cout << std::endl;
  rbtree.remove(12);
  rbtree.print();

  std::cout << std::endl;
  rbtree.remove(4);
  rbtree.print();

  return 0;
}
