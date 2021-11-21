#include <iostream>

int main() {
    std::string string;
    std::string key = "key";

    std::cout << "[>] Enter text: ";
    std::cin >> string;

    if ((string.find(key[0]) != -1) && (string.find(key[1]) != -1) && (string.find(key[2]) != -1)) {
        std::cout << "[+] Yes" << std::endl;
    } else {
        std::cout << "[+] No" << std::endl;
    }

    return 0;
}
