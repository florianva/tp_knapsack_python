import random
import self
import Eval
import numpy as np


def init(n):
    tf = np.array([True, False])
    b = np.random.choice(tf, int(n))
    return b

def voisin(n, b):

    self.b = b
    i = random.randint(0, int(n)-1)
    b[i] = np.invert(b[i])
    return b


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

        b[i] = np.invert(b[i])

        self.profit = Eval.profit(self.n, self.p, self.w, self.b, self.c, beta)

        # Si le profit est le plus important sur le nombre d evaluations realises, cela devient le profit maximum
        if self.profit > self.profitmax:
            self.profitmax = self.profit
            self.bmax = self.b

        b[i] = np.invert(b[i])

    return self.bmax