#include <iostream>

void input(int** &matrix, int &row, int &column) {
    std::cout << "[>] Enter size of matrix (row column): ";
    std::cin >> row >> column;

    matrix = new int* [row];
    for (int i = 0; i < row; i++) {
        matrix[i] = new int [column];
    }

    for (int i = 0; i < row; i++) {
        std::cout << "[>] Enter " << i + 1 <<" line: ";
        for (int j = 0; j < column; j++) {
            std::cin >> matrix[i][j];
        }
    }
}

int* calc(int** &matrix, const int &row, const int &column) {
    int* array = new int [row];

    int multiply = 0;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            if (j == 0) {
                multiply = matrix[i][j];
            } else if (matrix[i][j] > 0) {
                multiply *= matrix[i][j];
            }
        }
    }
    return array;
}

void print(int* &array, const int &size){
    std::cout << "[+] Output array: ";
    for (int i = 0; i < size; i++) {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
}
