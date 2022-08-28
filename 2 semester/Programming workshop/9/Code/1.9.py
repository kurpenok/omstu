counter = lambda array: len([i for i in array if type(i) == float])

if __name__ == "__main__":
    print(counter([1, "abcd", 3.12, 1.2, 4, "xyz", 5, "pqr", 7, -5, -12.22]))

