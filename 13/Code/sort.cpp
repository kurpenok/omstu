#include <iostream>

#include "sort.h"

void sort(int*& array, int& size) {
    std::cout << "[+] Sorted array: ";
    for (int i = 0; i < size; i++) {
        if (array[i] < 0) {
            std::cout << array[i] << " ";
        }
    }
    for (int i = 0; i < size; i++) {
        if (array[i] >= 0) {
            std::cout << array[i] << " ";
        }
    }
    std::cout << std::endl;
}
