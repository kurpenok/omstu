// Создать класс с динамическим массивом
// Конструктор, деструктор
// Добавление счётчика чисел
// Методы добавления/удаления/подсчёта уникальных/заполнение случайными/вывод

#include <cstddef>
#include <iostream>
#include <sys/types.h>

template <typename T = int>
class vector {
    private:
        T* array;
        size_t sz;
        size_t cap;

    public:
        vector<T>(size_t s, const T& value) {
            sz = s;

            if (sz >= cap) {
                reverse(cap * 2);
            }

            new(array + sz) T(value);
        }
        ~vector<T>() {
            delete [] reinterpret_cast<u_int8_t*>(array);
        }


        size_t size() const;
        void resize(size_t newsize);

        size_t capacity() const;

        void reverse (size_t newcap) {
            if (newcap <= cap) return;

            T* newarr = reinterpret_cast<T*>(new u_int8_t[newcap * sizeof(T)]);

            for (size_t i = 0; i < sz; ++i) {
                try {
                    new(newarr+i) T(array[i]);
                } catch (...) {
                    for (size_t j = 0; j < i; ++j) {
                        (newarr+i)->~T();
                    }
                    delete [] reinterpret_cast<u_int8_t*>(newarr);
                    throw;
                }
            }

            for (size_t i = 0; i < sz; ++i) {
                (array+i)->~T();
            }

            delete [] reinterpret_cast<u_int8_t*>(array);
            cap = newcap;
            array = newarr;
        }

        void push_back(const T& value) {
            if (sz >= cap) {
                reverse(cap * 2);
            }

            new(array + sz) T(value);

            ++sz;
        }

        void pop_back() {
            --sz;
            (array+sz)->~T();
        }

        int count_unique() {
            int count = sz;
            for (size_t i = 0; i < sz; ++i) {
                for (size_t j = 0; j < sz; ++j) {
                    if (array[i] == array[j]) {
                        --count;
                        break;
                    }
                }
            }
            return count;
        }

        void show() {
            std::cout << "[+] Array: ";
            for (size_t i = 0; i < sz; ++i) {
                std::cout << array[i] << " ";
            }
            std::cout << std::endl;
        }

        struct iterator {
            private:
                T* ptr;
            public:
                T& operator*() const {
                    return *ptr;
                }
        };
};

int main() {
    vector<int> v(5, 0);
    v.push_back(1);
    v.push_back(2);
    
    return 0;
}

