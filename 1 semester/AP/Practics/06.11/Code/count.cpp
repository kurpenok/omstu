int count(const int *array, int &size) {
    int c = 0;
    for (int i = 0; i < size; i++) {
        if (array[i] % 2) {
            c++;
        }
    }
    return c;
}
