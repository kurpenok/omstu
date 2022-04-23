#pragma once

#include <functional>
#include <iostream>

#include "RedBlackTree.h"

template <class Key, class Compare = std::less<Key>>
class Set {
public:
    struct Iterator {};

    Set();
    Set(const Set<Key>&);
    Set<Key>& operator=(const Set<Key>&);
    ~Set();
    
    Iterator Begin();
    Iterator End();

    bool Empty() const;
    size_t Size() const;

    void Clear();
    Iterator Insert(const Key&);
    void Erase();

    Iterator Find(const Key&);

private:
    RBTree<Key> rbtree_;
    size_t size;
};

