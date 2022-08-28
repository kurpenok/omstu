#include <iostream>

#include "sort.h"

int main() {
    int size = 12;
    int* array = new int [12];

    std::cout << "[>] Enter array: ";
    for (int i = 0; i < size; i++) {
        std::cin >> array[i];
    }

    sort(array, size);

    return 0;
}
