import random


def init(n):

    b = [None]*int(n)
    for i in range(0, int(n)):
        b[i] = bool(random.getrandbits(1))

    return b