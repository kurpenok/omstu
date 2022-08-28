#include <iostream>
#include <vector>

void bubbleSort(std::vector<int>& array);

void combSort(std::vector<int>& array);

void shakeSort(std::vector<int>& array);

int partition(std::vector<int>& array, int start, int end);
void quickSort(std::vector<int>& array, int start, int end);

int main() {
    int count;
    std::cout << "[>] Enter count of elements: ";
    std::cin >> count;

    std::vector<int> array;
    
    std::cout << "[>] Enter elements: ";
    int temp;
    for (int i = 0; i < count; ++i) {
        std::cin >> temp;
        array.push_back(temp);
    }

    quickSort(array, 0, count - 1);

    std::cout << "[+] Sorted array: ";
    for (auto i: array) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
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

int partition(std::vector<int>& array, int start, int end) {
    int pivot = array[start];
    int count = 0;

    for (int i = start + 1; i <= end; ++i) {
        if (array[i] <= pivot) {
            ++count;
        }
    }

    int pivotIndex = start + count;
    std::swap(array[pivotIndex], array[start]);
    
    int i = start;
    int j = end;
    while (i < pivotIndex && j > pivotIndex) {
        while (array[i] <= pivot) {
            ++i;
        }
        while (array[j] > pivot) {
            --j;
        }
        if (i < pivotIndex && j > pivotIndex) {
            std::swap(array[i], array[j]);
            ++i;
            --j;
        }
    }

    return pivotIndex;
}

void quickSort(std::vector<int>& array, int start, int end) {
    if (start >= end) {
        return;
    }

    int index = partition(array, start, end);

    quickSort(array, start, index - 1);
    quickSort(array, index + 1, end);
}

