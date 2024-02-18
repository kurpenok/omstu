#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

class DeviceName {
    private:
        std::string firm;
        std::string manufacturer;
    public:
        DeviceName(std::string f, std::string m) {
            firm = f;
            manufacturer = m;
        }
        std::string get_firm() {
            return firm;
        }
        std::string get_manufacturer() {
            return manufacturer;
        }
};

class ElectronicDevice: public DeviceName {
    private:
        std::string consumption;
        int power;
        std::string dimensions;
    public:
        ElectronicDevice(std::string f, std::string m, std::string c,
                int p, std::string d):DeviceName(f, m) {
            consumption = c;
            power = p;
            dimensions = d;
        }
        std::string get_consumption() {
            return consumption;
        }
        int get_power() {
            return power;
        }
        std::string get_dimensions() {
            return dimensions;
        }
};

class MechanicalDevice: public DeviceName {
    private:
        std::string drive;
        std::string dimensions;
        int cost;
    public:
        MechanicalDevice(std::string f, std::string m, std::string d,\
                std::string dim, int c):DeviceName(f, m) {
            drive = d;
            dimensions = dim;
            cost = c;
        }
        std::string get_drive() {
            return drive;
        }
        std::string get_dimensions() {
            return dimensions;
        }
        int get_cost() {
            return cost;
        }
};

int average_mechanical(
        std::vector<MechanicalDevice>& mechanicals);

std::vector<ElectronicDevice> find_by_consumption(
        std::vector<ElectronicDevice>& electronics,
        std::string consumption);

std::vector<MechanicalDevice> find_by_cost(
        std::vector<MechanicalDevice>& mechanicals,
        int cost);

std::vector<std::string> find_by_dimensions(
        std::vector<ElectronicDevice>& electronics,
        std::vector<MechanicalDevice>& mechanicals,
        std::string dimensions);


// Main method
int main() {
    std::vector<ElectronicDevice> electronics;
    std::vector<MechanicalDevice> mechanicals;

    int n;
    std::cout << "[>] Enter count of electronic devices: ";
    std::cin >> n;

    std::string firm;
    std::string manufacturer;

    std::string consumption;
    int power;
    std::string dimensions;

    for (int i = 0; i < n; i++) {
        std::cin >> consumption >> power >> dimensions;
        electronics.push_back(ElectronicDevice(
            firm,
            manufacturer,
            consumption,
            power,
            dimensions
        ));
    }

    std::cout << "[>] Enter count of mechanical devices: ";
    std::cin >> n;

    std::string drive;
    int cost;

    for (int i = 0; i < n; i++) {
        std::cin >> drive >> dimensions >> cost;
        mechanicals.push_back(MechanicalDevice(
            firm,
            manufacturer,
            drive,
            dimensions,
            cost
        ));
    }

    std::cout << "[+] Average mechanical: " << average_mechanical(mechanicals) << std::endl;
    
    std::cout << "[>] Enter consumption: ";
    std::cin >> consumption;
    std::vector<ElectronicDevice> by_consumption = find_by_consumption(
            electronics,
            consumption
    );

    std::cout << "[>] Enter cost: ";
    std::cin >> cost;
    std::vector<MechanicalDevice> by_cost = find_by_cost(
            mechanicals,
            cost
    );

    std::cout << "[>] Enter dimensions: ";
    std::cin >> dimensions;
    std::vector<std::string> by_dimensions = find_by_dimensions(
            electronics,
            mechanicals,
            dimensions
    );

    return 0;
}


int average_mechanical(
        std::vector<MechanicalDevice>& mechanicals) {
    int amount = 0;

    for (int i = 0; i < mechanicals.size(); i++) {
        amount += mechanicals[i].get_cost();
    }

    return amount / mechanicals.size();
}

std::vector<ElectronicDevice> find_by_consumption(
        std::vector<ElectronicDevice>& electronics,
        std::string consumption) {
    std::vector<ElectronicDevice> result;

    for (int i = 0; i < electronics.size(); i++) {
        if (electronics[i].get_consumption() == consumption) {
            result.push_back(electronics[i]);
        }
    }

    return result;
}

std::vector<MechanicalDevice> find_by_cost(
        std::vector<MechanicalDevice>& mechanicals,
        int cost) {
    std::vector<MechanicalDevice> result;

    for (int i = 0; i < mechanicals.size(); i++) {
        if (mechanicals[i].get_cost() == cost) {
            result.push_back(mechanicals[i]);
        }
    }

    return result;
}

std::vector<std::string> find_by_dimensions(
        std::vector<ElectronicDevice>& electronics,
        std::vector<MechanicalDevice>& mechanicals,
        std::string dimensions) {
    
    std::vector<std::string> result;

    for (int i = 0; i < electronics.size(); i++) {
        if (electronics[i].get_dimensions() == dimensions) {
            result.push_back(electronics[i].get_firm());
        }
    }

    for (int i = 0; i < mechanicals.size(); i++) {
        if (mechanicals[i].get_dimensions() == dimensions) {
            result.push_back(mechanicals[i].get_firm());
        }
    }

    return result;
}

