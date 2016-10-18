import random

import Eval
import numpy as np

def init(n):
    b = np.random.randint(2, size=n)
    #b = [0,1,1,0,1]
    return b

def voisin(n, b):

    b = b
    i = random.randint(0, int(n)-1)
    b[i] = np.invert(b[i])
    return b

def hillClimber(ks, blocal):

    profitmaxlocal = 0

    for i in xrange(len(blocal)):

        #blocal[i] = np.invert(blocal[i])
        if blocal[i] == 1:
            blocal[i] = 0
        else:
            blocal[i] = 1

        profitlocal = ks.eval(blocal)

        if profitlocal > profitmaxlocal:
            #bmaxlocal = np.copy(blocal)
            indice = i;
            profitmaxlocal = profitlocal

        #blocal[i] = np.invert(blocal[i])
        #print(profitmaxlocal)

        if blocal[i] == 1:
            blocal[i] = 0
        else:
            blocal[i] = 1

    #return bmaxlocal
    return indice, profitmaxlocal

