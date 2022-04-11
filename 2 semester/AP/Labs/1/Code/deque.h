#pragma once

#include <cstddef>
#include <iostream>
#include "circular_buffer.h"
#include "page.h"

template <class T>
class Deque {
private:
    const static int kPageSize = 100;
    CircularBuffer<Page<T, kPageSize>*> buffer;
    size_t size;

public:
    Deque();
    Deque(const Deque<T>&);
    Deque<T>& operator=(const Deque<T>&);
    ~Deque();

    T operator[](size_t) const;
    T& operator[](size_t);

    void PushFront(T);
    void PushBack(T);
    void PopFront();
    void PopBack();

    size_t Size() const;
    void Swap(Deque<T>&);
    void Clear();
};

template <class T>
Deque<T>::Deque() {
    buffer = CircularBuffer<Page<T, kPageSize>*>();
    size = 0;
}

template <class T>
Deque<T>::Deque(const Deque<T>& other) {
    for (size_t i = 0; i < buffer.Size(); ++i) {
        auto page = new Page<T, kPageSize>;
        *page = *(other.buffer[i]);
        buffer.PushBack(page);
    }
    size = other.size;
}

template <class T>
Deque<T>& Deque<T>::operator=(const Deque<T> &other) {
   if (this != &other) {
        size_t buffer_size = buffer.Size();
        for (size_t i = 0; i < buffer_size; ++i) {
            delete buffer.Back();
            buffer.PopBack();
        }
        for (size_t i = 0; i < other.buffer.Size(); ++i) {
            auto page = new Page<T, kPageSize>;
            *page = *(other.buffer[i]);
            buffer.PushBack(page);
        }
        size = other.size;
   }
   return *this;
}

template <class T>
Deque<T>::~Deque() {
    size_t buffer_size = buffer.Size();
    for (size_t i = 0; i < buffer_size; ++i) {
        delete buffer.Back();
        buffer.PopBack();
    }
}

template <class T>
T Deque<T>::operator[](size_t index) const {
    if ((buffer.Front()->Full()) || (index < buffer.Front()->Size())) {
        return (*(buffer[index / kPageSize]))[index % kPageSize];
    }
    index -= buffer.Front()->Size();
    return (*(buffer[1 + index / kPageSize]))[index % kPageSize];
}

template <class T>
T& Deque<T>::operator[](size_t index) {
    if ((buffer.Front()->Full()) || (index < buffer.Front()->Size())) {
        return (*(buffer[index / kPageSize]))[index % kPageSize];
    }
    index -= buffer.Front()->Size();
    return (*(buffer[1 + index / kPageSize]))[index % kPageSize];
}

template <class T>
void Deque<T>::PushFront(T value) {
    if ((buffer.Size() == 0) || (buffer.Front()->Full())) {
        auto page = new Page<T, kPageSize>;
        buffer.PushFront(page);
    }
    buffer.Front()->PushFront(value);
    size++;
}

template <class T>
void Deque<T>::PushBack(T value) {
    if ((buffer.Size() == 0) || (buffer.Back()->Full())) {
        auto page = new Page<T, kPageSize>;
        buffer.PushBack(page);
    }
    buffer.Back()->PushBack(value);
    size++;
}

template <class T>
void Deque<T>::PopFront() {
    buffer.Front()->PopFront();
    if (buffer.Front()->Empty()) {
        delete buffer.Front();
        buffer.PopFront();
    }
    size--;
}

template <class T>
void Deque<T>::PopBack() {
    buffer.Back()->PopBack();
    if (buffer.Back()->Empty()) {
        delete buffer.Back();
        buffer.PopBack();
    }
    size--;
}

template <class T>
size_t Deque<T>::Size() const {
    return size;
}

template <class T>
void Deque<T>::Swap(Deque<T>& other) {
    buffer.Swap(other.buffer);
    size_t temp_size = size;
    size = other.size;
    other.size = temp_size;
}

template <class T>
void Deque<T>::Clear() {
    size_t buffer_size = buffer.Size();
    for (size_t i = 0; i < buffer_size; ++i) {
        delete buffer.Back();
        buffer.PopBack();
    }
    size = 0;
}

