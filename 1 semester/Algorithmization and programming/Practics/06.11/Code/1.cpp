#include <iostream>
#include <string>

void input(int** &matrix, int &row, int &column) {
    std::cout << "[>] Enter size of matrix (row column): ";
    std::cin >> row;
    std::cin >> column;

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

int count(int** matrix, int &current_row, int &column) {
    int count_ones = 0;
    for (int j = 0; j < column; j++) {
        if (matrix[current_row][j] == 1) {
            count_ones++;
        }
    }
    return count_ones;
}

int sum(int** matrix, int &current_row, int &column) {
    int s = 0;
    for (int j = 0; j < column; j++) {
        s += matrix[current_row][column];
    }
    return s;
}

int main() {
    int **matrix_1;
    int row_1, column_1;

    int **matrix_2;
    int row_2, column_2;

    int **matrix_3;
    int row_3, column_3;

    input(matrix_1, row_1, column_1);
    input(matrix_2, row_2, column_2);
    input(matrix_3, row_3, column_3);

    int max_count_ones_sum_1 = 0;
    int max_count_ones_1 = 0;
    int count_ones_1 = 0;

    for (int i = 0; i < row_1; i++) {
        count_ones_1 = count(matrix_1, i, column_1);
        if (max_count_ones_1 < count_ones_1) {
            max_count_ones_1 = count_ones_1;
            max_count_ones_sum_1 = sum(matrix_1, i, column_1);
        }
    }
    std::cout << "[+] Sum elements of line with max ones count: " << max_count_ones_sum_1 << std::endl;

    int max_count_ones_sum_2 = 0;
    int max_count_ones_2 = 0;
    int count_ones_2 = 0;

    for (int i = 0; i < row_2; i++) {
        count_ones_2 = count(matrix_2, i, column_2);
        if (max_count_ones_2 < count_ones_2) {
            max_count_ones_2 = count_ones_2;
            max_count_ones_sum_2 = sum(matrix_2, i, column_2);
        }
    }
    std::cout << "[+] Sum elements of line with max ones count: " << max_count_ones_sum_2 << std::endl;

    int max_count_ones_sum_3 = 0;
    int max_count_ones_3 = 0;
    int count_ones_3 = 0;

    for (int i = 0; i < row_3; i++) {
        count_ones_3 = count(matrix_3, i, column_3);
        if (max_count_ones_3 < count_ones_3) {
            max_count_ones_3 = count_ones_3;
            max_count_ones_sum_3 = sum(matrix_3, i, column_3);
        }
    }
    std::cout << "[+] Sum elements of line with max ones count: " << max_count_ones_sum_3 << std::endl;

    return 0;
}
