sort = lambda array: [element for element in 
        sorted(array, key=lambda x: x["model"], reverse=True)]

if __name__ == "__main__":
    print(sort([
        {"make": "Nokia", "model": 216, "color": "black"},
        {"make": "Mi Max", "model": 2, "color": "gold"},
        {"mako": "Samsung", "model": 7, "color": "blue"}
    ]))

