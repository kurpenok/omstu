#include <iostream>

int f(int n);

int main() {
    std::cout << "[+] F(100): " << f(100) << std::endl;
    
    int steps[100];

    for (int i = 1; i < 101; i++) {
        if (i <= 3) {
            steps[i - 1] = i;
        } else if ((i > 3) && (i % 3 == 0)) {
            steps[i - 1] = i * i * i + steps[i - 2];
        } else if ((i > 3) && (i % 3 == 1)) {
            steps[i - 1] = 4 + steps[(i / 3) - 1];
        } else if ((i > 3) && (i % 3 == 2)) {
            steps[i - 1] = i * i + steps[i - 3];
        }
    }

    std::cout << "[+] F(100): " << steps[99] << std::endl;

    return 0;
}

int f(int n) {
    if (n <= 3) {
        return n;
    } else if ((n > 3) && (n % 3 == 0)) {
        return n * n * n + f(n - 1);
    } else if ((n > 3) && (n % 3 == 1)) {
        return 4 + f(n / 3);
    } else if ((n > 3) && (n % 3 == 2)) {
        return n * n + f(n - 2);
    }

    return 0;
}

