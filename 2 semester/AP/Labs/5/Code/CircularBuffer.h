#pragma once

#include <cstddef>
#include <iostream>

template <class T>
class CircularBuffer {
private:
    T* buffer;
    size_t size;
    size_t capacity;
    size_t start;
    size_t end;

public:
    CircularBuffer();
    explicit CircularBuffer(size_t);
    CircularBuffer(const CircularBuffer<T>&);
    CircularBuffer<T>& operator=(const CircularBuffer<T>&);
    ~CircularBuffer();

    T operator[](size_t) const;
    T& operator[](size_t);

    T Front() const;
    T& Front();
    T Back() const;
    T& Back();

    bool Empty() const;
    size_t Size() const;
    size_t Capacity() const;

    void PushFront(T);
    void PushBack(T);
    void PopFront();
    void PopBack();
    void Clear();
    void Reserve(size_t);
    void Swap(CircularBuffer<T>&);
    T* CopyOldBuffer();
};

template <class T>
CircularBuffer<T>::CircularBuffer() {
    buffer = nullptr;
    start = 0;
    end = 0;
    size = 0;
    capacity = 0; 
}

template <class T>
CircularBuffer<T>::CircularBuffer(size_t cap) {
    buffer = nullptr;
    start = 0;
    end = 0;
    size = 0;
    capacity = 0;
    if (cap > 0) {
        buffer = new T[cap];
        capacity = cap;
    }
}

template <class T>
void CopyBuffer(T* first_buffer, T* second_buffer, size_t start_index, size_t end_index) {
    size_t min_index = (start_index < end_index) ? start_index : end_index;
    size_t max_index = (start_index > end_index) ? start_index : end_index;
    for (size_t i = min_index; i <= max_index; ++i) {
        first_buffer[i] = second_buffer[i];
    }
}

template <class T>
T* CircularBuffer<T>::CopyOldBuffer() {
    T* new_buffer = new T[2 * capacity];
    for (size_t i = 0; i < size; ++i) {
        new_buffer[i] = (*this)[i];
    }
    return new_buffer;
}

template <class T>
CircularBuffer<T>::CircularBuffer(const CircularBuffer<T>& other) {
    buffer = nullptr;
    start = 0;
    end = 0;
    size = 0;
    capacity = 0;
    if (other.capacity) {
        buffer = new T[other.capacity];
        start = other.start;
        end = other.end;
        size = other.size;
        capacity = other.capacity;
        CopyOldBuffer(buffer, other.buffer, start, end);
    }
}

template <class T>
CircularBuffer<T>& CircularBuffer<T>::operator=(const CircularBuffer<T>& other) {
    if (this != &other) {
        T* old_buffer = buffer;
        buffer = nullptr;
        start = 0;
        end = 0;
        size = 0;
        capacity = 0;
        if (other.capacity > 0) {
            buffer = new T[other.capacity];
            start = other.start;
            end = other.end;
            size = other.size;
            capacity = other.capacity;
            CopyBuffer(buffer, other.buffer, start, end);
            delete[] old_buffer;
        }
    }
    return  *this;
}

template <class T>
CircularBuffer<T>::~CircularBuffer() {
    delete [] buffer;
}

template <class T>
T CircularBuffer<T>::operator[](size_t index) const {
    return buffer[(start + index) % capacity];
}

template <class T>
T& CircularBuffer<T>::operator[](size_t index) {
    return buffer[(start + index) % capacity];
}

template <class T>
T CircularBuffer<T>::Front() const {
    return buffer[start];
}

template <class T>
T& CircularBuffer<T>::Front() {
    return buffer[start];
}

template <class T>
T CircularBuffer<T>::Back() const {
    return buffer[end];
}

template <class T>
T& CircularBuffer<T>::Back() {
    return buffer[end];
}

template <class T>
bool CircularBuffer<T>::Empty() const {
    return size == 0;
}

template <class T>
size_t CircularBuffer<T>::Size() const {
    return size;
}

template <class T>
size_t CircularBuffer<T>::Capacity() const {
    return capacity;
}

template <class T>
void CircularBuffer<T>::PushFront(T value) {
    if (capacity == 0) {
        buffer = new T[1];
        start = 0;
        end = 0;
        capacity = 1;
    } else if (size == capacity) {
        T* old_buffer = buffer;
        T* new_buffer = CopyOldBuffer();
        buffer = new_buffer;
        delete[] old_buffer;
        capacity *= 2;
        start = capacity - 1;
        end = size - 1;
    } else if (start == 0) {
        start = capacity - 1;
    } else if (size == 0) {
        start = 0;
    } else {
        start--;
    }
    buffer[start] = value;
    size++;
}

template <class T>
void CircularBuffer<T>::PushBack(T value) {
    if (capacity == 0) {
        buffer = new T[1];
        start = 0;
        end = 0;
        capacity = 1;
    } else if (size == capacity) {
        T* old_buffer = buffer;
        T* new_buffer = CopyOldBuffer();
        buffer = new_buffer;
        delete[] old_buffer;
        capacity *= 2;
        start = 0;
        end = size;
    } else if (end == capacity - 1) {
        end = 0;
    } else if (size == 0) {
        end = start;
    } else {
        end++;
    }
    buffer[end] = value;
    size++;
}

template <class T>
void CircularBuffer<T>::PopFront() {
    if (start == capacity - 1) {
        start = 0;
    } else {
        start++;
    }
    size--;
}

template <class T>
void CircularBuffer<T>::PopBack() {
    if (end == 0) {
        end = capacity - 1;
    } else {
        end--;
    }
    size--;
}

template <class T>
void CircularBuffer<T>::Clear() {
    start = 0;
    end = 0;
    size = 0;
}

template <class T>
void CircularBuffer<T>::Reserve(size_t cap) {
    T* old_buffer = buffer;
    buffer = nullptr;
    start = 0;
    end = 0;
    if (cap > 0) {
        buffer = new T[cap];
        if (size != 0) {
            buffer = CopyOldBuffer();
            start = 0;
            end = size - 1;
        }
    }
    capacity = cap;
    delete[] old_buffer;
}

template <class T>
void SwapValues(T& first_value, T& second_value) {
    T temp = first_value;
    first_value = second_value;
    second_value = temp;
}

template <class T>
void CircularBuffer<T>::Swap(CircularBuffer<T>& other) {
    if (this == &other) {
        return;
    }
    SwapValues(buffer, other.buffer);
    SwapValues(start, other.start);
    SwapValues(end, other.end);
    SwapValues(size, other.size);
    SwapValues(capacity, other.capacity);
}

