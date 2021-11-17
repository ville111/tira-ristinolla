import copy


class Tietokonepelaaja():
    def __init__(self, merkki:str, nimi:str, ruudukko):
        self.merkki = merkki
        self.nimi = nimi
        self.ruudukko = ruudukko
        self.x = -1
        self.y = -1


    def aseta_piste(self, x:int, y:int):
        self.x = x
        self.y = y


    def siirra(self):
        if not self.x == -1 and not self.y == -1:
            print("siirretään")
            ruudut = copy.deepcopy(self.ruudukko.ruudut)
            siirrot =  self.mahdolliset_siirrot(ruudut)
            print("mahdolliset siirrot", siirrot)
            paras_siirto = None
            paras_arvo = -1
            
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = self.merkki
                uusi_arvo = self.minimax(tmp_ruudut, 0, 2, True)
                if uusi_arvo > paras_arvo:
                    paras_arvo = uusi_arvo
                    paras_siirto = siirto
            x, y = paras_siirto
            self.x = -1
            self.y = -1
            print("paras siirto", paras_siirto)
            print("ruudukko", self.ruudukko.ruudut)
            return self.merkki, x, y
        return None


    def mahdolliset_siirrot(self, ruudut):
        n = len(ruudut)
        vapaat = []

        for i in range(n):
            for j in range(n):
                if ruudut[i][j] != -1:
                    min_x = max(0, i-1)
                    min_y = max(0,j-1)
                    max_x = min(i+1, n-1)
                    max_y = min(j+1,n-1)
                    for a in range (min_x, max_x):
                        for b in range (min_y, max_y):
                            if ruudut[a][b] == -1:
                                if (a,b) not in vapaat:
                                    vapaat.append((a,b))
        return vapaat


    def pisteyta(self, ruudut):
        n = len(ruudut)
        for i in range (n):
            for j in range(n):
                if ruudut[i][j] == -1:
                    continue
                if i + 4 < n and (ruudut[i][j] == ruudut[i+1][j] and \
                    ruudut[i+1][j] == ruudut[i+2][j]):
                    if ruudut[i+2][j]  == ruudut[i+3][j] and \
                    ruudut[i+3][j]  == ruudut[i+4][j]:
                        return 3
                    return 10
                elif j + 4 < n and (ruudut[i][j] == ruudut[i][j+1] and \
                    ruudut[i][j+1] == ruudut[i][j+2]):
                    if ruudut[i][j+2]  == ruudut[i][j+3] and \
                    ruudut[i][j+3]  == ruudut[i][j+4]:
                        return 3
                    return 10
                elif i + 4 < n and j + 4 < n and (ruudut[i][j] == ruudut[i+1][j+1] and \
                    ruudut[i+1][j+1] == ruudut[i+2][j+2]):
                    if ruudut[i+2][j+2]  == ruudut[i+3][j+3] and \
                    ruudut[i+3][j+3]  == ruudut[i+3][j+4]:
                        return 3
                    return 10
                elif i + 4 < n and j - 4 >= 0 and (ruudut[i][j] == ruudut[i+1][j-1] and \
                    ruudut[i+1][j-1] == ruudut[i+2][j-2]):
                    if ruudut[i+2][j-2]  == ruudut[i+3][j-3] and \
                    ruudut[i+3][j-3]  == ruudut[i+3][j-4]:
                        return 3
                    return 10
        return 0


    def minimax(self,ruudut, syvyys, maks_syvyys, maksimoija):
        siirrot = self.mahdolliset_siirrot(ruudut)

        if syvyys == maks_syvyys or len(siirrot) == 0:
            pisteet = self.pisteyta(ruudut) 
            if not maksimoija:
                pisteet = -1 * pisteet
            return pisteet
    
        if maksimoija:   
            paras_arvo = -1000       
            merkki = 1
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = merkki
                paras_arvo = max(paras_arvo, self.minimax(tmp_ruudut, syvyys+1, maks_syvyys, False))        
            return paras_arvo
        else:
            paras_arvo = 1000
            merkki = 0
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = merkki
                paras_arvo = min(paras_arvo, self.minimax(tmp_ruudut, syvyys+1, maks_syvyys, True))
            return paras_arvo
                   

