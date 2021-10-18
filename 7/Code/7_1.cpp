#include <iostream>

int main() {
    int width = 4;
    int height = 7;

    int max;
    int max_i;
    int max_j;
    int matrix[width][height];

    for (int i = 0; i < width; i++) {
        for (int j = 0; j < height; j++) {
            std::cout << "[>] Enter (" << i + 1 << ", " << j + 1 << ") element: ";
            std::cin >> matrix[i][j];
            if (max < matrix[i][j]) {
                max = matrix[i][j];
                max_i = i;
                max_j = j;
            }
        }
    }

    for (int i = 0; i < width; i++) {
        for (int j = 0; j < height; j++) {
            if ((i == 0) && (j == 0)) {
                printf("%3d", max);
            } else if (i == 0) {
                if (j == max_j) {
                    printf("%3d", matrix[max_i][0]);
                } else {
                    printf("%3d", matrix[max_i][j]);
                }
            } else {
                printf("  0");
            }
        }
        std::cout << std::endl;
    }

    return 0;
}
