#include <iostream>
#include <vector>

template <class T> class DequeIterator;

template <typename T>
class Deque {
    protected:
        std::vector<T> vector_1;
        std::vector<T> vector_2;

    public:
        typedef DequeIterator<T> iterator;

        Deque(): vector_1(), vector_2() {}
        Deque(unsigned int size, T& initial):
            vector_1(size / 2, initial), vector_2(size - (size / 2), initial) {}
        Deque(Deque<T>& deque):
            vector_1(deque.vector_1), vector_2(deque.vector_2) {}

        T& operator[](unsigned int);
        T& front();
        T& back();
        
        bool empty() {
            return vector_1.empty() && vector_2.empty();
        }

        iterator begin() {
            return iterator(this, 0);
        }
        iterator end() {
            return iterator(this, size());
        }

        void erase(const iterator&);
        void erase(const iterator&, const iterator&);
        void erase(const iterator&, const T&);
        int size() {
            return vector_1.size() + vector_2.size();
        }
        void push_front(const T& value) {
            vector_1.push_back(value);
        }
        void push_back(const T& value) {
            vector_2.push_back(value);
        }
        void pop_front();
        void pop_back();
    };

template <class T>
T& Deque<T>::front() {
    if (vector_1.empty()) {
        return vector_2.front();
    } else {
        return vector_1.back();
    }
}

template <class T>
T& Deque<T>::back() {
    if (vector_1.empty()) {
        return vector_2.back();
    } else {
        return vector_1.front();
    }
}

template <class T>
T& Deque<T>::operator[](unsigned int index) {
    int n = vector_1.size();

    if (index < n) {
        return vector_1[(n - 1)- index];
    } else {
        return vector_2[index - n];
    }
}

template <class T>
T& Deque<T>::iterator DequeIterator<T>::operator++(int) {
    Deque<T>::iterator clone(theDeque, index);
    index++;
    return clone;
}

template <class T>
void Deque<T>::erase(const iterator& it) {
    int index = it.index;
    int n = vector_1.size();
    
    if (index < n) {
        vector_1.erase(vector_1.begin() + ((n - 1) - index));
    } else {
        vector_2.erase(vector_2.begin() + (n - index));
    }
}

int main() {
    return 0;
}

