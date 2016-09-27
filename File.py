
class Read :
    def __init__(self, fileName):
        with open(fileName, "r") as text:
            lineTab = text.read().splitlines()
            self.n = lineTab[0]
            self.p = lineTab[1].split(" ")
            self.w = lineTab[2].split(" ")
            self.c = lineTab[3]
            #print(self.n)

    def getN(self):
        # Do something if you want
        return self.n

    def getP(self):
        # Do something if you want
        return self.p

    def getW(self):
        # Do something if you want
        return self.w

    def getC(self):
        # Do something if you want
        return self.c


class Write() :
    def __init__(self,fileName,line):
        file = open(fileName, "a")
        file.write(line+"\n")
        file.close()

