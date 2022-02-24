p = int(input())
x = int(input())
y = int(input())

money = x * 100 + y
money += money * (p / 100)

print(int(money // 100), int(money % 100))
