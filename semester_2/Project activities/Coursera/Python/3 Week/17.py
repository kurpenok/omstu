s = input()

while s.find("@") != -1:
    s = s[:s.find("@")] + s[s.find("@") + 1:]

print(s)
