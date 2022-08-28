int sum(const int *array, int &size) {
    int s = 0;
    for (int i = 0; i < size; i++) {
        if (array[i] < 0) {
            s += array[i];
        }
    }
    return s;
}
