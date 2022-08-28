#include <iostream>

#include "input.h"
#include "print_matrix.h"
#include "math_modules.h"

int main() {
    int** matrix_1;
    int row_1, column_1;

    int** matrix_2;
    int row_2, column_2;

    int** matrix_output;

    input(matrix_1, row_1, column_1);
    input(matrix_2, row_2, column_2);

    if ((row_1 != row_2) || (column_1 != column_2)) {
        std::cout << "[-] FATAL ERROR! The sizes of the matrices do not match!" << std::endl;
        return 0;
    }

    std::cout << "[!] INSTRUCTION!" << std::endl;
    std::cout << "[1] To add matrices" << std::endl;
    std::cout << "[2] To subtract matrices" << std::endl;
    std::cout << "[3] For piecemeal matrix multiplication" << std::endl;
    std::cout << "[4] To exit" << std::endl << std::endl;

    int status;
    while (true) {
        std::cout << "[>] Enter status: ";
        std::cin >> status;
        if (status == 1) {
            matrix_output = amount(matrix_1, matrix_2, row_1, column_1);
            print_matrix(matrix_output, row_1, column_1);
        } else if (status == 2) {
            matrix_output = difference(matrix_1, matrix_2, row_1, column_1);
            print_matrix(matrix_output, row_1, column_1);
        } else if (status == 3) {
            matrix_output = multiply(matrix_1, matrix_2, row_1, column_1);
            print_matrix(matrix_output, row_1, column_1);
        } else if (status == 4) {
            std::cout << "[+] The program has completed its work" << std::endl;
            return 0;
        }
    }
}
