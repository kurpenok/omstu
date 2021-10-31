#include <iostream>
#include <cmath>

double f_1(double a, double x) {
    return tan(pow(a, 2) + sin(M_PI * x));
}

double f_2(double a, double x) {
    return a * sin(M_PI - cos(M_PI * x));
}

double f_3(double x) {
    return log10(x);
}

double f_cycle(double a) {
    double x = 0;
    double dx = a / 4;

    std::cout << "[+] Function 1: ";
    while (x <= 1) {
        printf("(%.2f, %.2f)", x, f_1(a, x));
        x += dx;
    }
    std::cout << std::endl;

    std::cout << "[+] Function 2: ";
    while (x <= 2) {
        printf("(%.2f, %.2f)", x, f_2(a, x));
        x += dx;
    }
    std::cout << std::endl;

    std::cout << "[+] Function 3: ";
    while (x < 3) {
        printf("(%.2f, %.2f)", x, f_3(x));
        x += dx;
    }
    std::cout << std::endl << std::endl;
}

int main() {
    f_cycle(0.5);
    f_cycle(0.75);
    f_cycle(1);

    return 0;
}

