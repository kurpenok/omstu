from math import ceil, log10

cost = int(input("[>] Enter cost of house: "))

print(f"[+] Count of cycle: {ceil(log10(cost))}")

