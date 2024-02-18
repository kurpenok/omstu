sort = lambda array: [list(sorted(sublist)) for sublist in array]

if __name__ == "__main__":
    print(sort([
        ["green", "orange"],
        ["black", "white"],
        ["white", "black", "orange"]
    ]))

