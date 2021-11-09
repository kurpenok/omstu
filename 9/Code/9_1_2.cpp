#include <iostream>

void pythagoras() {
    int row = 10;
    int column = 10;

    std::cout << "+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+" << std::endl;
    std::cout << "|  *  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |" << std::endl;
    std::cout << "+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+" << std::endl;
    for (int i = 1;  i < row; i++) {
        std::cout << "|  " << i << "  |";
        for (int j = 1; j < column; j++) {
            printf(" %3d |", i * j);
        }
        std::cout << std::endl;
        std::cout << "+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+" << std::endl;
    }
}

int main() {
    pythagoras();

    return 0;
}
