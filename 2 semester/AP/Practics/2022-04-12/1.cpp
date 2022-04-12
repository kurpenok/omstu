#include <iostream>
#include <cmath>
#include <iterator>

class Figure {
public:
    virtual double get_perimeter() = 0;
    virtual double get_square() = 0;
    virtual int get_type() = 0;
};

class Circle: public Figure {
private:
    double radius;

public:
    Circle(double r): radius(r) {}
    
    double get_perimeter() override {
        return 2 * M_PI * radius;
    }

    double get_square() override {
        return M_PI * radius * radius;
    }

    int get_type() override {
        return 0;
    }
};

class Triangle: public Figure {
private:
    double side_a;
    double side_b;
    double side_c;

public:
    Triangle(double a, double b, double c): side_a(a), side_b(b), side_c(c) {}
    
    double get_perimeter() override {
        return side_a + side_b + side_c;
    }

    double get_square() override {
        double p = get_perimeter() / 2;
        return std::sqrt(p * (p - side_a) * (p - side_b) * (p - side_c));
    }

    int get_type() override {
        return 3;
    }
};

class Rectangle: public Figure {
private:
    double width;
    double height;

public:
    Rectangle(double w, double h): width(w), height(h) {}
    
    double get_perimeter() override {
        return 2 * (width + height);
    }

    double get_square() override {
        return width * height;
    }

    int get_type() override {
        return 4;
    }
};

int main() {
    Circle circle(10);
    std::cout << circle.get_type() << std::endl;
    std::cout << circle.get_square() << std::endl;
    std::cout << circle.get_perimeter() << std::endl <<std::endl;

    Triangle triangle(3, 4, 5);
    std::cout << triangle.get_type() << std::endl;
    std::cout << triangle.get_square() << std::endl;
    std::cout << triangle.get_perimeter() << std::endl <<std::endl;

    Rectangle rectangle(30, 40);
    std::cout << rectangle.get_type() << std::endl;
    std::cout << rectangle.get_square() << std::endl;
    std::cout << rectangle.get_perimeter() << std::endl <<std::endl;
}

