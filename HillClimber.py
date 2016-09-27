import self

import Booltab
import Eval
import File


def getProfitMax(fileName, nbEval):

    self.profitmax = 0
    self.profit = 0

    #Recuperation des donnees du fichier
    f = File.Read(fileName)
    self.n = f.getN()
    self.p = f.getP()
    self.w = f.getW()
    self.c = f.getC()

    #Recuperation de la penalite
    beta = Eval.beta(self.n, self.p, self.w)

    #On genere aleatoirement un nouveau tableau de booleens
    self.b = Booltab.init(self.n)

    #Pour chaque evaluation
    for i in range(0, nbEval):

        self.b = Booltab.hillClimber(self.n, self.b, self.p, self.w, self.c, beta)

        #On recupere le profit de ce tableau
        self.profit = Eval.profit(self.n, self.p, self.w, self.b, self.c, beta)

        #Si le profit est le plus important sur le nombre d evaluations realises, cela devient le profit maximum
        if self.profit > self.profitmax:
            self.profitmax = self.profit

    return self.profitmax