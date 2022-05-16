sort = lambda array: [sublist for sublist in sorted(array, key=lambda x: (len(x), x[0]))]

if __name__ == "__main__":
    print(sort([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]))

