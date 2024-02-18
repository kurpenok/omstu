with open("input.txt", "r", encoding="utf-8") as data:
    text = data.readlines()

students = {}

for line in text:
    student = line.split()
    students[student[0]] = student[1:]

for student in list(sorted(students.keys())):
    print(student, students[student][0], students[student][-1])
