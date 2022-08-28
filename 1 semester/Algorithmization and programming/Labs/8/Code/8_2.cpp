#include <iostream>
#include <cmath>

bool check(const double x[], const double y[], int size){
    for (int i = 0; i < size; i++) {
        if (x[i] * y[i] <= 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int size = 8;
    double x[size];
    double y[size];

    std::cout << "[>] Enter array X: ";
    for (int i = 0; i < size; i++) {
        std::cin >> x[i];
    }
    std::cout << "[>] Enter array Y: ";
    for (int i = 0; i < size; i++) {
        std::cin >> y[i];
    }

    double sum = 0;
    if (check(x, y, size)) {
        for (int i = 0; i < size; i++) {
            sum += pow(x[i], 2);
        }
    } else {
        for (int i = 0; i < size; i++) {
            sum += pow(y[i], 2);
        }
    }

    std::cout << "[+] Sum of array: " << sum << std::endl;

    return 0;
}
