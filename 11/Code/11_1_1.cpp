#include <iostream>
#include <fstream>
#include <vector>

void input(int**& matrix, int& row, int& column);

int** split(int**& matrix, int& row, int& column, const std::string& text);

void find(int**& matrix, int& row, int& column, int& max, int& max_i, int& max_j);

void output(int**& matrix, int& row, int& column, int& max, int& max_i, int& max_j);

int main() {
    int **matrix = new int* [0];
    int row, column;

    input(matrix, row, column);

    int max, max_i, max_j;

    find(matrix, row, column, max, max_i, max_j);

    output(matrix, row, column, max, max_i, max_j);

    return 0;
}

void input(int**& matrix, int& row, int& column) {
    std::ifstream input("input_1.txt");

    std::string text;
    std::string line;

    std::vector<int> size;

    if (input.is_open()) {
        while (getline(input, line)) {
            text += line + '\n';
        }
    }

    for (char symbol: text) {
        if (symbol == '\n') {
            break;
        } else if (symbol != ' ') {
            size.push_back(static_cast<int> (symbol) - static_cast<int> ('0'));
        }
    }

    row = size[0];
    column = size[1];

    matrix = new int* [row];

    for (int i = 0; i < row; i++) {
        matrix[i] = new int [column];
    }

    matrix = split(matrix, row, column, text);
}

int** split(int**& matrix, int& row, int& column, const std::string& text) {
    std::vector<int> numbers;
    std::string number;

    bool flag = false;
    for (char symbol: text) {
        if ((symbol == '\n') && !flag) {
            flag = true;
        } else if (((symbol == ' ') || (symbol == '\n')) && flag) {
            numbers.push_back(std::stoi(number));
            number = "";
        } else if ((symbol != ' ') && flag) {
            number += symbol;
        }
    }

    int index = 0;
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < column; ++j) {
            matrix[i][j] = numbers[index];
            ++index;
        }
    }

    return matrix;
}

void find(int**& matrix, int& row, int& column, int& max, int& max_i, int& max_j) {
    max = 0;
    max_i = 0;
    max_j = 0;

    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < column; j++) {
            if (max < matrix[i][j]) {
                max = matrix[i][j];
                max_i = i;
                max_j = j;
            }
        }
    }
}

void output(int**& matrix, int& row, int& column, int& max, int& max_i, int& max_j) {
    std::ofstream output("output_1.txt", std::ios::trunc);

    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < column; ++j) {
            if (i == 0) {
                if (j == 0) {
                    output << matrix[max_i][max_j] << " ";
                } else if (j == max_j) {
                    output << matrix[max_i][0] << " ";
                } else {
                    output << matrix[max_i][j] << " ";
                }
            } else if (i == max_i) {
                if (j == 0) {
                    output << matrix[0][max_j] << " ";
                } else if (j == max_j) {
                    output << matrix[0][0] << " ";
                } else {
                    output << matrix[0][j] << " ";
                }
            } else {
                if (j == 0) {
                    output << matrix[i][max_j] << " ";
                } else if (j == max_j) {
                    output << matrix[i][0] << " ";
                } else {
                    output << matrix[i][j] << " ";
                }
            }
        }
        output << '\n';
    }

    output.close();
}
