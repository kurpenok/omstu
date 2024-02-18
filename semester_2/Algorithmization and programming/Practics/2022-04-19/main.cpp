#include <iostream>
#include <string>
#include <vector>

#include "enrolle.h"
#include "teacher.h"

int main() {
    int count;

    std::cout << "[>] Enter count of applicants: ";
    std::cin >> count;

    std::vector<Enrolle> applicants;
    
    std::string name;
    std::string surname;
    std::string exam;

    std::string tname;
    std::string tsurname;
    double points;

    double sum;

    for (int i = 0; i < count; ++i) {
        std::cout << "[>] Enter teacher parameters: ";
        std::cin >> tname >> tsurname >> points;
        Teacher teacher(tname, tsurname, points);

        std::cin >> name >> surname >> exam;
        applicants.push_back(Enrolle(
                    name, surname, exam, tname, tsurname, points));

        sum += teacher.getPoints();
    }

    double average = sum / count;

    std::cout << "[+] Average of points: " << average << std::endl;

    std::cout << "[+] List of enlisted:" << std::endl;
    for (auto enrolle: applicants) {
        if (enrolle.getExamPoints() >= 4.5) {
            std::cout << "[+] "
                << enrolle.getName() << " "
                << enrolle.getSurname() << " "
                << enrolle.getExam() << " "
                << enrolle.getExamPoints() << " "
                << enrolle.getTName() << " "
                << enrolle.getTSurname() << std::endl;
        }
    }
}

