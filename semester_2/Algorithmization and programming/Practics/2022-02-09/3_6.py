status = 0

x = y = 0

while True:
    action = input("[>] Enter action: ")
    if action == "STOP":
        break
    if action == "Right":
        status = (status + 1) % 4
    elif action == "Left":
        status = (status - 1) % 4
    elif action == "Step":
        if status == 0:
            x += 0
            y += 1
        elif status == 1:
            x += 1
            y += 0
        elif status == 2:
            x += 0
            y -= 1
        elif status == 3:
            x -= 1
            y += 0

print(f"[+] Current coords: ({x}, {y})")

