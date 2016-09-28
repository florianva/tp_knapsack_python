import self

#Calcul du profit selon une possibilite d'objets a emporter
def profit(n, p, w, b, c, beta):
    self.weight = 0
    self.z = 0
    self.n = n
    self.p = p
    self.w = w
    self.b = b
    self.c = c
    self.beta = beta

    #Pour chaque objet dans le sac
    for i in range(0, int(self.n)):
        if self.b[i] == True:

            #Calcul du poids et du profit
            self.weight = float(float(self.weight)+float(self.w[i]))
            self.z = float(float(self.z)+float(self.p[i]))

            #Si le poids depasse la contrainte
            if float(self.weight) > float(self.c):
                self.z = float(self.z) - (float(self.beta) * (float(self.weight)-float(self.c)))

    return float(self.z)

#Calcul de la penalite en fonction des profits et des poids des objets

def beta(n,p,w):

    self.r = 0
    self.m = 0
    self.n = n
    self.p = p
    self.w = w

    #On recupere le p/w le plus eleve
    for i in range(0, int(self.n)):
        self.r = float(float(self.p[i]) / float(self.w[i]))
        #print(self.r)
        if self.r > self.m:
            self.m = self.r


    return self.m

