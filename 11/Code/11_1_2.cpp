#include <iostream>
#include <iomanip>
#include <fstream>

void pythagoras() {
    std::ofstream output("output_2.txt", std::ios::trunc);

    int row = 10;
    int column = 10;

    if (output.is_open()) {
        output << "+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+" << '\n';
        output << "|  *  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |" << '\n';
        output << "+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+" << '\n';
        for (int i = 1; i < row; i++) {
            output << "|  " << i << "  |";
            for (int j = 1; j < column; j++) {
                output << std::setw(3) << i * j << "  |";
            }
            output << '\n';
            output << "+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+" << '\n';
        }
    }
    output.close();
}

int main() {
    pythagoras();

    return 0;
}
