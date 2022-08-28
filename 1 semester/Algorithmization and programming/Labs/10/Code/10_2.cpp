#include <iostream>

int main() {
    std::string string;
    std::cout << "[>] Enter text: ";
    getline(std::cin, string);

    bool flag = true;

    std::string temp;
    temp += string[0];

    for (int i = 1; i < string.size(); i++) {
        if (string[i] == ' ') {
            std::cout << temp << " ";
            flag = true;
            temp = "";
        } else if (string[i] < string[i - 1]) {
            flag = false;
            temp = "";
        } else if ((string[i] > string[i - 1]) && flag) {
            temp += string[i];
        }
    }
    std::cout << temp << std::endl;

    return 0;
}
