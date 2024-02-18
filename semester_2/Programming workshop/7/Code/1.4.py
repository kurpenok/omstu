def get_triangle(rows: int) -> list:
    row = [1]
    output = []
    for _ in range(rows):
        output.append(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]
    return output

