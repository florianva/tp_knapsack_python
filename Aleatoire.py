import Booltab
import Eval
import File


def getProfitMax(fileName, nbEval) :

    profitmax = 0
    profit = 0

    #Recuperation des donnees du fichier
    f = File.Read(fileName)
    n = f.getN()
    p = f.getP()
    w = f.getW()
    c = f.getC()

    #Recuperation de la penalite
    beta = Eval.beta(n, p, w)

    #Pour chaque evaluation
    for i in range(0, nbEval):

        #On genere aleatoirement un nouveau tableau de booleens
        b = Booltab.init(int(n))

        #On recupere le profit de ce tableau
        profit = Eval.profit(n, p, w, b, c, beta)

        #Si le profit est le plus important sur le nombre d evaluations realises, cela devient le profit maximum
        if profit > profitmax:
            profitmax = profit

    return profitmax