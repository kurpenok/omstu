#include <iostream>
#include <string>
#include <vector>

class Human {
    public: 
        Human(std::string f, std::string d) {
            fio = f;
            date = d;
        }
        ~Human() {
            std::cout << "[+] Human memory cleared" << std::endl;
        }
        std::string get_date() {
            return date;
        }
        std::string get_fio() {
            return fio;
        }
    private:
        std::string fio;
        std::string date;
};

class Student: public Human {
    public:
        Student(std::string f, std::string d, int s, int l):Human(f, d) {
            school = s;
            level = l;
            std::cout << "[+] Object created" << std::endl;
        }
        ~Student() {
            std::cout << "[+] Student memory cleared" << std::endl;
        }

        int school;
        int level;
};

void find(std::vector<Student> students, std::string date, int school);

int main() {
    std::vector<Student> students;
    
    std::string fio, date;
    int school, level;

    while (true) {
        std::cout << "[>] Enter parameters: ";
        std::cin >> fio >> date >> school >> level;

        Student student(fio, date, school, level);
        students.push_back(student);

        break;
    }

    find(students, "26.08.2003", 166);

    return 0;
}

void find(std::vector<Student> students, std::string date, int school) {
    for (int i = 0; i < students.size(); i++) {
        if (students[i].school == school && students[i].get_date() == date) {
            std::cout << students[i].get_fio() << std::endl;
        }
    }
}

