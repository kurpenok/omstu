#include <iostream>
#include <cmath>

double f(double x) {
    double b = 1.3;

    if (x < 1.3) {
        return log(b * x) - (1 / (b * x + 1));
    } else if ((x >= 1.3) && (x <= 1.7)) {
        return b * x + 1;
    } else if (x > 1.7) {
        return log(b * x) + (1 / (b * x + 1));
    }

    return 0;
}

int main() {
    double x;

    std::cout << "[>] Enter X [1, 2]: ";
    std::cin >> x;

    double result = f(x);
    std::cout << "[+] Result: " << result << std::endl;

    return 0;
}
