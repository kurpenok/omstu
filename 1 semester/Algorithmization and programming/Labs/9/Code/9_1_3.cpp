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

void calc(double** &matrix, int &row, int &column, double &value, double &step, double &stop) {
    matrix = new double* [row];
    for (int i = 0; i < row; i++) {
        matrix[i] = new double [column];
    }

    int counter = 0;
    while (value <= stop) {
        matrix[0][counter] = value;
        matrix[1][counter] = f_1(value);
        matrix[2][counter] = f_2(value);
        value += step;
        counter++;
    }
}

int main() {
    double start = 1;
    double stop = 2;
    double steps = 11;
    double value = 1;
    double step = (stop - start) / steps;

    int row = 3;
    int column = (int) steps + 1;
    auto** matrix = new double * [0];

    calc(matrix, row, column, value, step, stop);

    std::cout << "+------------+------------+------------+" << std::endl;
    std::cout << "|    Value   |    F(1)    |    F(2)    |" << std::endl;
    std::cout << "|------------+------------+------------|" << std::endl;
    for (int i = 0; i < steps + 1; i++) {
        printf("|    %.2f    |    %.2f    |    %.2f    |\n", matrix[0][i], matrix[1][i], matrix[2][i]);
    }
    std::cout << "+------------+------------+------------+" << std::endl;

    return 0;
}
