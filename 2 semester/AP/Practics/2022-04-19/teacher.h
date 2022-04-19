#pragma once

#include <string>

class Teacher {
private:
    std::string name;
    std::string surname;
    double points;

public:
    Teacher(std::string n, std::string s, double p):
        name(n), surname(s), points(p) {}

    double getPoints() {
        return points;
    }
};

