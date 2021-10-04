#include <iostream>

int main() {
    int array[12];
    for (int i = 0; i < 12; i++) {
        std::cout << "[>] Enter " << i + 1<< " element of array: ";
        std::cin >> array[i];
    }

    std::cout << "[+] Sorted array: ";
    for (int i: array) {
        if (i < 0) {
            std::cout << i << " ";
        }
    }
    for (int i: array) {
        if (i >= 0) {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}

