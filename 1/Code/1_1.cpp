#include <iostream>
#include <cmath>

double f(double a, double b, double x) {
    double y = sqrt(std::abs(a * x * pow(sin(x), 2))) + (pow(M_E, -2 * x) * (x + b));
    return y;
}

int main() {
    double a, b, x1, x2;

    x1 = 1.0;
    x2 = 2.0;
    a = 0.5;
    b = 3.1;

    double y1 = f(a, b, x1);
    std::cout << "[+] F(" << a << ", " << b << ", " << x1 << "): " << y1 << std::endl;

    double y2 = f(a, b, x2);
    std::cout << "[+] F(" << a << ", " << b << ", " << x2 << "): " << y2 << std::endl;

    return 0;
}
