import File
import Aleatoire
import HillClimber
import MarcheAleatoire

fileInName = "ks_1000.txt";
fileOutName = "hc.csv"
tabNbEval = [20, 50, 100]
repetitions = 30

#profitmax = HillClimber.getProfitMax(fileInName, 1)
for index in range(0, len(tabNbEval)):
    nbEval = tabNbEval[index]

    #Nombre de fois a executer le programme
    for i in range(0, repetitions):

        #profitmax = Aleatoire.getProfitMax(fileInName, nbEval)
        #profitmax = MarcheAleatoire.getProfitMax(fileInName, nbEval)
        profitmax = HillClimber.getProfitMax(fileInName, nbEval)

        #Ecriture de la ligne dans le fichier csv
        line = str(nbEval)+";"+str(profitmax)
        File.Write(fileOutName, line)

