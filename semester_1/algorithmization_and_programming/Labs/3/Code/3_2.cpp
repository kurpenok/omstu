#include <iostream>
#include <cmath>

double f_1(double x) {
    double result = pow(M_E, -x) * log10(sqrt(x + 1));
    return result;
}

double f_2(double x) {
    double result = x + sin(x);
    return result;
}
int main() {
    double start = 1;
    double stop = 2;
    double steps = 11;
    double value = 1;
    double step = (stop - start) / steps;

    std::cout << "+------------+------------+------------+" << std::endl;
    std::cout << "|    Value   |    F(1)    |    F(2)    |" << std::endl;
    std::cout << "|------------+------------+------------|" << std::endl;
    for (int i = 0; i <= steps; i++) {
        printf("|    %.2f    |    %.2f    |    %.2f    |\n", value, f_1(value), f_2(value));
        value += step;
    }
    std::cout << "+------------+------------+------------+" << std::endl;

    return 0;
}
