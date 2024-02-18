#pragma once

#include <iostream>
#include <ostream>

template<class T>
class Card {
private:
    T data;

public:
    Card(T&);

    T getData();

    friend std::ostream& operator<<(std::ostream& s, Card<T> c);
};

template<class T>
Card<T>::Card(T& data) {
    this->data = data;
}

template<class T>
T Card<T>::getData() {
    return data;
}

template<class T>
std::ostream& operator<<(std::ostream& s, Card<T> c) {
    s << c.getData();
    return s;
}

