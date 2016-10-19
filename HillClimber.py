

import numpy as np


class Bestimprovement :

    def __init__(self, ks, nbEval):
        self.ks = ks
        self.nbEval = nbEval
        self.tab_indice = [i for i in range(self.ks.n)]





    def getProfitMax(self):



        profitmaxglobal = 0


        bmaxglobal = np.random.randint(2, size=self.ks.n)



        for i in xrange(self.nbEval):

            #On recupere le profit de ce tableau
            p = self.ks.eval(bmaxglobal)
            if p > 0 :
                profitmaxglobal = p



            ind, profitmaxlocal = self.Hamming2(bmaxglobal)
            print(profitmaxlocal)

            if ind > -1 :
                if profitmaxlocal > profitmaxglobal:
                    profitmaxglobal = profitmaxlocal

                    if bmaxglobal[ind] == 1:
                        bmaxglobal[ind] = 0
                    else:
                        bmaxglobal[ind] = 1
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
                indice = i
                #print(i)
                profitmaxlocal = profitlocal
            else:
                indice = -1


            #blocal[i] == 1 - blocal[i]
            if blocal[i] == 1:
                blocal[i] = 0
            else:
                blocal[i] = 1

        return indice, profitmaxlocal

    def Hamming2(self, blocal):
        profitmaxlocal = 0
        profitlocal = -1
        j = 0
        i = 0
        #print("profitmaxlocal : ")
        #print(profitmaxlocal)
        for i in xrange(len(blocal)):
        #while(profitlocal <= profitmaxlocal & j < self.ks.n):

            ind = self.RandomIndice(j)

            # blocal[i] == 1 - blocal[i]
            if blocal[ind] == 1:
                blocal[ind] = 0
            else:
                blocal[ind] = 1

            profitlocal = self.ks.eval(blocal)

            #print("profitlocal : ")
            #print(profitlocal)

            if profitlocal > profitmaxlocal:
                indice = ind
                # print(i)
                profitmaxlocal = profitlocal
               # print(profitmaxlocal)


            if blocal[ind] == 1:
                blocal[ind] = 0
            else:
                blocal[ind] = 1

            j += 1
        return indice, profitmaxlocal

    def RandomIndice(self, j):
        r = np.random.randint(self.ks.n - j)
        i = self.tab_indice[r]
        self.tab_indice[r] = self.tab_indice[self.ks.n-j-1]
        self.tab_indice[self.ks.n - j - 1] = i
        return i