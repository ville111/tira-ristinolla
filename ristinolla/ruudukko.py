

class Ruudukko:
    """ Tämä luokka pitää kirjaa pelin ruudukosta: mitkä ruudut
        ovat tyhjiä ja missä on pelaajien merkit.
    """

    def __init__(self, n:int):
        self.n = n
        self.ruudut = [[-1]* n for i in range(n)]


    def aseta_merkki(self, merkki, x, y):
        if self.ruudut[x][y] == -1:
            self.ruudut[x][y] = merkki


    def anna_merkki(self, x, y):
        if self.ruudut[x][y] == -1:
            return None
        return self.ruudut[x][y]


    def viiden_suora(self, merkki):
        n = self.n
        for i in range (n):
            for j in range(n):
                if i + 4 < n and (self.ruudut[i][j] == merkki and \
                    self.ruudut[i+1][j] == merkki and \
                    self.ruudut[i+2][j]  == merkki and \
                    self.ruudut[i+3][j]  == merkki  and \
                    self.ruudut[i+4][j] == merkki):
                    return True
                elif j + 4 < n and (self.ruudut[i][j] == merkki and \
                        self.ruudut[i][j+1] == merkki and \
                        self.ruudut[i][j+2]  == merkki and \
                        self.ruudut[i][j+3]  == merkki  and \
                        self.ruudut[i][j+4] == merkki):
                    return True
                elif i + 4 < n and j + 4 < n and (self.ruudut[i][j] == merkki and \
                        self.ruudut[i+1][j+1] == merkki and \
                        self.ruudut[i+2][j+2]  == merkki and \
                        self.ruudut[i+3][j+3]  == merkki  and \
                        self.ruudut[i+4][j+4] == merkki):
                    return True
                elif i + 4 < n and j - 4 >= 0 and (self.ruudut[i][j] == merkki and \
                        self.ruudut[i+1][j-1] == merkki and \
                        self.ruudut[i+2][j-2]  == merkki and \
                        self.ruudut[i+3][j-3]  == merkki  and \
                        self.ruudut[i+4][j-4] == merkki):
                    return True
        return False
