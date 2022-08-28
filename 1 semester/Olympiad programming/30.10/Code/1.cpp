#include <iostream>

void input(int** &matrix, int &row, int &column);

void set_zero(int** &output, int &row, int &column);

void right(int** &matrix, int** &output, const int &row, const int &column, int start_x, int start_y);

void down(int** &matrix, int** &output, const int &row, const int &column, int start_x, int start_y);

int main() {
    int row, column;

    int** matrix;
    int** output;

    input(matrix, row, column);
    set_zero(output, row, column);

    int start_x = 1;
    int start_y = 1;

    output[1][1] = matrix[1][1];

    right(matrix, output, row, column, start_x, start_y);
    down(matrix, output, row, column, start_x, start_y);

    std::cout << "[+] Max count: " << output[row - 2][column - 2] << std::endl;

    return 0;
}

void input(int** &matrix, int &row, int &column) {
    const int WALL = 0;

    std::cout << "[>] Enter size of matrix (row column): ";
    std::cin >> row >> column;

    row += 2;
    column += 2;

    matrix = new int* [row];

    for (int i = 0; i < row; i++) {
        matrix[i] = new int [column];
    }

    for (int i = 0; i < row; i++) {
        if ((i != 0) && (i != row - 1)) {
            std::cout << "[>] Enter " << i << " line: ";
        }
        for (int j = 0; j < column; j++) {
            if ((i == 0) || (i == row - 1) || (j == 0) || (j == column - 1)) {
                matrix[i][j] = WALL;
            } else {
                std::cin >> matrix[i][j];
            }
        }
    }
}

void set_zero(int** &output, int &row, int &column) {
    const int FREE = 0;

    output = new int* [row];

    for (int i = 0; i < row; i++) {
        output[i] = new int [column];
    }
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            output[i][j] = FREE;
        }
    }
}

void right(int** &matrix, int** &output, const int &row, const int &column, int start_x, int start_y) {
    if ((start_x == column - 1) || (start_y == row - 1)) {
        return;
    }

    if (output[start_x][start_y] + matrix[start_x + 1][start_y] > output[start_x + 1][start_y]) {
        output[start_x + 1][start_y] = output[start_x][start_y] + matrix[start_x + 1][start_y];

        for (int i = 1; i < row - 1; i++) {
            for (int j = 1; j < column - 1; j++) {
                std::cout << output[i][j] << "  ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
    start_x++;

    right(matrix, output, row, column, start_x, start_y);
    down(matrix, output, row, column, start_x, start_y);
}

void down(int** &matrix, int** &output, const int &row, const int &column, int start_x, int start_y) {
    if ((start_x == column - 1) || (start_y == row - 1)) {
        return;
    }

    if (output[start_x][start_y] + matrix[start_x][start_y + 1] > output[start_x][start_y + 1]) {
        output[start_x][start_y + 1] = output[start_x][start_y] + matrix[start_x][start_y + 1];
    }
    start_y++;

    right(matrix, output, row, column, start_x, start_y);
    down(matrix, output, row, column, start_x, start_y);
}
