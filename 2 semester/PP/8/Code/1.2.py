def numerals(number: int) -> str:
    comparison = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "20": "Twenty",
        "30": "Thirty",
        "40": "Forty",
        "50": "Fifty",
        "60": "Sixty",
        "70": "Seventy",
        "80": "Eighty",
        "90": "Ninety",
        "100": "Hundred"
    }

    n = str(number)

    if n in comparison.keys():
        return comparison[n]
    else:
        digit_1 = n[0] + "0"
        digit_2 = n[1]
        return f"{comparison[digit_1]}-{comparison[digit_2]}"


if __name__ == "__main__":
    print(numerals(30))
    print(numerals(99))

