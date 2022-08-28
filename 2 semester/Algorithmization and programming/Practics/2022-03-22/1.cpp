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

void find_date(std::vector<Student>& students);

void find_school(std::vector<Student>& students);

void add(std::vector<Student>& students);

void remove(std::vector<Student>& students);

int main() {
    std::vector<Student> students;

    int status = 0;

    std::cout << "[1] Add\n[2] Remove\n[3] Find by date\n[4] Find by school\n[5] Exit\n" << std::endl;

    while (true) {
        std::cout << "[>] Enter status: ";
        std::cin >> status;

        switch (status) {
            case 1:
                add(students);
                break;
            case 2:
                remove(students);
                break;
            case 3:
                find_date(students);
                break;
            case 4:
                find_school(students);
                break;
            case 5:
                return 0;
        }
    }

    return 0;
}

void add(std::vector<Student>& students) {
    std::string fio, date;
    int school, level;

    std::cout << "[>] Enter parameters (fio, date, school, level): ";
    std::cin >> fio >> date >> school >> level;

    Student student(fio, date, school, level);
    students.push_back(student);

    std::cout << "[+] Student added" << std::endl << std::endl;
}

void remove(std::vector<Student>& students) {
    students.pop_back();
    std::cout << "[+] Student removed" << std::endl << std::endl;
}

void find_date(std::vector<Student>& students) {
    std::string date;

    std::cout << "[>] Enter date: ";
    std::cin >> date;

    for (int i = 0; i < students.size(); i++) {
        if (students[i].get_date() == date) {
            std::cout << students[i].get_fio() << std::endl;
        }
    }

    std::cout << "[+] Find finished" << std::endl << std::endl;
}

void find_school(std::vector<Student>& students) {
    int school;

    std::cout << "[>] Enter school: ";
    std::cin >> school;

    for (int i = 0; i < students.size(); i++) {
        if (students[i].school == school) {
            std::cout << students[i].get_fio() << std::endl;
        }
    }

    std::cout << "[+] Find finished" << std::endl << std::endl;
}

