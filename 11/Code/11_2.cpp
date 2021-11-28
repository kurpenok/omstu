#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

void input(int**& matrix, int& row, int& column);

int** split(int**& matrix, int& row, int& column, const std::string& text);

void replace(int**& matrix, int& row, int& column);

void output(int**& matrix, int& row, int& column);

int main() {
    int **matrix = nullptr;
    int row, column;

    input(matrix, row, column);

    replace(matrix, row, column);

    output(matrix, row, column);

    return 0;
}

void input(int**& matrix, int& row, int& column) {
    std::ifstream input("input_5.txt");

    std::string text;
    std::string line;

    row = 0;
    if (input.is_open()) {
        while (getline(input, line)) {
            text += line + '\n';
            ++row;
        }
    }

    column = 0;

    for (char symbol: text) {
        if (symbol == '\n') {
            ++column;
            break;
        } else if (symbol == ' ') {
            ++column;
        }
    }

    matrix = new int* [row];

    for (int i = 0; i < row; i++) {
        matrix[i] = new int [column];
    }

    matrix = split(matrix, row, column, text);
}

int** split(int**& matrix, int& row, int& column, const std::string& text) {
    std::vector<int> numbers;
    std::string number;

    for (char symbol: text) {
        if ((symbol == ' ') || (symbol == '\n')) {
            numbers.push_back(std::stoi(number));
            number = "";
        } else {
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

void replace(int**& matrix, int& row, int& column) {
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < column; ++j) {
            if ((i + 1 % 2 == 0) && (j + 1 % 2 == 0)) {
                matrix[i][j] = 0;
            }
        }
    }
}

void output(int**& matrix, int& row, int& column) {
    std::ofstream output("output_5.txt", std::ios::trunc);

    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < column; ++j) {
            output << std::setw(3) << matrix[i][j] << " ";
        }
        output << '\n';
    }

    output.close();
}
