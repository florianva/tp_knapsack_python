import time

import File
import Aleatoire
import HillClimber
import MarcheAleatoire
from Eval import Knapsack

if __name__ == '__main__':

    fileInName = "ks_2000.txt"
    ks = Knapsack(fileInName)

#    x = [ 0, 1, 0, 0, 1]
#    print x, ks.eval(x)

#    x = [ 0, 0, 1, 1, 0]
#    print x, ks.eval(x)



    fileOutName = "time_best_2000.csv"
    tabNbEval = [10,20,50,100,200,500,1000]
    repetitions = 1



    #profitmax = HillClimber.getProfitMax(fileInName, 1)
    for index in xrange(len(tabNbEval)):
        nbEval = tabNbEval[index]
        hc = HillClimber.Bestimprovement(ks, nbEval)
        #t1 = int(round(time.time() * 1000))
        t1 = time.time()

        #Nombre de fois a executer le programme
        for i in xrange(repetitions):

            #profitmax = Aleatoire.getProfitMax(fileInName, nbEval)
            #profitmax = MarcheAleatoire.getProfitMax(fileInName, nbEval)
            profitmax = hc.getProfitMax()
            #t2 = int(round(time.time() * 1000))
            t2 = time.time()
            tt = t2 - t1
            print("write : ")
            print(profitmax)
            print("temps (s) :")
            print(t2-t1)
            #Ecriture de la ligne dans le fichier csv
            #line = str(nbEval)+";"+str(profitmax)
            line = str(nbEval)+";"+str(tt)
            File.Write(fileOutName, line)

