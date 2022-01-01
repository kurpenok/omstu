#include <iostream>

#include "input.h"
#include "sum.h"
#include "count.h"

int main() {
    int size = 0;
    std::cout << "[>] Enter size: ";
    std::cin >> size;

    int *array = new int[size];

    input(array, size);

    std::cout << "[+] Sum of negative elements: " << sum(array, size) << std::endl;
    std::cout << "[+] Count of odd elements: " << count(array, size) << std::endl;
}
