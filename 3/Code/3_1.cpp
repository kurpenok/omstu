#include <iostream>
#include <cmath>

int main() {
    double first_element = 4.0;
    double second_element = 0;

    for (int i = 0; i < 100; i++) {
        second_element += (pow(-1, i) / ((2 * i) + 1));
    }

    double pi = first_element * second_element;

    std::cout << "[+] Pi: " << pi << std::endl;

    return 0;
}
