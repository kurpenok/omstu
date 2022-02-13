from fractions import Fraction

numerator_1 = int(input("[>] Enter first numerator: "))
denominator_1 = int(input("[>] Enter first denominator: "))
numerator_2 = int(input("[>] Enter second numerator: "))
denominator_2 = int(input("[>] Enter second denominator: "))

print(f"[+] Result: {Fraction(numerator_1, denominator_1) - Fraction(numerator_2, denominator_2)}")

