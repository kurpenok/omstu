#pragma once

#include <string>

#include "teacher.h"

class Enrolle {
private:
    std::string name;
    std::string surname;
    std::string tname;
    std::string tsurname;
    std::string exam;
    double points;

public:
    Enrolle(std::string n, std::string s, std::string tn, std::string ts,
            std::string e, double p): name(n), surname(s), tname(tn),
            tsurname(ts), exam(e), points(p) {}
        
    std::string getName() {
        return name;
    }

    std::string getSurname() {
        return surname;
    }

    std::string getTName() {
        return tname;
    }

    std::string getTSurname() {
        return tsurname;
    }

    std::string getExam() {
        return exam;
    }
    
    double getExamPoints() {
        return points;
    }
};

