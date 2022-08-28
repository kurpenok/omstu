sort = lambda array: [sublist for sublist in sorted(array, key=lambda x: x[1])]

if __name__ == "__main__":
    print(sort([
        ("English", 88),
        ("Social", 82),
        ("Science", 90),
        ("Math", 97)
    ]))

