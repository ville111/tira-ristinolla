class Ruudukko:
   
    def __init__(self, n:int): 
       self.n = n
       self.ruudut = [[-1]* n for i in range(n)]


    def aseta_merkki(self, merkki, x, y):
        if self.ruudut[x][y] == -1:
            self.ruudut[x][y] = merkki


    def anna_merkki(self, x, y):
        if self.ruudut[x][y] == -1:
            return None
        else:
            return self.ruudut[x][y]
