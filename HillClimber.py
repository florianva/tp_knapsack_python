
from numpy.core.tests.test_mem_overlap import xrange
import numpy as np


class Bestimprovement :

    def __init__(self, ks, nbEval):
        self.ks = ks
        self.nbEval = nbEval
        for i in xrange(self.ks.n):
            print(i)
            self.tab_indice = i





    def getProfitMax(self):



        profitmaxglobal = 0


        bmaxglobal = np.random.randint(2, size=self.ks.n)



        for i in xrange(self.nbEval):

            #On recupere le profit de ce tableau
            profitmaxglobal = self.ks.eval(bmaxglobal)



            indice, profitmaxlocal = self.Hamming2(bmaxglobal)
            print(profitmaxlocal)


            if profitmaxlocal > profitmaxglobal:
                profitmaxglobal = profitmaxlocal

                if bmaxglobal[indice] == 1:
                    bmaxglobal[indice] = 0
                else:
                    bmaxglobal[indice] = 1
                #bmaxglobal[indice] = 1 - bmaxglobal[indice]

            else:
                return profitmaxglobal
        #print(profitmaxglobal)

        return profitmaxglobal



    def Hamming(self,blocal):
        profitmaxlocal = 0

        for i in xrange(len(blocal)):

            #blocal[i] == 1 - blocal[i]
            if blocal[i] == 1:
                blocal[i] = 0
            else:
                blocal[i] = 1


            profitlocal = self.ks.eval(blocal)
            #print(profitlocal)

            if profitlocal > profitmaxlocal:
                indice = i;
                #print(i)
                profitmaxlocal = profitlocal


            #blocal[i] == 1 - blocal[i]
            if blocal[i] == 1:
                blocal[i] = 0
            else:
                blocal[i] = 1

        return indice, profitmaxlocal

    def Hamming2(self, blocal):
        profitmaxlocal = -1
        profitlocal = self.ks.eval(blocal)
        j = 0
        i = 0

        while(profitlocal <= profitmaxlocal & j < self.ks.n):

            i = self.RandomIndice(j)

            # blocal[i] == 1 - blocal[i]
            if blocal[i] == 1:
                blocal[i] = 0
            else:
                blocal[i] = 1

            profitlocal = self.ks.eval(blocal)
            # print(profitlocal)


            if blocal[i] == 1:
                blocal[i] = 0
            else:
                blocal[i] = 1

            j += 1
        return i, profitmaxlocal

    def RandomIndice(self, j):
        r = np.random.randint(self.ks.n - j)
        i = self.tab_indice[r]
        self.tab_indice[r] = self.tab_indice[self.ks.n-j-1]
        self.tab_indice[self.ks.n - j - 1] = i
        return i