n = int(input())

students = {}

for i in range(n):
    student = input().split()
    students[int(student[1])] = student[0]

for key in list(sorted(students.keys(), reverse=True)):
    print(students[key])
