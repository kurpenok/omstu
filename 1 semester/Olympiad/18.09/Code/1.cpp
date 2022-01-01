#include <iostream>
#include <cmath>

int check(int &number) {
    int mods = 0;
    int max_mod = 0;
    for (int i = 2; i < (int) sqrt(number) + 1; i++) {
        if (mods > 3) {
            return 0;
        } else if (number % i == 0) {
            max_mod = i;
            mods++;
        }
    }
    if (mods == 3) {
        return max_mod;
    }
    return 0;
}

int main() {
    int result;
    for (int i = 1; i <= 200; i++) {
        result = check(i);
        if (result != 0) {
            std::cout << "[+] " << i << ": " << result << std::endl;
        }
    }

    return 0;
}
