#include <iostream>
#include <vector>

class Semi {
private:
    int speed;
    int weight;

public:
    Semi(int s, int w): speed(s), weight(w) {
        speed = s;
        weight = w;
    }

    void set_speed(int s) {
        speed = s;
    }

    void set_weight(int w) {
        weight = w;
    }
};

int main() {
    std::vector<Semi> semi;

    int speed;
    int weight;

    std::cout << "[>] Enter ten object parameters:" << std::endl;
    for (int i = 0; i < 10; ++i) {
        std::cout << "[>] Enter " << i + 1 << " parameter: ";
        std::cin >> speed >> weight;
        semi.push_back(Semi(speed, weight));
    }
}

