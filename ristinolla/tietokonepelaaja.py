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
            #print("siirretään")
            ruudut = copy.deepcopy(self.ruudukko.ruudut)
            siirrot =  self.mahdolliset_siirrot(ruudut)
            #print("mahdolliset siirrot", siirrot)
            paras_siirto = None
            paras_arvo = -10000
            parhaat_siirrot = []

            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = self.merkki
                uusi_arvo = self.minimax(tmp_ruudut, 0, 1, False)
                #print(f"siirto: {siirto} - uusi arvo:{uusi_arvo} - paras arvo:{paras_arvo}")
                parhaat_siirrot.append((siirto, paras_arvo))
                if uusi_arvo > paras_arvo:
                    paras_arvo = uusi_arvo
                    paras_siirto = siirto
                   
            x, y = paras_siirto
            self.x = -1
            self.y = -1
            print("paras siirto", paras_siirto)
            print("kaikki siirrot", parhaat_siirrot)
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
                    max_x = min(i+2, n-1)
                    max_y = min(j+2,n-1)
                    for a in range (min_x, max_x):
                        for b in range (min_y, max_y):
                            if ruudut[a][b] == -1:
                                if (a,b) not in vapaat:
                                    vapaat.append((a,b))
        return vapaat


    def pisteyta(self, ruudut):
        n = len(ruudut)
        loppupisteet = 0
        pisteet_0 = 0
        pisteet_x = 0
       
        merkki = "0"
        for i in range (n):
            for j in range(n):
                if i + 4 < n and (ruudut[i][j] == merkki and \
                    ruudut[i+1][j] == merkki and \
                    ruudut[i+2][j]  == merkki and \
                    ruudut[i+3][j]  == merkki  and \
                    ruudut[i+4][j] == merkki):
                    pisteet_0 = 10
                elif j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i][j+1] == merkki and \
                        ruudut[i][j+2]  == merkki and \
                        ruudut[i][j+3]  == merkki  and \
                        ruudut[i][j+4] == merkki):
                    pisteet_0 = 10
                elif i + 4 < n and j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j+1] == merkki and \
                        ruudut[i+2][j+2]  == merkki and \
                        ruudut[i+3][j+3]  == merkki  and \
                        ruudut[i+4][j+4] == merkki):
                    pisteet_0 = 10
                elif i + 4 < n and j - 4 >= 0 and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j-1] == merkki and \
                        ruudut[i+2][j-2]  == merkki and \
                        ruudut[i+3][j-3]  == merkki  and \
                        ruudut[i+4][j-4] == merkki):
                    pisteet_0 = 10

        
        merkki = "X"
        for i in range (n):
            for j in range(n):
                if i + 4 < n and (ruudut[i][j] == merkki and \
                    ruudut[i+1][j] == merkki and \
                    ruudut[i+2][j]  == merkki and \
                    ruudut[i+3][j]  == merkki  and \
                    ruudut[i+4][j] == merkki):
                        pisteet_x = -10
                   
                elif j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i][j+1] == merkki and \
                        ruudut[i][j+2]  == merkki and \
                        ruudut[i][j+3]  == merkki  and \
                        ruudut[i][j+4] == merkki):
                    pisteet_x = -10
                elif i + 4 < n and j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j+1] == merkki and \
                        ruudut[i+2][j+2]  == merkki and \
                        ruudut[i+3][j+3]  == merkki  and \
                        ruudut[i+4][j+4] == merkki):
                    pisteet_x = -10
                elif i + 4 < n and j - 4 >= 0 and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j-1] == merkki and \
                        ruudut[i+2][j-2]  == merkki and \
                        ruudut[i+3][j-3]  == merkki  and \
                        ruudut[i+4][j-4] == merkki):
                    pisteet_x = -10
        print("pisteetx", pisteet_x)

        loppupisteet = pisteet_0
        if pisteet_x < 0:
            loppupisteet = pisteet_x
        #print("loppupisteet", loppupisteet)
        return loppupisteet


    def minimax(self,ruudut, syvyys, maks_syvyys, maksimoija):
        siirrot = self.mahdolliset_siirrot(ruudut)
        valipisteet = self.pisteyta(ruudut)
        if valipisteet != 0:
            return valipisteet

        if syvyys == maks_syvyys or len(siirrot) == 0:
            pisteet = self.pisteyta(ruudut) 
            #print(f"pisteet: {pisteet} syvyys: {syvyys}")
            return pisteet

    
        if maksimoija:   
            #print("maximizer")
            paras_arvo = -1000       
            merkki = "0"
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = merkki
                uusi_arvo = self.minimax(tmp_ruudut, syvyys+1, maks_syvyys, False)
                print(f"paras_arvo:{paras_arvo} uusi arvo:{uusi_arvo}")
                paras_arvo = max(paras_arvo, uusi_arvo) 
            #print ("takaisin paras arvo:", paras_arvo)       
            return paras_arvo
        else:
            #print("minimizer")
            paras_arvo = 1000
            merkki = "X"
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = merkki
                paras_arvo = min(paras_arvo, self.minimax(tmp_ruudut, syvyys+1, maks_syvyys, True))
            
            print ("takaisin paras arvo:", paras_arvo)    
            return paras_arvo
                   

