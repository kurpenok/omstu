#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    double b = 1.3;

    if (x < 1.3) {
        return (log(b * x - 1)) - (1 / (b * x + 1));
    } else if ((x >= 1.4) && (x <= 1.7)) {
        return b * x + 1;
    } else if (x > 1.7) {
        return (log(b * x + 1)) - (1 / (b * x + 1));
    }

    return 0;
}

int main() {
    double x = 0;

    while ((x < 1) | (x > 2)) {
        cout << "[>] Enter X [1, 2]: ";
        cin >> x;
    }

    double result = f(x);
    cout << "[+] Result: " << result << endl;

    return 0;
}
