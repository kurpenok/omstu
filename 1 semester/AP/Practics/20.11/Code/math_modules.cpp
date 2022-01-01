int** amount(int**& matrix_1, int**& matrix_2, int& row, int& column) {
    int** matrix_output;
    matrix_output = new int* [row];
    for (int i = 0; i < row; i++) {
        matrix_output[i] = new int [column];
    }

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            matrix_output[i][j] = matrix_1[i][j] + matrix_2[i][j];
        }
    }

    return matrix_output;
}

int** difference(int**& matrix_1, int**& matrix_2, int& row, int& column) {
    int** matrix_output;
    matrix_output = new int* [row];
    for (int i = 0; i < row; i++) {
        matrix_output[i] = new int [column];
    }

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            matrix_output[i][j] = matrix_1[i][j] - matrix_2[i][j];
        }
    }

    return matrix_output;
}

int** multiply(int**& matrix_1, int**& matrix_2, int& row, int& column) {
    int** matrix_output;
    matrix_output = new int* [row];
    for (int i = 0; i < row; i++) {
        matrix_output[i] = new int [column];
    }

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            matrix_output[i][j] = matrix_1[i][j] * matrix_2[i][j];
        }
    }

    return matrix_output;
}
