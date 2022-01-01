#include <iostream>

int main() {
    int x;
    std::cout << "[>] Enter X (type k5): ";
    std::cin >> x;

    int k = x / 10;

    if ((x * x) == (k * (k + 1) * 100 + 25)) {
        std::cout << "[+] Success!";
    } else {
        std::cout << "[-] Fatal error!";
    }

    return 0;
}
