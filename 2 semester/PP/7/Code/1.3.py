def get_unique(array: list) -> list:
    unique = []
    for i in array:
        if i in unique:
            unique.append(i)
    return unique

