finder = lambda array: max(list(sorted([i for i in array if str(i).isdigit()])))

if __name__ == "__main__":
    print(finder(["Python", 3, 2, 4, 5, "version"]))

