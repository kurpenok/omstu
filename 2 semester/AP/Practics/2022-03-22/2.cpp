#include <iostream>
#include <string>

class Doctor {
    public:
        Doctor(std::string n="Ivanov", std::string s="Ivan", std::string b="Surgery", int cat=3, std::string spec="Surgeon") {
            name = n;
            surname = s;
            branch = b;
            category = cat;
            special = spec;
        }
        ~Doctor() {}

        void show() {
            std::cout << name << surname << branch << category << special << std::endl;
        }

        std::string get_special() {
            return special;
        }

        std::string get_brach() {
            return branch;
        }
    private:
        std::string name;
        std::string surname;

        std::string branch;
        
        int category;

        std::string special;
};

int main() {
    Doctor doctor;

    return 0;
}

