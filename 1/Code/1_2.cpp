#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double r, square, value, relationship;

    cout << "[>] Enter R: ";
    cin >> r;

    square = M_PI * pow(r, 2);
    value = (4 * M_PI * pow(r, 3)) / 3;

    cout << "[+] Square = " << square << endl;
    cout << "[+] Value = " << value << endl;

    relationship = square / value;

    cout << "[+] Relationship = " << relationship << endl;

    return 0;
}
