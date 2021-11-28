#include <iostream>
#include <fstream>
#include <set>

struct Person {
    std::string surname = "Not specified";
    std::string name = "Not specified";
    std::string middle_name = "Not specified";
    std::string address = "Not specified";
    std::string profession = "Not specified";
};

void write(const Person& person, const std::string& path);

void count(const std::string& path);

int main() {
    std::string path;
    std::cout << "[>] Enter file name: ";
    std::cin >> path;

    Person person;
    char status;
    while (true) {
        std::cout << "[>] To continue, click n: ";
        std::cin >> status;

        if (status != 'n') {
            break;
        }

        std::cout << "[>] Enter surname: ";
        std::cin >> person.surname;
        std::cout << "[>] Enter name: ";
        std::cin >> person.name;
        std::cout << "[>] Enter middle name: ";
        std::cin >> person.middle_name;
        std::cout << "[>] Enter address: ";
        std::cin >> person.address;
        std::cout << "[>] Enter profession: ";
        std::cin >> person.profession;

        write(person, path);

        std::cout << std::endl;
    }

    count(path);

    return 0;
}

void write(const Person& person, const std::string& path) {
    std::ofstream output(path, std::ios::trunc);

    output << person.surname << " ";
    output << person.name << " ";
    output << person.middle_name << " ";
    output << person.address << " ";
    output << person.profession << "\n";

    output.close();
}

void count(const std::string& path) {
    std::ifstream input(path);

    std::string text;
    std::string line;

    if (input.is_open()) {
        while (getline(input, line)) {
            text += line + '\n';
        }
    }

    std::set<std::string> professions;

    std::string element;

    for (char symbol: text) {
        if (symbol == '\n') {
            professions.insert(element);
            element = "";
        } else if (symbol == ' ') {
            element = "";
        } else {
            element += symbol;
        }
    }

    int count;
    for (const std::string& profession: professions) {
        count = 0;
        for (char symbol: text) {
            if (symbol == '\n') {
                if (element == profession) {
                    ++count;
                }
                element = "";
            } else if (symbol == ' ') {
                element = "";
            } else {
                element += symbol;
            }
        }
        std::cout << "[+] For " << profession << ": " << count;
    }
}
