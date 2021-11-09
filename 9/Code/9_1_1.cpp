#include <iostream>

void input(int** &matrix, int &row, int &column) {
    std::cout << "[>] Enter size of matrix (row column): ";
    std::cin >> row >> column;
    std::cout << std::endl;

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

void find(int** &matrix, int &row, int &column, int &max, int &max_i, int &max_j) {
    max = 0;
    max_i = 0;
    max_j = 0;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            if (max < matrix[i][j]) {
                max = matrix[i][j];
                max_i = i;
                max_j = j;
            }
        }
    }
}

int main() {
    int **matrix = new int* [0];
    int row, column;

    input(matrix, row, column);

    int max, max_i, max_j;

    find(matrix, row, column, max, max_i, max_j);

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            if (i == 0) {
                if (j == 0) {
                    printf("%5d", matrix[max_i][max_j]);
                } else if (j == max_j) {
                    printf("%5d", matrix[max_i][0]);
                } else {
                    printf("%5d", matrix[max_i][j]);
                }
            } else if (i == max_i) {
                if (j == 0) {
                    printf("%5d", matrix[0][max_j]);
                } else if (j == max_j) {
                    printf("%5d", matrix[0][0]);
                } else {
                    printf("%5d", matrix[0][j]);
                }
            } else {
                if (j == 0) {
                    printf("%5d", matrix[i][max_j]);
                } else if (j == max_j) {
                    printf("%5d", matrix[i][0]);
                } else {
                    printf("%5d", matrix[i][j]);
                }
            }
        }
        std::cout << std::endl;
    }

    return 0;
}
