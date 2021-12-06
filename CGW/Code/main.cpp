#include <ncurses.h>

#include "modules.h"

int main() {
    char points[6][30] = {
            "[1] Show author",
            "[2] Solve the equation",
            "[3] Show a table of values",
            "[4] Calculate the integral",
            "[5] Build a graph",
            "[6] Exit"
    };

    int status = 0;

    initscr();
    curs_set(0);
    keypad(stdscr, true);

    start_color();
    init_pair(1, COLOR_YELLOW, COLOR_BLACK);
    init_pair(2, COLOR_WHITE, COLOR_BLACK);

    while (true) {
        clear();

        for (int i = 0; i < 6; i++) {
            if (i == status) {
                attron(COLOR_PAIR(1));
            } else {
                attron(COLOR_PAIR(2));
            }
            printw("%s\n", points[i]);
        }

        switch (getch()) {
            case KEY_UP:
                if (status)
                    status--;
                break;
            case KEY_DOWN:
                if (status != 5)
                    status++;
                break;
            case '\n':
                switch (status) {
                    case 0:
                        print_author();
                        break;
                    case 1:
                        print_equation();
                        break;
                    case 2:
                        print_table();
                        break;
                    case 3:
                        print_integral();
                        break;
                    case 4:
                        print_graph();
                        break;
                    case 5:
                        endwin();
                        return 0;
                }
        }
    }
}
