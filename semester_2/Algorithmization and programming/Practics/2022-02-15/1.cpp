#include <iostream>
#include <set>

int main() {
    int size = 10;
    int array[] = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};

    std::set<int> new_array;
    
    std::cout << "[>] Input array: ";
    for (int i = 0; i < size; i++) {
        new_array.insert(array[i]);
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
    
    std::cout << "[+] Set on input array: ";
    for (auto i: new_array) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}

