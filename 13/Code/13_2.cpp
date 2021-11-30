#include <iostream>

#include "modules.h"

int main() {
    int size;
    int* a;
    int* b;
    int* c;

    input(a, size);
    input(b, size);
    input(c, size);

    int z;

    int* bc = sum(b, c, size);

    if (min(a, size) < min(b, size)) {
        z = (max(b, size) / max(a, size)) + (max(c, size) / min(bc, size));
        std::cout << "[+] Z: " << z << std::endl;
    } else if (min(a, size) > min(b, size)) {
        z = max(bc, size) + min(c, size);
        std::cout << "[+] Z: " << z << std::endl;
    }

    return 0;
}
