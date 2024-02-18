const int n = 10;

inline int velich_radix(int number, int radix) {
    while(radix > 1) {
        number /= 10;
        radix--;
    }

    return number % 10;
}
 
inline void radixSort(int dop_mas[n][n], int mas[n], int radix) {
    int mas_col[n];
    int i;
    int j;
    int temp = 0;

    for(i=0; i<n; i++) {
        mas_col[i] = 0;
    }
    
    for(i = 0; i < n; i++) {
        int a = velich_radix(mas[i], radix);
        dop_mas[mas_col[a]][a] = mas[i];
        mas_col[a]++;
    }

    for(i = 0; i < n; i++) {
        for(j = 0; j < mas_col[i]; j++) {
            mas[temp] = dop_mas[j][i];
            temp++;
        }
    }
}

