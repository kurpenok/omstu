status = 0
limb = ""

trunk = 0
tail = 0
foot = 0
ear = 0
eye = 0
mouth = 0

while True:
    status = input("[>] Enter status: ")

    if status == "Lunch":
        break
    
    status = int(status)
    limb = input("[>] Enter limb: ")

    if limb == "trunk":
        trunk += status
    elif limb == "tail":
        tail += status
    elif limb == "foot":
        foot += status
    elif limb == "ear":
        ear += status
    elif limb == "eye":
        eye += status
    elif limb == "mouth":
        mouth += status
    else:
        print("[-] Limb not recognized")

trunk //= 1
tail //= 1
foot //= 4
ear //= 2
eye //= 2
mouth //= 1

print(min([trunk, tail, foot, ear, eye, mouth]))

