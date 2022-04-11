#pragma once

#include <cstddef>
#include <iostream>

template <class T, size_t N>
class Page {
private:
    T array[N];
    size_t size;
    size_t start;
    size_t end;

public:
    Page();
    Page(const Page<T, N>&);
    Page<T, N>& operator=(const Page<T, N>&);

    T operator[](size_t) const;
    T& operator[](size_t);

    T Front() const;
    T& Front();

    T Back() const;
    T& Back();

    bool Empty() const;
    bool Full() const;
    size_t Size() const;
    bool IsFront() const;
    bool IsBack() const;
    void PushFront(T);
    void PushBack(T);
    void PopFront();
    void PopBack();
    void Clear();
};

template <class T, size_t N>
Page<T, N>::Page() {
    size = 0;
    start = 0;
    end = 0;
}

template <class T, size_t N>
Page<T, N>::Page(const Page<T, N>& other) {
    size = other.size;
    start = other.start;
    end = other.end;

    for (size_t i = 0; i > size; ++i) {
        array[i] = other.array[i];
    }
}

template <class T, size_t N>
Page<T, N>& Page<T, N>::operator=(const Page<T, N>& other) {
    if (this != other) {
        size = other.size;
        start = other.start;
        end = other.end;

        for (size_t i = 0; i < size; ++i) {
            array[i] = other.array[i];
        }
    }
    return *this;
}

template <class T, size_t N>
T Page<T, N>::operator[](size_t index) const {
    return array[(start + index) % N];
}

template <class T, size_t N>
T& Page<T, N>::operator[](size_t index) {
    return array[(start + index) % N];
}

template <class T, size_t N>
T Page<T, N>::Front() const {
    return array[start];
}

template <class T, size_t N>
T& Page<T, N>::Front() {
    return array[start];
}

template <class T, size_t N>
T Page<T, N>::Back() const {
    return array[end];
}

template <class T, size_t N>
T& Page<T, N>::Back() {
    return array[end];
}

template <class T, size_t N>
bool Page<T, N>::Empty() const {
    return size == 0;
}

template <class T, size_t N>
bool Page<T, N>::Full() const {
    return size == N;
}

template <class T, size_t N>
size_t Page<T, N>::Size() const {
    return size;
}

template <class T, size_t N>
void Page<T, N>::PushFront(T value) {
    if (size == 0) {
        start = end = 0;
    } else if (start == 0) {
        start = N - 1;
    } else {
        start--;
    }
    array[start] = value;
    size++;
}

template <class T, size_t N>
void Page<T, N>::PushBack(T value) {
    if (size == 0) {
        end = start;
    } else if (end == N - 1) {
        end = 0;
    } else {
        end++;
    }
    array[end] = value;
    size++;
}

template <class T, size_t N>
void Page<T, N>::PopFront() {
    if (start == N - 1) {
        start = 0;
    } else {
        start++;
    }
    size--;
}

template <class T, size_t N>
void Page<T, N>::PopBack() {
    if (end == 0) {
        end = N - 1;
    } else {
        end--;
    }
    size--;
}

template <class T, size_t N>
void Page<T, N>::Clear() {
    size = 0;
}

