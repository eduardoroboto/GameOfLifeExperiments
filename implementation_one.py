import random


def create_grid(size: int) -> list:
    f = int(size/2)
    return [random.sample([0]*f+[1]*f,f*2) for _ in range(size)]
