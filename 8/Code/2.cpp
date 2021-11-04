#include <iostream>
#include <cmath>

double f_square(double r) {
    return M_PI * pow(r, 2);
}

double f_value(double r) {
    return (4 * M_PI * pow(r, 3)) / 3;
}

double f_relationship(double r) {
    return f_square(r) / f_value(r);
}

int main() {
    double r;

    std::cout << "[>] Enter R: ";
    std::cin >> r;

    std::cout << "[+] Square: " << f_square(r) << std::endl;
    std::cout << "[+] Value: " <<  f_value(r) << std::endl;
    std::cout << "[+] Relationship: " << f_relationship(r) << std::endl;

    return 0;
}
