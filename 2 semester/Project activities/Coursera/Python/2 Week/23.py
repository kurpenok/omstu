i1 = int(input())
r1 = int(input())
i2 = int(input())
r2 = int(input())
i3 = int(input())
r3 = int(input())

lenght1 = r1 - i1
lenght2 = r2 - i2
lenght3 = r3 - i3
dist12 = max(i1, r1, i2, r2) - min(i1, r1, i2, r2) - lenght1 - lenght2
dist23 = max(i3, r3, i2, r2) - min(i3, r3, i2, r2) - lenght3 - lenght2
dist31 = max(i3, r3, i1, r1) - min(i3, r3, i1, r1) - lenght3 - lenght1
overlap = (dist31 <= 0) + (dist23 <= 0) + (dist12 <= 0)

if overlap >= 2:
    answer = 0
elif lenght1 >= dist23:
    answer = 1
elif lenght2 >= dist31:
    answer = 2
elif lenght3 >= dist12:
    answer = 3
else:
    answer = -1
print(answer)
