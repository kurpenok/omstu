#!/usr/bin/env python3

import numpy as np


def main() -> None:
    my_array = np.arange(10, 70, 2)
    print("[+] Array:")
    print(my_array, end="\n\n")

    a = my_array.reshape(6, 5).transpose()
    print("[+] Matrix from array:")
    print(a, end="\n\n")

    a = a * 2.5
    a = a - 5
    print("[+] Matrix before transformation:")
    print(a, end="\n\n")

    b = np.random.uniform(0, 10, size=(6, 3))
    print("[+] Matrix B:")
    print(b, end="\n\n")

    a_vector = np.sum(a, axis=1)
    print("[+] Size of vector A:", len(a_vector), end="\n\n")

    b_vector = np.sum(b, axis=0)
    print("[+] Size of vector B:", len(b_vector), end="\n\n")

    multiply_ab = np.dot(a, b)
    print("[+] Multiply of A and B:")
    print(multiply_ab, end="\n\n")

    a = np.delete(a, 2, axis=1)
    print("[+] Matrix A before delete third column:")
    print(a, end="\n\n")

    b = b.transpose()
    b = np.concatenate((b, (np.random.randint(10, 20, (3, 6)))))
    b = b.transpose()
    print("[+] Matrix B before appended three columns:")
    print(b, end="\n\n")

    det_a = np.linalg.det(a)
    print("[+] Determinant A:", det_a)
    
    if det_a:
        reverse_a = np.linalg.inv(a)
        print("[+] Reverse matrix A:")
        print(reverse_a, end="\n\n")

    det_b = np.linalg.det(b)
    print("[+] Determinant B:", det_b)

    if det_b:
        reverse_b = np.linalg.inv(b)
        print("[+] Reverse matrix B:")
        print(reverse_b, end="\n\n")

    a = np.linalg.matrix_power(a, 6)
    print("[+] Matrix A:")
    print(a, end="\n\n")

    b = np.linalg.matrix_power(b, 14)
    print("[+] Matrix B:")
    print(b, end="\n\n")

    a = np.array([
        [1, -4, 2, 1.4],
        [2, -3.5, 9, 0],
        [7, 5, -4, 3],
        [1, 2, 3, 4],
    ])
    b = np.array([20, 7.8, -6, 6])
    solution = np.linalg.solve(a, b)
    print("[+] Solution of SLAU:", solution)


if __name__ == "__main__":
    main()
