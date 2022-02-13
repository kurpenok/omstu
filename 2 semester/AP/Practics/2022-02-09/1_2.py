name = input("[>] Enter name: ")
email = input("[>] Enter email: ")

if "@" not in name and "@" in email:
    print("[+] OK")
elif "@" not in name and "@" not in email:
    print("[-] Incorrect email")
elif "@" in name and "@" in email:
    print("[-] Incorrect login")
elif "@" in name and "@" not in email:
    print("[-] Incorrect data")

