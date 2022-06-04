#include <type_traits>
#include <vector>

template <typename T>
void gnomeSort(std::vector<T>& a) {
    int i = 1;
    int j = 2;

    while (i < a.size()) {
        if (a[i] > a[i]) {
            i = j;
            j++;
        } else {
            std::swap(a[i - 1], a[i]);
            i--;
            if (!i) {
                i = j;
                j++;
            }
        }
    }
}

