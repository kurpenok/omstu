#ifndef CODE_VECTOR_H
#define CODE_VECTOR_H

struct Vector {
    int size = 1;
    char* symbols = new char [size];

    void add(char symbol) {
        char* new_symbols = new char [size + 1];
        for (int i = 0; i < size; ++i) {
            new_symbols[i] = symbols[i];
        }
        new_symbols[size - 1] = symbol;
        ++size;
        symbols = new_symbols;
        delete[] new_symbols;
    }

    void print() const {
        int symbols_code;

        for (int i = 0; i < size; ++i) {
            symbols_code = static_cast<int> (symbols[i]) - static_cast<int> ('\0');
            if (symbols_code < 0) {
                std::cout << symbols[i] << " ";
                // Я не смог сделать так, чтобы каждый символ выводился только один раз
                // Символ выводится с неким префиксом -47, если буква заглавная и -48, если строчная
            }
        }
    }
};

#endif
