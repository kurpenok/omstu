#pragma once

#include <cstddef>
#include <iostream>

template <typename T>
class SetIterator;

template <typename T>
class Set {
private:

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
Set<T>::Set() {}

template <class T>
Set<T>::Set(const Set<T>& other) {}

template <class T>
Set<T>& Set<T>::operator=(const Set<T>& other) {}

template <class T>
Set<T>::~Set<T>() {}

template <class T>
bool Set<T>::Empty() const {}

template <class T>
size_t Set<T>::Size() const {}

template <class T>
void Set<T>::Clear() {}

template <class T>
Set<T>& Set<T>::Insert() {}

template <class T>
void Set<T>::Erase() {}

template <class T>
void  Set<T>::Swap(Set<T>& other) {}

template <class T>
Set<T>& Set<T>::operator+(Set<T> &other) {}

template <class T>
Set<T>& Set<T>::operator-(Set<T> &other) {}

