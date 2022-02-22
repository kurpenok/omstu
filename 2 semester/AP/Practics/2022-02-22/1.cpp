#include <iostream>
#include <map>

int main() {
    int n;
    
    std::cout << "[>] Enter count of numbers: ";
    std::cin >> n;

    int phone, minutes;

    std::map<int, int> m;

    for (int i = 0; i < n; i++) {
        std::cout << "[>] Enter phone number and minutes: ";
        std::cin >> phone >> minutes;

        m[phone] += minutes;
    }
    
    for (auto [phone, minutes]: m) {
        std::cout << "[+] " << phone << ": " << minutes << std::endl;
    }

    return 0;
}

