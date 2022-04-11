#include <iostream>
#include <vector>

class Base {
private:
    int count, number;
    std::vector<int> numbers;

public:
    void input_numbers() {
        std::cout << "[>] Enter count of numbers: ";
        std::cin >> count;

        std::cout << "[>] Enter numbers: ";
        for (int i = 0; i < count; ++i) {
            std::cin >> number;
            numbers.push_back(number);
        }
    }

    std::vector<int> get_numbers() {
        return numbers;
    }
};

class Derived: public Base {
public:
    void swap(int *xp, int *yp) {
        int temp = *xp;
        *xp = *yp;
        *yp = temp;
    }

    void sort() {
        std::vector<int> numbers;
        numbers = get_numbers();

        for (int i = 0; i < numbers.size() - 1; ++i) {
            for (int j = 0; j < numbers.size() - i - 1; ++j) {
                if (numbers[j] > numbers[j + 1]) {
                    swap(&numbers[j], &numbers[j + 1]);
                }
            }
        }
        
        std::cout << "[+] Show sorted array: ";
        for (auto n: numbers) {
            std::cout << n << " ";
        }
        std::cout << std::endl;
    }

    int sum() {
        int s = 0;
        for (auto n: get_numbers()) {
            s += n;
        }
        return s;
    }
};

int main() {
    Derived derived;

    derived.input_numbers();
    
    derived.sort();

    std::cout << "[+] Sum of array: " << derived.sum() << std::endl;
}

