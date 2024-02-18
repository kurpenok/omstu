#include <iostream>

#include "RSA.h"

int main() {
    long long p;
    long long q;

    std::cout << "[>] Enter two simple numbers: ";
    std::cin >> p >> q;

    RSA rsa(p, q);

    long long* private_key = rsa.generate_private();
    long long* public_key = rsa.generate_public();

    std::cout << "[+] Private key: {" << private_key[0] << ", " << \
        private_key[1] << "}" << std::endl;
    std::cout << "[+] Public key: {" << public_key[0] << ", " << \
        public_key[1] << "}" << std::endl;

    long long message;
    std::cout << "[>] Enter message: ";
    std::cin >> message;

    long long encrypted = rsa.encrypt(message, public_key);
    long long decrypted = rsa.decrypt(encrypted, private_key);

    std::cout << "[+] Encrypted message: " << encrypted << std::endl;
    std::cout << "[+] Decrypted message: " << decrypted << std::endl;
}

