#include <iostream>
#include <cmath>

double f(double a, double b, double x) {
    double result = sqrt(std::abs(a * x * pow(sin(x), 2))) + (pow(M_E, -2 * x) * (x + b));
    return result;
}

int main() {
    double a, b, x1, x2;

    x1 = 1.0;
    x2 = 2.0;
    a = 0.5;
    b = 3.1;

    std::cout << "[+] F(" << a << ", " << b << ", " << x1 << "): " << f(a, b, x1) << std::endl;

    std::cout << "[+] F(" << a << ", " << b << ", " << x2 << "): " << f(a, b, x2) << std::endl;

    return 0;
}
