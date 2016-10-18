class Knapsack:

    def __init__(self, filename):
        with open(filename, "r") as f:
            self.n = int(f.readline())
            s = f.readline().split(' ')
            self.profits = [ int(i) for i in s ]
            s = f.readline().split(' ')
            self.weights = [ int(i) for i in s ]
            self.C = int(f.readline())
            self.beta = 0
            for (p,w) in zip(self.profits, self.weights):
                if w > 0:
                    if float(p)/float(w) > self.beta:
                        self.beta = float(p)/float(w)

    def eval(self, x):
        z = 0
        w = 0
        for i in range(self.n):
            if x[i] == 1:
                z += self.profits[i]
                w += self.weights[i]
        if w <= self.C:
            return z
        else:
            t = z - self.beta * (w - self.C)
            return t

    def __str__(self):
        s = str(self.n) + "\n"
        for p in self.profits:
            s += str(p) + " "
        s += "\n"
        for w in self.weights:
            s += str(w) + " "
        s += "\n" + str(self.C)
        s += "\n" + str(self.beta)
        return(s)