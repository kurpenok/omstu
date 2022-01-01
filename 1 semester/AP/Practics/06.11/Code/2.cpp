#include <iostream>

void input(int *array, int &size) {
    std::cout << "[>] Enter size: ";
    std:: cin >> size;

    std::cout << "[>] Enter array: ";
    for (int i = 0; i < size; i++) {
        std::cin >> array[i];
    }
}

double sum(const int *array, int &size) {
    double s = 0;
    for (int i = 0; i < size; i++) {
        if (array[i] > 0) {
            s += array[i];
        }
    }
    return s;
}

double count(const int *array, int &size) {
    double c = 0;
    for (int i = 0; i < size; i++) {
        if (array[i] > 0) {
            c++;
        }
    }
    return c;
}

int main() {
    int array_1[100];
    int size_1 = 0;

    int array_2[100];
    int size_2 = 0;

    input(array_1, size_1);
    input(array_2, size_2);

    double s_1 = sum(array_1, size_1);
    double c_1 = count(array_1, size_1);

    double s_2 = sum(array_2, size_2);
    double c_2 = count(array_1, size_1);

    std::cout << "[+] Average: " << (s_1 + s_2) / (c_1 + c_2) << std::endl;

    return 0;
}
