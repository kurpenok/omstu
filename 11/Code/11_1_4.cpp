#include <iostream>
#include <fstream>
#include <vector>

void input(int*& array, int& size, const std::string& path);

int max(int*& array, int& size);

int min(int*& array, int& size);

int* sum(int*& array_1, int*& array_2, int& size);

int main() {
    int size;
    int* a;
    int* b;
    int* c;

    input(a, size, "input_4_1.txt");
    input(b, size, "input_4_2.txt");
    input(c, size, "input_4_3.txt");

    int z;

    int* bc = sum(b, c, size);

    std::ofstream output("output_4.txt", std::ios::trunc);

    if (min(a, size) < min(b, size)) {
        z = (max(b, size) / max(a, size)) + (max(c, size) / min(bc, size));
        output << "[+] Z: " << z << '\n';
    } else if (min(a, size) > min(b, size)) {
        z = max(bc, size) + min(c, size);
        output << "[+] Z: " << z << '\n';
    }

    return 0;
}

void input(int*& array, int& size, const std::string& path) {
    std::ifstream input(path);

    std::string text;
    std::string line;

    if (input.is_open()) {
        while (getline(input, line)) {
            text += line + '\n';
        }
    }

    for (char symbol: text) {
        if (symbol == '\n') {
            break;
        } else if (symbol != ' ') {
            size = static_cast<int> (symbol) - static_cast<int> ('0');
        }
    }

    array = new int [size];

    std::vector<int> numbers;
    std::string number;

    bool flag = false;
    for (char symbol: text) {
        if ((symbol == '\n') && !flag) {
            flag = true;
        } else if (((symbol == ' ') || (symbol == '\n')) && flag) {
            numbers.push_back(std::stoi(number));
            number = "";
        } else if ((symbol != ' ') && flag) {
            number += symbol;
        }
    }

    for (int i = 0; i < size; ++i) {
        array[i] = numbers[i];
    }
}

int max(int*& array, int& size) {
    int m = array[0];

    for (int i = 0; i < size; i++) {
        if (m < array[i]) {
            m = array[i];
        }
    }
    return m;
}

int min(int*& array, int& size) {
    int m = array[0];

    for (int i = 0; i < size; i++) {
        if (m > array[i]) {
            m = array[i];
        }
    }
    return m;
}

int* sum(int*& array_1, int*& array_2, int& size) {
    int* array = new int [size];

    for (int i = 0; i < size; i++) {
        array[i] = array_1[i] + array_2[i];
    }
    return array;
}
