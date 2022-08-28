in_1 = input("[>] Enter first number: ")
in_2 = input("[>] Enter second number: ")
in_3 = input("[>] Enter third number: ")

bool_1 = in_1 == "1" or in_1 == "раз" or in_2 == "один"
bool_2 = in_2 == "2" or in_2 == "два"
bool_3 = in_3 == "3" or in_3 == "три"

if bool_1 and bool_2 and bool_3:
    print("[+] Fire")
else:
    print("[-] Not fire")

