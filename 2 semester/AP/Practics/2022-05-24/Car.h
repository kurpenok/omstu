#pragma once

#include <iostream>
#include <iterator>
#include <string>

class Car {
public:
    std::string label;
    short cylinder;
    int power;

    Car(std::string& l, short& c, int& p) {
        label = l;
        cylinder = c;
        power = p;
    }

    ~Car() {}

    void show() {
        std::cout << "[+] Car " << label << ": "
            << cylinder << ", " << power << std::endl;
    }
};

class Truck: public Car {
public:
    int loadCapacity;
    
    Truck(std::string& l, short& c, int& p, int& lc): Car(l, c, p) {
        label = l;
        cylinder = c;
        power = p;
        loadCapacity = lc;
    }

    ~Truck() {}

    void show() {
        std::cout << "[+] Truck " << label << ": "
            << cylinder << ", " << power << ", " << loadCapacity << std::endl;
    }
};

