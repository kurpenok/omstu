#include <iostream>

int f(int n);

int get_digit_amount(int n);

int main() {
    std::cout << "[+] The amount of digits: " << get_digit_amount(f(1)) << std::endl;

    int steps[20];

    for (int i = 20; i > 0; i--) {
        if (i > 15) {
            steps[i - 1] = i * i - 5;
        } else if (i <= 15) {
            steps[i - 1] = i * steps[i + 1] + i + steps[i + 2]; 
        }
    }

    std::cout << "[+] The amount of digits: " << get_digit_amount(steps[0]) << std::endl;
    
    return 0;
}

int f(int n) {
    if (n > 15) {
        return n * n - 5;
    } else if (n <= 15) {
        return n * f(n + 2) + n + f(n + 3);
    }

    return 0;
}

int get_digit_amount(int n) {
    int amount = 0;

    while (n) {
        amount += n % 10;
        n /= 10;
    }

    return amount;
}

