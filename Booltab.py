import random
import self
import Eval
import numpy as np

def init(n):
    b = np.random.randint(2, size=n)
    #b = [0,1,1,0,1]
    return b

def voisin(n, b):

    self.b = b
    i = random.randint(0, int(n)-1)
    b[i] = np.invert(b[i])
    return b

def hillClimber(n, bmaxglobal, p, w, c, beta, profitmaxglobal):

    self.n = n
    self.p = p
    self.w = w
    self.c = c
    self.beta = beta
    self.profitmaxlocal = 0
    self.profitmaxglobal = profitmaxglobal
    self.bmaxglobal = bmaxglobal
    self.i = -1
    self.blocal = np.copy(bmaxglobal)

    for i in range(0, len(self.blocal)):

        #self.blocal[i] = np.invert(self.blocal[i])
        if self.blocal[i] == 1:
            self.blocal[i] = 0
        else:
            self.blocal[i] = 1

        self.profitlocal = Eval.profit(self.n, self.p, self.w, self.blocal, self.c, beta)

        if self.profitlocal > self.profitmaxlocal:
            self.bmaxlocal = np.copy(self.blocal)
            self.profitmaxlocal = self.profitlocal

        #self.blocal[i] = np.invert(self.blocal[i])

        if self.blocal[i] == 1:
            self.blocal[i] = 0
        else:
            self.blocal[i] = 1

    return self.bmaxlocal


    #for i in range(0,int(self.n)):
    #while ((self.profit < self.profitmax) & (self.i < self.n)):
     #   self.i = self.i + 1
      #  self.b[self.i] = np.invert(self.b[self.i])
       # self.profit = Eval.profit(self.n, self.p, self.w, self.b, self.c, beta)

        # Si le profit est le plus important sur le nombre d evaluations realises, cela devient le profit maximum
#        if self.profit > self.profitmax:
 #          self.profitmax = self.profit
  #          self.bmax = self.b


   # self.b[self.i] = np.invert(self.b[self.i])


#    return self.bmax

