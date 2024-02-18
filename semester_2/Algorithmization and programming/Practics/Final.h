#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <map>

class Product {
public:
    std::string name;
    
    Product(std::string name) {
        this->name = name;
    }
};

class EProduct {
public:
    std::vector<std::map<Product, int>> products;
    std::string date;
    int count;

    EProduct(std::vector<std::map<Product, int>> products, std::string date) {
        this->products = products;
        this->date = date;

        this->count = products.size();
    }
};

class RProduct {
public:
    std::vector<std::map<Product, int>> products;
    std::string date;
    int count;

    RProduct(std::vector<std::map<Product, int>> products, std::string date) {
        this->products = products;
        this->date = date;

        this->count = products.size();
    }

    std::vector<std::map<Product, int>> difference(std::vector<std::map<Product, int>> eproducts) {
        std::vector<std::map<Product, int>> remains;

        for (auto eproduct: eproducts) {
            bool flag = false;
            for (auto product: products) {
                if (eproduct == product) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                remains.push_back(eproduct);
            }
        }
        return remains;
    }
};

