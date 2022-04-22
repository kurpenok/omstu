#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <type_traits>
#include <vector>
#include <algorithm>

void bubbleSort(std::vector<int>& array);

void combSort(std::vector<int>& array);

void shakeSort(std::vector<int>& array);

void merge(std::vector<int>& a, std::vector<int>& b);
void quickSort(std::vector<int>& array);

int main() {
    std::vector<int> array;
}

void bubbleSort(std::vector<int>& array) {
    int temp;

    for (int i = 0; i < array.size(); ++i) {
        for (int j = 0; j < array.size() - i - 1; ++j) {
            if (array[j] > array[j + 1]) {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

void combSort(std::vector<int>& array) {
    double factor = 1.2473309;
    int step = array.size() - 1;
    int temp;

    while (step >= 1) {
        for (int i = 0; i + step < array.size(); ++i) {
            if (array[i] > array[i + step]) {
                temp = array[i];
                array[i] = array[i + step];
                array[i + step] = temp;
            }
        }
    }
}

void shakeSort(std::vector<int>& array) {
    int control = array.size();
    int left = 0;
    int right = array.size() - 1;

    do {
        for (int i = left; i < right; ++i) {
            if (array[i] > array[i + 1]) {
                std::swap(array[i], array[i + 1]);
                control = i;
            }
        }
        right = control;
        for (int i = right; i > left; i--) {
            if (array[i] < array[i - 1]) {
                std::swap(array[i], array[i - 1]);
                control = i;
            }
        }
        left = control;
    } while (left < right);
}

void quickSort(std::vector<int>& array) {}

