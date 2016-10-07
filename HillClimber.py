import self
import Booltab
import Eval
import File
import Hamming


def getProfitMax(fileName, nbEval):


    #Recuperation des donnees du fichier
    f = File.Read(fileName)
    self.n = f.getN()
    self.p = f.getP()
    self.w = f.getW()
    self.c = f.getC()

    #Recuperation de la penalite
    beta = Eval.beta(self.n, self.p, self.w)

    # On genere aleatoirement un nouveau tableau de booleens
    self.bmaxglobal = Booltab.init(int(self.n))

    for i in range(0,nbEval):

        #On recupere le profit de ce tableau
        self.profitmaxglobal = Eval.profit(self.n, self.p, self.w, self.bmaxglobal, self.c, beta)

        #On recupere le tableau dont le profit est le maximum avec la distance de Hamming
        self.bmaxlocal = Booltab.hillClimber(self.n,self.bmaxglobal,self.p,self.w,self.c,beta,self.profitmaxglobal)

        #On calcule le profit pour ce tableau
        self.profitmaxlocal = Eval.profit(self.n, self.p, self.w, self.bmaxlocal, self.c, beta)

        if self.profitmaxlocal > self.profitmaxglobal:
            self.profitmaxglobal = self.profitmaxlocal
            self.bmaxglobal = self.bmaxlocal
        else:
            return self.profitmaxglobal

    return self.profitmaxglobal