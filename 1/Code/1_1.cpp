#include <iostream>
#include <cmath>

int main() {
    double a, b, x1, x2, y1, y2;

    x1 = 1;
    x2 = 2;
    a = 0.5;
    b = 3.1;

    y1 = sqrt(std::abs(a * x1 * pow(sin(x1), 2))) + (pow(M_E, -2 * x1) * (x1 + b));
    std::cout << "[+] Y1: " << y1 << std::endl;

    y2 = sqrt(std::abs(a * x2 * pow(sin(x2), 2))) + (pow(M_E, -2 * x1) * (x2 + b));
    std::cout << "[+] Y2: " << y2 << std::endl;

    return 0;
}
