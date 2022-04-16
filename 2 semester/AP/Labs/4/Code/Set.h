#pragma once

#include <cstddef>
#include <iostream>

template <typename T>
class SetIterator;

template <typename T>
class Set {
private:
    size_t size;

public:
    Set();
    Set(const Set&);
    Set<T>& operator=(const Set<T>&);
    ~Set();

    bool Empty() const;
    size_t Size() const;

    void Clear();
    Set& Insert();
    void Erase();
    void Swap(Set<T>& other);

    Set& operator+(Set<T>& other);
    Set& operator-(Set<T>& other);
};

template <class T>
Set<T>::Set() {
    size = 0;
}

template <class T>
Set<T>::Set(const Set<T>& other) {
    size = other.size;
}

template <class T>
Set<T>& Set<T>::operator=(const Set<T>& other) {
    size = other.size;
}

template <class T>
Set<T>::~Set<T>() {
    size = 0;
}

template <class T>
bool Set<T>::Empty() const {
    return size == 0;
}

template <class T>
size_t Set<T>::Size() const {
    return size;
}

template <class T>
void Set<T>::Clear() {
    size = 0;
}

template <class T>
Set<T>& Set<T>::Insert() {
    size++;
}

template <class T>
void Set<T>::Erase() {
    size--;
}

template <class T>
void  Set<T>::Swap(Set<T>& other) {
    size_t temp = size;
    size = other.size;
    other.size = temp;
}

template <class T>
Set<T>& Set<T>::operator+(Set<T> &other) {
    return *this;
}

template <class T>
Set<T>& Set<T>::operator-(Set<T> &other) {
    return *this;
}

