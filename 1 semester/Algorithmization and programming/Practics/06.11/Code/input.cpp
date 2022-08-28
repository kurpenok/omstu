#include <iostream>

void input(int *array, int &size) {
    std::cout << "[>] Enter array: ";
    for (int i = 0; i < size; i++) {
        std::cin >> array[i];
    }
}
