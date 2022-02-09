in_1 = input()
in_2 = input()
in_3 = input()

bool_1 = in_1 == "1" or in_1 == "раз" or in_2 == "один"
bool_2 = in_2 == "2" or in_2 == "два"
bool_3 = in_3 == "3" or in_3 == "три"

if bool_1 and bool_2 and bool_3:
    print("ГОРИ")
else:
    print("НЕ ГОРИ")

