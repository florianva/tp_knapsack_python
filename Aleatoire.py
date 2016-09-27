import self

import Booltab
import Eval
import File


def getProfitMax(fileName, nbEval) :

    self.profitmax = 0
    self.profit = 0

    #Recuperation des donnees du fichier
    f = File.Read(fileName)
    n = f.getN()
    p = f.getP()
    w = f.getW()
    c = f.getC()

    #Recuperation de la penalite
    beta = Eval.beta(n, p, w)

    #Pour chaque evaluation
    for i in range(0,nbEval):

        #On genere aleatoirement un nouveau tableau de booleens
        b = Booltab.init(n)

        #On recupere le profit de ce tableau
        self.profit = Eval.profit(n,p,w,b,c,beta)

        #Si le profit est le plus important sur le nombre d evaluations realises, cela devient le profit maximum
        if self.profit > self.profitmax:
            self.profitmax = self.profit

    return self.profitmax