#include <iostream>

int main() {
    int s = 0;
    int n = 1;

    int x;
    do {
        std::cout << "[>] Enter X: ";
        std::cin >> x;
        s += x * n;
        n++;
    } while (x > 0);

    s -= x * --n;

    std::cout << "[+] Sum of numbers: " << s << std::endl;

    return 0;
}
