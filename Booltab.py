import random

import self


def init(n):

    b = [None]*int(n)
    for i in range(0, int(n)):
        b[i] = bool(random.getrandbits(1))

    return b

def voisin(n, b):

    self.b = b
    i = random.randint(0, int(n)-1)
    if self.b[i] == False:
        self.b[i] = bool(1)
    else:
        self.b[i] = bool(0)
    return self.b