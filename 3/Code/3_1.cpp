#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double first_element = 4.0;
    double second_element = 0;

    for (int i = 0; i < 100; i++) {
        second_element += (pow(-1, i) / ((2 * i) + 1));
    }

    double pi = first_element * second_element;

    cout << "[+] Pi: " << pi << endl;

    return 0;
}
