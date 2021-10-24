#include <iostream>

int main() {
    int row = 7;
    int column = 4;

    int max = 0;
    int max_i = 0;
    int max_j = 0;
    int matrix[row][column];

    for (int i = 0; i < row; i++) {
        std::cout << "[>] Enter " << i + 1 << " line: ";
        for (int j = 0; j < column; j++) {
            std::cin >> matrix[i][j];
            if (max < matrix[i][j]) {
                max = matrix[i][j];
                max_i = i;
                max_j = j;
            }
        }
    }
    std::cout << std::endl;

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
