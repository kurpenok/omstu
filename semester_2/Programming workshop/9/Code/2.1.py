from random import choices
from random import randint 

from string import digits
from string import ascii_letters
from string import ascii_lowercase
from string import ascii_uppercase


def generate_name(lenght: int) -> str:
    lenght_part_1 = randint(2, lenght - 2)
    lenght_part_2 = lenght - lenght_part_1

    part_1 = ""
    part_2 = ""
    number_index = randint(1, lenght_part_1)

    for i in range(lenght_part_1):
        if not i:
            part_1 += "".join(choices(ascii_letters))
        elif i == number_index:
            part_1 += "".join(choices(digits))
        else:
            part_1 += "".join(choices(ascii_letters + digits))

    for i in range(lenght_part_2):
        if not i:
            part_2 += "".join(choices(
                ascii_uppercase[:len(ascii_uppercase) // 2]))
        else:
            part_2 += "".join(choices(ascii_lowercase))

    return f"{part_1} {part_2}"


if __name__ == "__main__":
    print(generate_name(12))

