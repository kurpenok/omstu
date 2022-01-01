#include <iostream>

const int WALL = -1;
const int FREE = 0;
const int CHECKED = 1;

void input(int** &matrix, int &row, int &column);

void set_zero(int** &output, int &row, int &column);

void set_points(int &start_x, int &start_y, int &end_x, int &end_y);

void up(int** &matrix, int** &output, int** &checked, int start_x, int start_y);

void right(int** &matrix, int** &output, int** &checked, int start_x, int start_y);

void down(int** &matrix, int** &output, int** &checked, int start_x, int start_y);

void left(int** &matrix, int** &output, int** &checked, int start_x, int start_y);

int main() {
    int row, column;

    int** matrix;

    input(matrix, row, column);

    int** output;

    set_zero(output, row, column);

    int** checked;

    set_zero(checked, row, column);

    int start_x, start_y;
    int end_x, end_y;

    set_points(start_x, start_y, end_x, end_y);

    output[start_x][start_y] = matrix[start_x][start_y];

    up(matrix, output, checked, start_x, start_y);
    set_zero(checked, row, column);
    checked[start_x][start_y] = CHECKED;

    right(matrix, output, checked, start_x, start_y);
    set_zero(checked, row, column);
    checked[start_x][start_y] = CHECKED;

    down(matrix, output, checked, start_x, start_y);
    set_zero(checked, row, column);
    checked[start_x][start_y] = CHECKED;

    left(matrix, output, checked, start_x, start_y);
    set_zero(checked, row, column);
    checked[start_x][start_y] = CHECKED;

    if (output[end_x][end_y] > 0) {
        std::cout << "[+] Max count: " << output[end_x][end_y] << std::endl;
    } else {
        std::cout << "[-] Path not found!" << std::endl;
    }

    return 0;
}

void input(int** &matrix, int &row, int &column) {
    std::cout << "[>] Enter size of matrix (row column): ";
    std::cin >> row >> column;

    row += 2;
    column += 2;

    matrix = new int* [row];

    for (int i = 0; i < row; i++) {
        matrix[i] = new int [column];
    }

    std::cout << "[!] Wall indicate -1 value!" << std::endl;
    for (int i = 0; i < row; i++) {
        if (i && (i != row - 1)) {
            std::cout << "[>] Enter " << i << " line: ";
        }
        for (int j = 0; j < column; j++) {
            if (!i || !j || (i == row - 1) || (j == column - 1)) {
                matrix[i][j] = WALL;
            } else {
                std::cin >> matrix[i][j];
            }
        }
    }
}

void set_zero(int** &output, int &row, int &column) {
    output = new int* [row];

    for (int i = 0; i < row; i++) {
        output[i] = new int [column];
    }

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            if (!i || !j || (i == row - 1) || (j == column - 1)) {
                output[i][j] = WALL;
            } else {
                output[i][j] = FREE;
            }
        }
    }
}

void set_points(int &start_x, int &start_y, int &end_x, int &end_y) {
    std::cout << "[>] Enter start coords (x y): ";
    std::cin >> start_x >> start_y;

    std::cout << "[>] Enter end coords (x y): ";
    std::cin >> end_x >> end_y;

    std::cout << std::endl;
}

void up(int** &matrix, int** &output, int** &checked, int start_x, int start_y) {
    if (output[start_x][start_y - 1] == WALL || checked[start_x][start_y - 1] || \
            output[start_x][start_y] + matrix[start_x][start_y - 1] <= output[start_x][start_y - 1]) {
        return;
    }

    output[start_x][start_y - 1] = output[start_x][start_y] + matrix[start_x][start_y - 1];
    checked[start_x][start_y - 1] = CHECKED;
    start_y--;

    up(matrix, output, checked, start_x, start_y);
    right(matrix, output, checked, start_x, start_y);
    down(matrix, output, checked, start_x, start_y);
    left(matrix, output, checked, start_x, start_y);
}

void right(int** &matrix, int** &output, int** &checked, int start_x, int start_y) {
    if (output[start_x + 1][start_y] == WALL  || checked[start_x + 1][start_y] || \
            output[start_x][start_y] + matrix[start_x + 1][start_y] <= output[start_x + 1][start_y]) {
        return;
    }

    output[start_x + 1][start_y] = output[start_x][start_y] + matrix[start_x + 1][start_y];
    checked[start_x + 1][start_y] = CHECKED;
    start_x++;

    up(matrix, output, checked, start_x, start_y);
    right(matrix, output, checked, start_x, start_y);
    down(matrix, output, checked, start_x, start_y);
    left(matrix, output, checked, start_x, start_y);
}

void down(int** &matrix, int** &output, int** &checked, int start_x, int start_y) {
    if (output[start_x][start_y + 1] == WALL || checked[start_x][start_y + 1] ||  \
            output[start_x][start_y] + matrix[start_x][start_y + 1] <= output[start_x][start_y + 1]) {
        return;
    }

    output[start_x][start_y + 1] = output[start_x][start_y] + matrix[start_x][start_y + 1];
    checked[start_x][start_y + 1] = CHECKED;
    start_y++;

    up(matrix, output, checked, start_x, start_y);
    right(matrix, output, checked, start_x, start_y);
    down(matrix, output, checked, start_x, start_y);
    left(matrix, output, checked, start_x, start_y);
}

void left(int** &matrix, int** &output, int** &checked, int start_x, int start_y) {
    if (output[start_x - 1][start_y] == WALL || checked[start_x - 1][start_y] ||  \
            output[start_x][start_y] + matrix[start_x - 1][start_y] <= output[start_x - 1][start_y]) {
        return;
    }

    output[start_x - 1][start_y] = output[start_x][start_y] + matrix[start_x - 1][start_y];
    checked[start_x - 1][start_y] = CHECKED;
    start_x--;

    up(matrix, output, checked, start_x, start_y);
    right(matrix, output, checked, start_x, start_y);
    down(matrix, output, checked, start_x, start_y);
    left(matrix, output, checked, start_x, start_y);
}
