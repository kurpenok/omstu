#include <iostream>
#include <cmath>

double f_1(double x) {
    double result = pow(M_E, -x) * log(sqrt(x + 1));
    return result;
}

double f_2(double x) {
    double result = x + sin(x);
    return result;
}
int main() {
    double start = 1;
    double stop = 2;
    double steps = 12;
    double value = 1;
    double step = (stop - start) / steps;

    double matrix[3][(int) steps];

    matrix[0][0] = value;
    matrix[1][0] = f_1(value);
    matrix[2][0] = f_2(value);

    for (int i = 1; i < steps; i++) {
        value += step;
        matrix[0][i] = value;
        matrix[1][i] = f_1(value);
        matrix[2][i] = f_2(value);
    }

    std::cout << "+------------+------------+------------+" << std::endl;
    std::cout << "|    Value   |    F(1)    |    F(2)    |" << std::endl;
    std::cout << "|------------+------------+------------|" << std::endl;
    for (int i = 0; i < steps; i++) {
        printf("|    %.2f    |    %.2f    |    %.2f    |\n", matrix[0][i], matrix[1][i], matrix[1][i]);
    }
    std::cout << "+------------+------------+------------+" << std::endl;

    return 0;
}
