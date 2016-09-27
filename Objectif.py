import File
import Aleatoire

fileInName = "ks_1000.txt";
fileOutName = "hc.csv"
tabNbEval = [100, 200, 300, 400, 500]
repetitions = 20


for index in range(0, len(tabNbEval)):
    nbEval = tabNbEval[index]

    #Nombre de fois a executer le programme
    for i in range(0, repetitions):

        profitmax = Aleatoire.getProfitMax(fileInName, nbEval)

        #Ecriture de la ligne dans le fichier csv
        line = str(nbEval)+";"+str(profitmax)
        File.Write(fileOutName, line)

