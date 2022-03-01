#include <iostream>
#include <algorithm>
#include <ostream>
#include <vector>
#include <map>

int main() {
    // Для заданного одномерного массива
    // Необходимо определить часто появляения
    // Каждого символа
    // Для этого используются алгоритмы и контейнер map
    
    std::vector<int> array;
    int element;
    int count;

    std::cout << "[>] Enter count of elements: ";
    std::cin >> count;
    
    std::cout << "[>] Enter array: ";
    for (int i = 0; i < count; i++) {
        std::cin >> element;
        array.push_back(element);
    }

    std::map<int, int> counter;

    for (int i = 0; i < count; i++) {
        counter[array[i]]++;
    }
    
    std::cout << "[+] Result: ";
    for (auto c: counter) {
        std::cout << "(" << c.first << ", " << c.second  << ") "<< std::endl;
    }
    std::cout << std::endl;

    return 0;
}

