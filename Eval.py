
import self

#Calcul du profit selon une possibilite d'objets a emporter
def profit(n, z, w, b, c, beta):
    self.weight = 0
    self.z = 0
    self.beta = beta

    #Pour chaque objet dans le sac
    for i in range(0, int(n)):
        #Calcul du poids et du profit
        #self.weight = float(float(self.weight)+(self.b[i]*float(self.w[i])))
        self.weight = float(self.weight) +(float(w[i]) * float(b[i]))
        #self.z = float(float(self.z)+float(self.p[i]))
        self.z = self.z + (float(z[i]) * float(b[i]))

    #Si le poids depasse la contrainte
    if float(self.weight) > float(c):
        self.z = float(self.z) - (float(beta) * (float(self.weight)-float(c)))

    return float(self.z)

#Calcul de la penalite en fonction des profits et des poids des objets

def beta(n,p,w):

    self.r = 0
    self.m = 0


    #On recupere le p/w le plus eleve
    for i in range(0, int(n)):
        self.r = float(float(p[i]) / float(w[i]))
        #print(self.r)
        if self.r > self.m:
            self.m = self.r


    return self.m

