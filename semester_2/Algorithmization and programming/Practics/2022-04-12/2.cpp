#include <iostream>
#include <ostream>
#include <fstream>
#include <cmath>

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
            value = std::log(number) / std::log(base);
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

Log& Log::operator>(double new_base) {
    value = std::log(number) / std::log(new_base);
    base = new_base;
    return *this;
}


std::ostream& operator<<(std::ostream& s, Log& l) {
    s << l.get_value();
    return s;
}

class MyStreambuf:public std::streambuf {
private:
    std::streambuf*firstBuf;
    std::streambuf*secondBuf;

public:
    MyStreambuf(std::streambuf*_firstBuf,std::streambuf*_secondBuf):firstBuf(_firstBuf),secondBuf(_secondBuf){}
    std::streamsize xsputn(const char_type *s, std::streamsize n) {
        firstBuf->sputn(s,n);
        secondBuf->sputn(s,n);
        return n;
    }
 
    int overflow(int_type c) {
        firstBuf->sputc(c);
        secondBuf->sputc(c);
        return c;
    }
};
 
int main() {
    std::ofstream stream("output.txt");
    MyStreambuf streambuf(stream.rdbuf(),std::cout.rdbuf());
    std::cout.rdbuf(&streambuf);

    Log log(8, 2);
    std::cout << log << std::endl;
}

