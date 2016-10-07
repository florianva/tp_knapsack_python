import self
import numpy as np

def newTab(b):

    self.b = b

    for i in range(0,len(self.b)):
        self.b[i] = np.invert(self.b[i])
        print self.b
        self.b[i] = np.invert(self.b[i])
