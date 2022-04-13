#include <iostream>
#include <ostream>

class Log {
private:
    double number;
    double base;
    double value;

public:
    Log(double n, double b): number(n), base(b) {
        if (base == 1) {
            throw "[-] The base is equal to one!";
        } else if (base <= 0) {
            throw "[-] Base less than or equal to zero!";
        } else if (number <= 0) {
            throw "[-] Number less than or equal to zero!";
        } else {
            // The value of the logarithm can only be an integer!

            double v = 1;
            for (int i = 0; i < number; ++i) {
                if (v == number) {
                    value = i;
                    break;
                } else if (v > number) {
                    throw "[-] Could not find degree!";
                }
                v *= base;
            }
        }
    }
    
    Log& operator=(Log&);
    Log& operator+(Log&);
    Log& operator-(Log&);
    Log& operator*(Log&);
    Log& operator/(Log&);
    Log& operator^(int);
    Log& operator>(double);

    double get_value() {
        return value;
    }
};

Log& Log::operator=(Log& other) {
    if (this != &other) {
        number = other.number;
        base = other.base;
        value = other.value;
    }
    return *this;
}

Log& Log::operator+(Log& other) {
    value += other.value; 
    return *this;
}

Log& Log::operator-(Log& other) {
    value -= other.value;
    return *this;
}

Log& Log::operator*(Log& other) {
    value *= other.value;
    return *this;
}

Log& Log::operator/(Log& other) {
    value /= other.value;
    return *this;
}

Log& Log::operator^(int power) {
    for (int i = 0; i < power; ++i) {
        value *= value;
    }
    return *this;
}

// Redefining base change operator doesn't work
/*
Log& Log::operator>(double new_base) {
    this = Log(number, new_base) / Log(base, new_base);
    base = new_base;
    return *this;
}
*/

std::ostream& operator<<(std::ostream& s, Log& l) {
    s << l.get_value();
    return s;
}

int main() {
    Log log(8, 2);
    std::cout << log << std::endl;
}

