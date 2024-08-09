import random


def get_rand_list(amount: int, minimum: int = -10000, maximum: int = 10000):
    return [random.randint(minimum, maximum) for _ in range(amount)]
