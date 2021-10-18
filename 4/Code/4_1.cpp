#include <iostream>
#include <cmath>

double f_1(double a, double p, double x) {
    return tan(pow(a, 2) + sin(p * x));
}

double f_2(double a, double p, double x) {
    return a * sin(p - cos(p * x));
}

double f_3(double x) {
    return log10(x);
}

int main() {
    double x;
    double a = 0.5;
    double p = 0.75;
    double dx = a / 4;

    std::cout << "[+] Function 1: ";
    x = 0;
    while (x <= 1) {
        printf("(%.2f, %.2f)", x, f_1(a, p, x));
        x += dx;
    }
    std::cout << std::endl;

    std::cout << "[+] Function 2: ";
    x = 1;
    while (x <= 2) {
        printf("(%.2f, %.2f)", x, f_2(a, p, x));
        x += dx;
    }
    std::cout << std::endl;

    std::cout << "[+] Function 3: ";
    x = 2;
    while (x < 3) {
        printf("(%.2f, %.2f)", x, f_3(x));
        x += dx;
    }
    std::cout << std::endl;

    return 0;
}

