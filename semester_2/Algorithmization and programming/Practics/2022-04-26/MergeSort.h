#pragma once

#include <vector>

template<class T>
std::vector<T> merge(std::vector<T>& a, std::vector<T>& b) {
    int i = 0;
    int j = 0;

    std::vector<T> c(a.size() + b.size());

    while (i < a.size() || j < b.size()) {
        if (j == b.size() || i < a.size() && a[i] < b[j]) {
            c[i + j] = a[i];
            ++i;
        } else {
            c[i + j] = b[j];
            ++j;
        }
    }

    return c;
}

template<class T>
std::vector<T> sort(std::vector<T>& a) {
    int n = a.size();

    if (n <= 1) {
        return a;
    }

    std::vector<T> l;
    std::vector<T> r;

    for (int i = 0; i < n; ++i) {
        if (i < n / 2 + 1) {
            l.push_back(a[i]);
        } else {
            r.push_back(a[i]);
        }
    }

    return merge(l, r);
}

