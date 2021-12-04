#include <iostream>

#include "Vector.h"

int main() {
    setlocale(LC_ALL, "Russian");

    std::string text;

    std::cout << "[>] Enter text: ";
    std::cin >> text;

    Vector vector;

    for (char symbol: text) {
        vector.add(symbol);
    }

    vector.print();

    return 0;
}
