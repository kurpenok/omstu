#include <iostream>

void sort(int array[], int size) {
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

int main() {
    int size = 12;
    int array[size];

    std::cout << "[>] Enter array: ";
    for (int i = 0; i < size; i++) {
        std::cin >> array[i];
    }

    sort(array, size);

    return 0;
}
