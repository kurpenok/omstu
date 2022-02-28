s = input()

if s.find("f") == -1:
    print(-2)
elif s.find("f", s.find("f") + 1) == -1:
    print(-1)
else:
    print(s.find("f", s.find("f") + 1))
