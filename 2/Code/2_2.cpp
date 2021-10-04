#include <iostream>

using namespace std;

int main() {
    int x;
    cout << "[>] Enter X (type k5): ";
    cin >> x;

    int k = x / 10;

    if ((x * x) == (k * (k + 1) * 100 + 25)) {
        cout << "[+] Success!";
    } else {
        cout << "[-] Fatal error!";
    }

    return 0;
}