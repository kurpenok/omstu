#include <iostream>
#include <cmath>

int main() {
    double r, square, value, relationship;

    std::cout << "[>] Enter R: ";
    std::cin >> r;

    square = M_PI * pow(r, 2);
    value = (4 * M_PI * pow(r, 3)) / 3;

    std::cout << "[+] Square: " << square << std::endl;
    std::cout << "[+] Value: " << value << std::endl;

    relationship = square / value;

    std::cout << "[+] Relationship: " << relationship << std::endl;

    return 0;
}
