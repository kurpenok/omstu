from time import sleep
from math import sqrt

def get_sqrt(number: int, pause: int) -> float:
    sleep(pause / 1000)
    return sqrt(number)

