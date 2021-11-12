class Pelaaja:

    def __init__(self, merkki:str):
        self.merkki = merkki
        self.x = -1
        self.y = -1

    def aseta_piste(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def siirra(self):
        if not self.x == -1 and not self.y == -1:
            x = self.x
            y = self.y
            self.x = -1
            self.y = -1
            return self.merkki, x, y
        else:
            return None
    