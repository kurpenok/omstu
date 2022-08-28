from math import sqrt, sin, pi


class Liked:
    def __init__(self, *args) -> None:
        self.data = []

        for arg in args:
            for line in arg:
                self.data.append(line)

    def likes(self) -> dict:
        self.emojis = [":)", ";)", ")", ":(", ";(", "("]
        output = dict()

        for line in self.data:
            for emoji in self.emojis:
                count = line.count(emoji)
                if count:
                    if emoji in output:
                        output[emoji] += count
                    else:
                        output[emoji] = count

        return output    


class MiMiMi(Liked):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def likes(self) -> dict:
        self.emojis = [":)", ";)", ")", ":(", ";(", "("]
        output = dict()

        for line in self.data:
            if ["cat", "kitten"] in line:
                for emoji in self.emojis:
                    count = line.count(emoji)
                    if count:
                        if emoji in output:
                            output[emoji] += count
                        else:
                            output[emoji] = count

        return output


class Mosquito:
    def __init__(self, age: int) -> None:
        self.age = age

    def __str__(self) -> str:
        return f"Mosquito, {self.age} age"


class MaleMosquito(Mosquito):
    def __init__(self, age: int, lives: str) -> None:
        self.age = age
        self.lives = lives

    def __str__(self) -> str:
        return f"I hear and see everything {self.lives}"


class FemaleMosquito(Mosquito):
    def __init__(self, age: int, feed: str) -> None:
        self.age = age
        self.feed = feed

    def __str__(self) -> str:
        return f"The thin squeak of a mosquito after eating {self.feed}"


class MosquitoLarva(Mosquito):
    def __str__(self) -> str:
        return f""


class Oscillations:
    def __init__(self, a: int) -> None:
        self.a = a


class SpringPendulum(Oscillations):
    def __init__(self, a: int, m: int, k: int) -> None:
        self.a = a
        self.m = m
        self.k = k

    def period(self) -> float:
        return 2 * pi * sqrt(self.m / self.k)

    def cyclic_frequeny(self, w: int) -> float:
        return 2 * pi / w

    def __str__(self, t: int, w: int) -> str:
        return f"X = {self.a * sin(w * t)}"


class MathPendulum(Oscillations):
    def __init__(self, a: int, l: int, g: int) -> None:
        self.a = a
        self.l = l
        self.g = g

    def period(self) -> float:
        return 2 * pi * sqrt(self.l / self.g)
    
    def cyclic_frequeny(self, w: int) -> float:
        return 2 * pi / w

    def __str__(self, t: int, w: int) -> str:
        return f"X = {self.a * sin(w * t)}"


class EMPendulum(Oscillations):
    def __init__(self, a: int, l: int, c: int) -> None:
        self.a = a
        self.l = l
        self.c = c

    def period(self) -> float:
        return 2 * pi * sqrt(self.l * self.c)
    
    def cyclic_frequeny(self, w: int) -> float:
        return 2 * pi / w

    def __str__(self, t: int, w: int) -> str:
        return f"X = {self.a * sin(w * t)}"


if __name__ == "__main__":
    liked = Liked(["Hi, Kuat! :)", "Well ;)", "How are you?))"])
    print(liked.likes())

