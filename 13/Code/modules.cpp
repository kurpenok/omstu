#include <iostream>

#include "modules.h"

void input(int*& array, int& size) {
    std::cout << "[>] Enter size of array: ";
    std::cin >> size;
    std::cout << std::endl;

    array = new int [size];

    std::cout << "[>] Enter array: ";
    for (int i = 0; i < size; i++) {
        std::cin >> array[i];
    }
    std::cout << std::endl;
}

int max(int*& array, int& size) {
    int m = array[0];

    for (int i = 0; i < size; i++) {
        if (m < array[i]) {
            m = array[i];
        }
    }
    return m;
}

int min(int*& array, int& size) {
    int m = array[0];

    for (int i = 0; i < size; i++) {
        if (m > array[i]) {
            m = array[i];
        }
    }
    return m;
}

int* sum(int*& array_1, int*& array_2, int& size) {
    int* array = new int [size];

    for (int i = 0; i < size; i++) {
        array[i] = array_1[i] + array_2[i];
    }
    return array;
}
