with open("input.txt", "r", encoding="utf-8") as data:
    k = int(data.readline())
    text = data.readlines()

students = {}
points = []

for line in text:
    student = line.split()
    p1, p2, p3 = int(student[-3]), int(student[-2]), int(student[-1])

    if p1 >= 40 and p2 >= 40 and p3 >= 40:
        students[student[0]] = [p1, p2, p3]
        points.append(p1 + p2 + p3)

points.sort(reverse=True)

if len(points) <= k:
    print(0)
else:
    if points[k - 1] == points[k]:
        d = k - 1
        while d > 0 and points[d - 1] == points[d]:
            d = d - 1
        if d == 0:
            print(1)
        else:
            print(points[d - 1])
    else:
        print(points[k - 1])
