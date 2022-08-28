from PIL import Image


def frame(path: str, width: int) -> None:
    image = Image.open(path)
    x, y = image.size
    pixels = image.load()

    rgb = [0, 0, 0]

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            rgb[0] += r
            rgb[1] += g
            rgb[2] += b

    rgb[0] //= x * y
    rgb[1] //= x * y
    rgb[2] //= x * y

    croped = image.crop((x // 3, y // 3, x - x // 3, y - y // 3))

    done = Image.new(
            "RGB",
            (x // 3 + (2 * width), y // 3 + (2 * width)),
            tuple(rgb))
    done.paste(croped, (20, 20))
    done.save("done.png")


if __name__ == "__main__":
    frame("bug.png", 20)

