def borders(tl: tuple, rb: tuple, point: tuple) -> None:
    if (tl[0] == point[0] and rb[1] <= point[1] <= tl[1]) or \
            (rb[0] == point[0] and rb[1] <= point[1] <= tl[1]) or \
            (tl[1] == point[1] and tl[0] <= point[0] <= rb[0]) or \
            (rb[1] == point[1] and tl[0] <= point[0] <= rb[0]):
        print("AT THE EDGE")
    elif tl[0] <= point[0] <= rb[0] and rb[1] <= point[1] <= tl[1]:
        print("INSIDE")
    else:
        print("OUTSIDE")


if __name__ == "__main__":
    borders((1, 3), (4, 0), (2, 2))
    borders((1, 3), (4, 0), (4, 2))
    borders((1, 3), (4, 0), (4, 4))

