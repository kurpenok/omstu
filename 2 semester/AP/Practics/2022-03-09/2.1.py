n = int(input())

grades = list(map(int, input().split()))

print(f"[+] Average of grades: {sum(grades) / len(grades)}")

