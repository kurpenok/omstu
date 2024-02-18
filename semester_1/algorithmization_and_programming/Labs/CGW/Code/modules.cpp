#include <cmath>

#include <ncurses.h>

double f_1(double x) {
    return 5 * pow(x, 2) - 2 * x * log(x) - 7;
}

double f_2(double x) {
    return pow(x, 2) * atan(x);
}

double find_root(double a, double b, double epsilon) {
    while(fabs(b - a) > epsilon) {
        a = b - (b - a) * f_1(b) / (f_1(b) - f_1(a));
        b = a - (a - b) * f_1(a) / (f_1(a) - f_1(b));
    }
    return b;
}

void print_author() {
    clear();
    printw("[+] Author: Kurpenov Kuat");
    getch();
}

void print_equation() {
    clear();
    printw("[+] Equation: 5x^2 - 2xlnx - 7 = 0\n");
    printw("[+] Solve of equation: %f\n", find_root(1, 2, 0.001));
    getch();
}

void print_table() {
    clear();

    printw("[+] Table of values\n\n");

    printw("+---------+---------+---------+\n");
    printw("|    X    |   Y_1   |   Y_2   |\n");
    printw("+---------+---------+---------+\n");

    double x = 1;

    for (int i = 0; i < 10; ++i) {
        printw("|  %+.2f  |  %+.2f  |  %+.2f  |\n", x, f_1(x), f_2(x));
        x += 0.1;
    }
    printw("+---------+---------+---------+\n");

    getch();
}

void print_integral_rectangle() {
    clear();

    double a = 1;
    double b = 2;
    double n = 100;

    double h = (b - a) / n;

    double result = 0;

    for(int i = 0; i < n; i++) {
        result += f_2(a + h * (i + 0.5));
    }

    result *= h;

    printw("[+] Equation: x^2 * arctg(x)dx\n");
    printw("[+] Integral [1, 2]: %f\n", result);

    getch();
}

void print_integral_trapezoid() {
    clear();

    double a = 1;
    double b = 2;
    double n = 100;

    double h = (b - a) / n;

    double result = h * (f_2(a) + f_2(b)) / 2.0;

    for (int i = 1; i < n; ++i) {
        result += h * f_2(a + h * i);
    }

    printw("[+] Equation: x^2 * arctg(x)dx\n");
    printw("[+] Integral [1, 2]: %f\n", result);

    getch();
}

void print_graph() {
    clear();

    double x = 2;
    double y;

    printw("[+] Equation: 5x^2 - 2xlnx - 7 = 0\n\n");

    for (int i = -5; i < 6; ++i) {
        y = static_cast<int> (f_1(x) * 10);
        if (!i) {
            addch('+');
        } else {
            addch('|');
        }

        for (int j = 0; j < 40; ++j) {
            if (y > -30 && y < 100) {
                if (j == static_cast<int> (x * 10)) {
                    addch('*');
                } else {
                    if (!i) {
                        addch('-');
                    } else {
                        addch(' ');
                    }
                }
            } else {
                if (!i) {
                    if (j == 39) {
                        addch('>');
                    } else {
                        addch('-');
                    }
                } else {
                    addch(' ');
                }
            }
        }
        addch('\n');
        x -= 0.1;
    }

    x = 2;

    printw("\n[+] Equation: x^2 * arctg(x)dx\n\n");

    for (int i = -5; i < 6; ++i) {
        y = static_cast<int> (f_2(x) * 10);
        if (!i) {
            addch('+');
        } else {
            addch('|');
        }

        for (int j = 0; j < 40; ++j) {
            if (y > -30 && y < 100) {
                if (j == static_cast<int> (x * 10)) {
                    addch('*');
                } else {
                    if (!i) {
                        addch('-');
                    } else {
                        addch(' ');
                    }
                }
            } else {
                if (!i) {
                    if (j == 39) {
                        addch('>');
                    } else {
                        addch('-');
                    }
                } else {
                    addch(' ');
                }
            }
        }
        addch('\n');
        x -= 0.1;
    }

    getch();
}
