#include "modules.h"

int main() {
    int **matrix_1 = nullptr;
    int row_1 = 0;
    int column_1 = 0;

    int **matrix_2 = nullptr;
    int row_2 = 0;
    int column_2 = 0;

    int **matrix_3 = nullptr;
    int row_3 = 0;
    int column_3 = 0;

    input(matrix_1, row_1, column_1);
    input(matrix_2, row_2, column_2);
    input(matrix_3, row_3, column_3);

    int* array_1 = calc(matrix_1, row_1, column_1);
    int* array_2 = calc(matrix_2, row_2, column_2);
    int* array_3 = calc(matrix_3, row_3, column_3);

    print(array_1, row_1);
    print(array_2, row_2);
    print(array_3, row_3);

    return 0;
}
