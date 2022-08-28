s = input()

new_s = s[s.find("h") + 1:s.rfind("h")]

while new_s.find("h") != -1:
    new_s = new_s[:new_s.find("h")] + "H" + new_s[new_s.find("h") + 1:]

print(s[:s.find("h") + 1] + new_s + s[s.rfind("h"):])
