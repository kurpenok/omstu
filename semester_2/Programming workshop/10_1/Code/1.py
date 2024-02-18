from PIL import Image


def search_for_lilies(path: str, color: tuple) -> int:
    with Image.open(path) as image:
        pixels = image.load()
        x, y = image.size

        colors = [0 for _ in range(x)]
        
        for i in range(x):
            for j in range(y):
               rgb = pixels[i, j]
               if rgb == color:
                   colors[i] += 1

    index = colors.index(max(colors))

    return index * 1001 // x - 500
        

if __name__ == "__main__":
    path = input("[>] Enter path to image: ")
    color = tuple(map(int, input("[>] Enter RGB-form color: ").split()))

    print(search_for_lilies(path, color))

