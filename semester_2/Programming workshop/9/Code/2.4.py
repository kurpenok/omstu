import pymorphy2


def get_nouns(lines: list) -> list:
    morph = pymorphy2.MorphAnalyzer()
    
    numbers = []
    nouns = []
    
    for string in lines:
        words = string.split()
        for word in words:
            parser = morph.parse(word)[0]
            if word.isdigit():
                numbers.append(int(word))
            elif "NOUN" in parser.tag:
                nouns.append(morph.parse(word)[0].normal_form)

    result = []

    for number, noun in zip(numbers, nouns):
        comment = morph.parse(noun)[0]
        result.append(f"{number} {comment.make_agree_with_number(number).word}")

    return result


if __name__ == "__main__":
    print(get_nouns(["варкалось шорька пырялись 1"]))

