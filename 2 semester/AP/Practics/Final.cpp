#include <iostream>
#include <string>
#include <vector>
#include <map>

#include "Final.h"

int main() {
    Product p1("Product 1");
    Product p2("Product 2");

    std::map<Product, int> me;
    me[p1] = 1;
    me[p2] = 2;

    std::vector<std::map<Product, int>> ve;
    ve.push_back(me);
    
    Product p3("Product 3");
    Product p4("Product 4");

    std::map<Product, int> mr;
    mr[p3] = 3;
    mr[p4] = 4;

    std::vector<std::map<Product, int>> vr;
    ve.push_back(mr);

    EProduct ep(ve, "2022-05-30");
    RProduct rp(vr, "2022-05-30");

    rp.difference(ep.products);

    return 0;
}

