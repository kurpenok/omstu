const int size = 20;
const int hor = 10;
const int ver = size;

inline void newBuckets(int buckets[][ver]) {
    for(int i = 0; i < hor; i++) {
        for(int j = 0; j < ver; j++) {
            buckets[i][j] = -1;
        }
    }
}

inline void bucketSort(int array[size]) {
    int buckets[hor][ver];
    int ostatok, temp;
    int count;

    for(int x = 1; x <= 100; x *= 10) {
        newBuckets(buckets);
        count = 0;
 
        for(int i = 0; i < size; i++) {
            temp = array[i] / x;
            ostatok = temp % 10;
            buckets[ostatok][i] = array[i];
        }
 
        for(int i = 0; i < hor; i++) { 
            for(int j = 0; j < ver; j++) {
                if(buckets[i][j] != -1) {
                    array[count] = buckets[i][j];
                    count++;
                }
            }
        }
    }
}

