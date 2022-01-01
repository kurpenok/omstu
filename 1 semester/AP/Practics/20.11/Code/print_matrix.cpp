#include <iostream>

void print_matrix(int**& matrix, int& row, int& column) {
    std::cout << "[+] Output matrix:" << std::endl;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            std::cout << matrix[i][j];
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}
