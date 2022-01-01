#ifndef CODE_LIST_H
#define CODE_LIST_H

struct Node {
    char symbol;
    Node* next;

    explicit Node(char _symbol): symbol(_symbol), next(nullptr) {}
};

struct List {
    Node* first;
    Node* last;

    List(): first(nullptr), last(nullptr) {}

    [[nodiscard]] bool is_empty() const {
        return first == nullptr;
    }

    void add(char _symbol) {
        Node* p = new Node(_symbol);
        if (is_empty()) {
            first = p;
            last = p;
            return;
        }
        last->next = p;
        last = p;
    }

    void print() const {
        if (is_empty()) {
            return;
        }
        Node* p = first;

        int symbols_code;

        while (p) {
            symbols_code = static_cast<int> (p->symbol) - static_cast<int> ('\0');
            if (symbols_code < 0) {
                std::cout << p->symbol << " ";
                // Я не смог сделать так, чтобы каждый символ выводился только один раз
                // Символ выводится с неким префиксом -47, если буква заглавная и -48, если строчная
            }
            p = p->next;
        }
        std::cout << std::endl;
    }
};

#endif
