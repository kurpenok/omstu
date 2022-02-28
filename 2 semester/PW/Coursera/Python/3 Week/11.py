s = input()

if s.find("f") == -1:
    pass
elif s.find("f", s.find("f") + 1) == -1:
    print(s.find("f"))
else:
    print(s.find("f"), s.rfind("f"))
