#pragma once

#include <cstddef>
#include <functional>
#include <iostream>

#include "RedBlackTree.h"

template <class Key, class Compare = std::less<Key>>
class Set {
public:
    Set();
    Set(const Set<Key>&);
    Set<Key>& operator=(const Set<Key>&);
    ~Set();
    
    bool Empty() const;
    size_t Size() const;

    void Clear();
    void Insert(const Key&);
    void Erase(const Key&);

    bool Find(const Key&);

private:
    RBTree<Key> rbtree_;
    size_t size_;
};

template <class Key, class Compare>
Set<Key, Compare>::Set() {}

template <class Key, class Compare>
Set<Key, Compare>::Set(const Set<Key>& other) {
    rbtree_ = other.rbtree_;
    size_ = other.size_;
}

template <class Key, class Compare>
Set<Key>& Set<Key, Compare>::operator=(const Set<Key> &other) {
    rbtree_ = other.rbtree_;
    size_ = other.size_;
}

template <class Key, class Compare>
Set<Key, Compare>::~Set() {
    delete rbtree_;
}

template <class Key, class Compare>
bool Set<Key, Compare>::Empty() const {
    return size_ == 0;
}

template <class Key, class Compare>
size_t Set<Key, Compare>::Size() const {
    return size_;
}

template <class Key, class Compare>
void Set<Key, Compare>::Clear() {
    rbtree_ = nullptr;
    size_ = 0;
}

template <class Key, class Compare>
void Set<Key, Compare>::Insert(const Key& key) {
    rbtree_.insert(key);
}

template<class Key, class Compare>
void Set<Key, Compare>::Erase(const Key& key) {
    rbtree_.remove(key);
}

template<class Key, class Compare>
bool Set<Key, Compare>::Find(const Key &key) {
    return rbtree_.search(key);
}

