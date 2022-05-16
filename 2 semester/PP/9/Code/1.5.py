if __name__ == "__main__":
    count = int(input("[>] Enter count of students: "))

    students = dict()

    for i in range(count):
        name = input("[>] Enter name: ")
        estimation = int(input("[>] Enter estimation: "))
        students[name] = estimation

    print(f"[+] Second minimal: {list(sorted(students.keys()))[1]}")

