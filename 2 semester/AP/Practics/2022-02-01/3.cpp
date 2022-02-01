#include <iostream>

int f(int n);

int main() {
    std::cout << "[+] F(84): " << f(84) << std::endl;

    int steps[84];

    for (int i = 1; i < 85; i++) {
        if (i <= 1) {
            steps[i - 1] = 1;
        } else if ((i > 1) && !(i % 2)) {
            steps[i - 1] = i * steps[i - 2];
        } else if ((i > 1) && (i % 2)) {
            steps[i - 1] = i + steps[i - 3];
        }
    }

    std::cout << "[+] F(84): " << steps[83] << std::endl;

    return 0;
}

int f(int n) {
    if (n <= 1) {
        return 1;
    } else if ((n > 1) && !(n % 2)) {
        return n * f(n - 1);
    } else if ((n > 1) && (n % 2)) {
        return n + f(n - 2);
    }

    return 0;
}

