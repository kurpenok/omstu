#include <iostream>
#include <string>
#include <vector>

class Holiday {
    private:
        std::string date;
        std::string name;
        std::string about;
    public:
        Holiday(std::string d, std::string n, std::string a) {
            date = d;
            name = n;
            about = a;

            std::string month = this->get_month();

            if (std::stoi(month) < 1 && std::stoi(month) > 12) {
                return;
            }
        }
        ~Holiday() {}

        std::string get_name() {
            return name;
        }

        std::string get_month() {
            std::string month = "";
            month += date[3];
            month += date[4];
            return month;
        }
};

void find(std::vector<Holiday>& holidays, std::string month);

int main() {
    std::vector<Holiday> holidays;
    
    holidays.push_back(Holiday("01-01", "New Year", "Happy"));
    holidays.push_back(Holiday("23-02", "Red Army Day", "Brutal"));
    
    if (holidays.size() > 0) {
        find(holidays, "01");
    }

    return 0;
}

void find(std::vector<Holiday>& holidays, std::string month) {
    std::cout << "[+] Find: ";
    for (int i = 0; i < holidays.size(); i++) {
        if (holidays[i].get_month() == month) {
            std::cout << holidays[i].get_name() << "; ";
        }
    }
    std::cout << std::endl;
}

