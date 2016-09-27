import random

import self

import Eval


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

def hillClimber(n, b, p, w, c, beta):

    self.n = n
    self.b = b
    self.p = p
    self.w = w
    self.c = c
    self.beta = beta
    self.profit = 0
    self.profitmax = 0
    self.bmax = [None] * int(self.n)

    for i in range(0,int(self.n)):
        if self.b[i] == False:
            self.b[i] = bool(1)
        else:
            self.b[i] = bool(0)

        self.profit = Eval.profit(self.n, self.p, self.w, self.b, self.c, beta)

        # Si le profit est le plus important sur le nombre d evaluations realises, cela devient le profit maximum
        if self.profit > self.profitmax:
            self.profitmax = self.profit
            self.bmax = self.b

        if self.b[i] == False:
            self.b[i] = bool(1)
        else:
            self.b[i] = bool(0)

    return self.bmax