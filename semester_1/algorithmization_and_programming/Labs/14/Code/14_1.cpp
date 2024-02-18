#include <iostream>

#include "List.h"

int main() {
    setlocale(LC_ALL, "Russian");

    std::string text;

    std::cout << "[>] Enter text: ";
    std::cin >> text;

    List list;

    for (char symbol: text) {
        list.add(symbol);
    }

    list.print();

    return 0;
}
