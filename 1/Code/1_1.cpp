#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double y1, y2, a, b, x1, x2;

    x1 = 1;
    x2 = 2;
    a = 0.5;
    b = 3.1;

    y1 = (sqrt(abs(a * x1 * sin(x1) * sin(x1)))) + ((x1 + b) * pow(M_E, -2 * x1));
    cout << "[+] Y1 = " << y1 << endl;

    y2 = (sqrt(abs(a * x2 * sin(x2) * sin(x2)))) + ((x2 + b) * pow(M_E, -2 * x1));
    cout << "[+] Y2 = " << y2 << endl;

    return 0;
}
