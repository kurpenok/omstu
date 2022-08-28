#include <iostream>

int f(int n);

int main() {
    std::cout << "[+] F(64): " << f(64) << std::endl;
    
    int steps[64];

    for (int i = 1; i < 65; i++) {
        if (i == 1) {
            steps[i - 1] = 1;
        } else if ((i > 1) && !(i % 2)) {
            steps[i - 1] = 2 * steps[i - 2];
        } else if ((i > 1) && (i % 2)) {
            steps[i - 1] = 5 * i + steps[i - 3];
        }
    }

    std::cout << "[+] F(64): " << steps[63] << std::endl;
    
    return 0;
}

int f(int n) {
    if (n == 1) {
        return 1;
    } else if ((n > 1) && !(n % 2)) {
        return 2 * f(n - 1);
    } else if ((n > 1) && (n % 2)) {
        return 5 * n + f(n - 2);
    }

    return 0;
}

