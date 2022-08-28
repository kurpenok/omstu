temp_house = 0

visible_houses = ""

for i in range(5):
    current_house = int(input(f"[>] Enter height of {i + 1} house: "))
    if current_house > temp_house:
        visible_houses += str(i + 1) + " "
        temp_house = current_house

print(visible_houses)

