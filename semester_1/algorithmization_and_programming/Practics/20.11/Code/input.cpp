#include <iostream>

void input(int**& matrix, int& row, int& column) {
    std::cout << "[>] Enter size of matrix (row column): ";
    std::cin >> row >> column;

    matrix = new int* [row];
    for (int i = 0; i < row; i++) {
        matrix[i] = new int [column];
    }

    for (int i = 0; i < row; i++) {
        std::cout << "[>] Enter " << i + 1 << " line: ";
        for (int j = 0; j < column; j++) {
            std::cin >> matrix[i][j];
        }
    }
}
