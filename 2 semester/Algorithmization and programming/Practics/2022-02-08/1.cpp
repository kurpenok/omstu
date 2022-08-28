#include <iostream>

int main() {
	long long two = 1;
	long five, number;

	for (int n = 2; n < 30; n += 2) {
		two *= 4;
		five = 5;

		for (int m = 1; m < 16; m += 2) {
			number = two * five;
			if ((100000000 <= number) && (number <= 300000000)) {
				std::cout << number << " " << n + m << std::endl;
			}
			five *= 25;
		}
	}

	return 0;
}

