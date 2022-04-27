#pragma once

#include <vector>

#include "RedBlackTree.h"

template<class T>
void sort(std::vector<T>& a) {
    RBTree<T> rbtree;

    for (auto i: a) {
        rbtree.insert(i);
    }

    rbtree.sortPrint();
}

