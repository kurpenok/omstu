#include <iostream>

int f(int n);

int main() {
	int count = 0;

	for (int i = 1; i < 1001; i++) {
		if (!(f(i) % 11)) {
			count++;
		}
	}
	std::cout << "[+] Count of multiples of 11: " << count << std::endl;
	
	int size = 1000;
	int* result = new int [size];
	
	count = 0;

	for (int i = size; i > 0; i--) {
		if (i > 25) {
			result[i - 1] = 2 * i * i * i + 1;
		} else {
			result[i - 1] = result[i + 1] + 2 * result[i + 2];
		}
	}

	for (int i = 0; i < size; i++) {
		if (!(result[i] % 11)) {
			count++;
		}
	}

	std::cout << "[+] Count of multiples of 11: " << count << std::endl;

    return 0;
}

int f(int n) {
	if (n > 25) {
		return 2 * n * n * n + 1;
	} else if (n <= 25) {
		return f(n + 2) + 2 * f(n + 3);
	}
	return 0;
}

