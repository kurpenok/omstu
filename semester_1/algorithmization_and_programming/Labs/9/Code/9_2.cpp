#include <iostream>

void input(int* &array, int &size) {
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

int max(int* &array, int &size) {
    int m = array[0];

    for (int i = 0; i < size; i++) {
        if (m < array[i]) {
            m = array[i];
        }
    }
    return m;
}

int min(int* &array, int &size) {
    int m = array[0];

    for (int i = 0; i < size; i++) {
        if (m > array[i]) {
            m = array[i];
        }
    }
    return m;
}

int* sum(int* &array_1, int* &array_2, int &size) {
    int* array = new int [size];

    for (int i = 0; i < size; i++) {
        array[i] = array_1[i] + array_2[i];
    }
    return array;
}

int main() {
    int size;
    int* a;
    int* b;
    int* c;

    input(a, size);
    input(b, size);
    input(c, size);

    int z;

    int* bc = sum(b, c, size);

    if (min(a, size) < min(b, size)) {
        z = (max(b, size) / max(a, size)) + (max(c, size) / min(bc, size));
        std::cout << "[+] Z: " << z << std::endl;
    } else if (min(a, size) > min(b, size)) {
        z = max(bc, size) + min(c, size);
        std::cout << "[+] Z: " << z << std::endl;
    }

    return 0;
}
