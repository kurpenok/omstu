#include <iostream>

const int WALL = -1;
const int FREE = 1000000;

void input(int** &matrix, int &row, int &column);

void set_walls(int** &matrix, int &row, int &column);

void set_points(int &start_x, int &start_y, int &end_x, int &end_y);

void up(int** &matrix, int start_x, int start_y);

void right(int** &matrix, int start_x, int start_y);

void down(int** &matrix, int start_x, int start_y);

void left(int** &matrix, int start_x, int start_y);

int main() {
    int row, column;

    int** matrix;

    input(matrix, row, column);
    set_walls(matrix, row, column);


    int start_x, start_y;
    int end_x, end_y;

    set_points(start_x, start_y, end_x, end_y);

    matrix[start_x][start_y] = 0;

    up(matrix, start_x, start_y);
    right(matrix, start_x, start_y);
    down(matrix, start_x, start_y);
    left(matrix, start_x, start_y);

    if (matrix[end_x][end_y] > 0) {
        std::cout << "[+] Count of steps: " << matrix[end_x][end_y] << std::endl;
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

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            if (!i || !j || (i == row - 1) || (j == column - 1)) {
                matrix[i][j] = WALL;
            } else {
                matrix[i][j] = FREE;
            }
        }
    }
}

void set_walls(int** &matrix, int &row, int &column) {
    int x = 0;
    int y = 0;
    while (true) {
        std::cout << "[>] Enter wall coords (x y; for end enter -1 -1): ";
        std::cin >> x >> y;
        if ((x == -1) && (y == -1)) {
            break;
        } else {
            matrix[x][y] = WALL;
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

void up(int** &matrix, int start_x, int start_y) {
    if (matrix[start_x][start_y - 1] == WALL || matrix[start_x][start_y] + 1 >= matrix[start_x][start_y - 1]) {
        return;
    }

    matrix[start_x][start_y - 1] = matrix[start_x][start_y] + 1;
    start_y--;

    up(matrix, start_x, start_y);
    right(matrix, start_x, start_y);
    down(matrix, start_x, start_y);
    left(matrix, start_x, start_y);
}

void right(int** &matrix, int start_x, int start_y) {
    if (matrix[start_x + 1][start_y] == WALL || matrix[start_x][start_y] + 1 >= matrix[start_x + 1][start_y]) {
        return;
    }

    matrix[start_x + 1][start_y] = matrix[start_x][start_y] + 1;
    start_x++;

    up(matrix, start_x, start_y);
    right(matrix, start_x, start_y);
    down(matrix, start_x, start_y);
    left(matrix, start_x, start_y);
}

void down(int** &matrix, int start_x, int start_y) {
    if (matrix[start_x][start_y + 1] == WALL || matrix[start_x][start_y] + 1 >= matrix[start_x][start_y + 1]) {
        return;
    }

    matrix[start_x][start_y + 1] = matrix[start_x][start_y] + 1;
    start_y++;

    up(matrix, start_x, start_y);
    right(matrix, start_x, start_y);
    down(matrix, start_x, start_y);
    left(matrix, start_x, start_y);
}

void left(int** &matrix, int start_x, int start_y) {
    if (matrix[start_x - 1][start_y] == WALL || matrix[start_x][start_y] + 1 >= matrix[start_x - 1][start_y]) {
        return;
    }

    matrix[start_x - 1][start_y] = matrix[start_x][start_y] + 1;
    start_x--;

    up(matrix, start_x, start_y);
    right(matrix, start_x, start_y);
    down(matrix, start_x, start_y);
    left(matrix, start_x, start_y);
}
