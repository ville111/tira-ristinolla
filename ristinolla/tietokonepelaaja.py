import copy
import time


class Tietokonepelaaja():
    """ Tämä luokka toteuttaa pelin tietokonepelaajan käyttäen minimax-algoritmia.
    """

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
            aika_1 = time.perf_counter()
            ruudut = copy.deepcopy(self.ruudukko.ruudut)
            aika_2 = time.perf_counter()
            siirrot =  self.mahdolliset_siirrot(ruudut)
            print("mahdolliset siirrot", siirrot)
            aika_3 = time.perf_counter()
            paras_siirto = None
            paras_arvo = -10000
            parhaat_siirrot = []

            aika_4 = time.perf_counter()
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = self.merkki

                aika_minimax_1 = time.perf_counter()
                uusi_arvo = self.minimax(tmp_ruudut, 0, 5, False)
                aika_minimax_2 = time.perf_counter()
                parhaat_siirrot.append((siirto, paras_arvo))
                if uusi_arvo > paras_arvo:
                    paras_arvo = uusi_arvo
                    paras_siirto = siirto

            x, y = paras_siirto
            self.x = -1
            self.y = -1
            aika_5 = time.perf_counter()

            print(" ")
            print("kokonaisaika:", aika_5-aika_1)
            print("mahdolliset siirrot:", aika_3-aika_2)
            print("paras siirto:", aika_5-aika_4)
            print("minimax:", aika_minimax_2-aika_minimax_1)
            print(" ")
            
            return self.merkki, x, y
        return None


    def mahdolliset_siirrot(self, ruudut):
        n = len(ruudut)
        vapaat = []

        for i in range(n):
            for j in range(n):
                if ruudut[i][j] != -1:
                    if (i+4<n) and (\
                        ruudut[i][j] == ruudut[i+1][j] and \
                        ruudut[i+1][j] == ruudut[i+2][j] and \
                        ruudut[i+2][j] == ruudut[i+3][j] ):
                        if ruudut[i+4][j] == -1:
                            vapaat.append((i+4,j))
                        elif i-1 >=0 and ruudut[i-1][j] == -1:
                            vapaat.append((i-1,j))
                    elif (i+3<n) and (\
                        ruudut[i][j] == ruudut[i+1][j] and \
                        ruudut[i+1][j] == ruudut[i+2][j] ):
                        if ruudut[i+3][j] == -1:
                            vapaat.append((i+3,j))
                        elif i-1 >=0 and ruudut[i-1][j] == -1:
                            vapaat.append((i-1,j))
                    elif (i+2<n) and (\
                        ruudut[i][j] == ruudut[i+1][j] ):
                        if ruudut[i+2][j] == -1:
                            vapaat.append((i+2,j))
                        elif i-1 >=0 and ruudut[i-1][j] == -1:
                            vapaat.append((i-1,j))
                   
                    if (j+4<n) and (\
                        ruudut[i][j] == ruudut[i][j+1] and \
                        ruudut[i][j+1] == ruudut[i][j+2] and \
                        ruudut[i][j+2] == ruudut[i][j+3] ):
                        if ruudut[i][j+4] == -1:
                            vapaat.append((i,j+4))
                        elif j-1 >=0 and ruudut[i][j-1] == -1:
                            vapaat.append((i,j-1))
                    elif (j+3<n) and (\
                        ruudut[i][j] == ruudut[i][j+1] and \
                        ruudut[i][j+1] == ruudut[i][j+2] ):
                        if ruudut[i][j+3] == -1:
                            vapaat.append((i,j+3))
                        elif j-1 >=0 and ruudut[i][j-1] == -1:
                            vapaat.append((i,j-1))
                    elif (j+2<n) and (\
                        ruudut[i][j] == ruudut[i][j+1] ):
                        if ruudut[i][j+2] == -1:
                            vapaat.append((i,j+2))
                        elif j-1 >=0 and ruudut[i][j-1] == -1:
                            vapaat.append((i,j-1))

                    if i+4<n and j+4<n and (\
                        ruudut[i][j] == ruudut[i+1][j+1] and \
                        ruudut[i+1][j+1] == ruudut[i+2][j+2] and \
                        ruudut[i+2][j+2] == ruudut[i+3][j+3]):
                        if ruudut[i+4][j+4] == -1:
                            vapaat.append((i+4,j+4))
                        elif i-1 >=0 and j-1>=0 and ruudut[i-1][j-1] == -1:
                            vapaat.append((i-1,j-1))
                    elif i+3<n and j+3<n and (\
                        ruudut[i][j] == ruudut[i+1][j+1] and \
                        ruudut[i+1][j+1] == ruudut[i+2][j+2]):
                        if ruudut[i+3][j+3] == -1:
                            vapaat.append((i+3,j+3))
                        elif i-1 >=0 and j-1>=0 and ruudut[i-1][j-1] == -1:
                            vapaat.append((i-1,j-1))

                    if i+4<n and j-4>=0 and (\
                        ruudut[i][j] == ruudut[i+1][j-1] and \
                        ruudut[i+1][j-1] == ruudut[i+2][j-2] and \
                        ruudut[i+2][j-2] == ruudut[i+3][j-3]):
                        if ruudut[i+4][j-4] == -1:
                            vapaat.append((i+4,j-4))
                        elif i-1 >=0 and j+1<n and ruudut[i-1][j+1] == -1:
                            vapaat.append((i-1,j+1))
                    elif i+3<n and j-3>=0 and (\
                        ruudut[i][j] == ruudut[i+1][j-1] and \
                        ruudut[i+1][j-1] == ruudut[i+2][j-2]):
                        if ruudut[i+3][j-3] == -1:
                            vapaat.append((i+3,j-3))
                        elif i-1 >=0 and j+1<n and ruudut[i-1][j+1] == -1:
                            vapaat.append((i-1,j+1))
                   
                    #print("vapaat", vapaat)
                """
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
                
        
        siirrot = []
        for siirto in vapaat:
            x, y = siirto
          
            if siirto not in siirrot and x-1>=0 and ruudut[x-1][y] != -1:
                siirrot.append(siirto)
            elif siirto not in siirrot and y-1 >= 0 and ruudut[x][y-1] != -1:
                siirrot.append(siirto)
            elif siirto not in siirrot and x+1 < n and ruudut[x+1][y] != -1:
                siirrot.append(siirto)
            elif siirto not in siirrot and y+1 < n and ruudut[x][y+1] != -1:
                siirrot.append(siirto)
            elif siirto not in siirrot and y+1 < n and x+1 < n and ruudut[x+1][y+1] != -1:
                siirrot.append(siirto)
            elif siirto not in siirrot and y-1 >= 0 and x-1 >=0 and ruudut[x-1][y-1] != -1:
                siirrot.append(siirto)
        #print("siirrot_", siirrot)
        return siirrot
        """
        if len(vapaat) == 0:
            for i in range(n):
                for j in range(n):
                    if ruudut[i][j] == "0" and i+1 < n and ruudut[i+1][j] == -1:
                        vapaat.append((i+1,j))
                    elif ruudut[i][j] != -1 and i+1 < n and ruudut[i+1][j] == -1:
                        vapaat.append((i+1,j))

        return list(set(vapaat))


    def pisteyta(self, ruudut):
        n = len(ruudut)
        pisteet_x = 0

       # Tietokonepelaaja
        merkki = "0"
        for i in range (n):
            for j in range(n):
                if i + 4 < n and (ruudut[i][j] == merkki and \
                    ruudut[i+1][j] == merkki and \
                    ruudut[i+2][j]  == merkki and \
                    ruudut[i+3][j]  == merkki and \
                    ruudut[i+4][j] == merkki):
                    return 10
                elif j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i][j+1] == merkki and \
                        ruudut[i][j+2]  == merkki):
                    if ruudut[i][j+3]  == merkki and ruudut[i][j+4] == merkki:
                        return 10
                    elif (j-1 >= 0 and ruudut[i][j-1] == -1) and ruudut[i][j+3] == -1:
                        pisteet_x = 0
                elif i + 4 < n and j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j+1] == merkki and \
                        ruudut[i+2][j+2]  == merkki):
                    if ruudut[i+3][j+3]  == merkki and ruudut[i+4][j+4] == merkki:
                        pisteet_x = 10
                    elif (i-1 >= 0 and j-1 >= 0 and \
                        ruudut[i-1][j-1] == -1) and ruudut[i+3][j+3] == -1:
                        pisteet_x = 0

                elif i + 4 < n and j - 4 >= 0 and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j-1] == merkki and \
                        ruudut[i+2][j-2]  == merkki):
                    if ruudut[i+3][j-3]  == merkki and ruudut[i+4][j-4] == merkki:
                        pisteet_x = 10
                    elif (i-1 >= 0 and j+1 < n and ruudut[i-1][j+1] == -1) and \
                        ruudut[i+3][j-3] == -1:
                        pisteet_x = 0

        # vastustaja
        merkki = "X"
        for i in range (n):
            for j in range(n):

                if i + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j] == merkki and \
                        ruudut[i+2][j]  == merkki):
                    if ruudut[i+3][j]  == merkki and ruudut[i+4][j] == merkki:
                        return -10
                    elif (i-1 >= 0 and ruudut[i-1][j] == -1) and ruudut[i+3][j] == -1:
                        pisteet_x = -5
                elif j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i][j+1] == merkki and \
                        ruudut[i][j+2]  == merkki):
                    if ruudut[i][j+3]  == merkki  and   ruudut[i][j+4] == merkki:
                        return -10
                    elif (j-1 >= 0 and ruudut[i][j-1] == -1) and ruudut[i][j+3] == -1:
                        pisteet_x = -5
                elif i + 4 < n and j + 4 < n and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j+1] == merkki and \
                        ruudut[i+2][j+2]  == merkki):
                    if ruudut[i+3][j+3]  == merkki and ruudut[i+4][j+4] == merkki:
                        return -10
                    elif (i-1 >= 0 and j-1 >= 0 and ruudut[i-1][j-1] == -1) and \
                        ruudut[i+3][j+3] == -1:
                        pisteet_x = -5

                elif i + 4 < n and j - 4 >= 0 and (ruudut[i][j] == merkki and \
                        ruudut[i+1][j-1] == merkki and \
                        ruudut[i+2][j-2]  == merkki):
                    if ruudut[i+3][j-3]  == merkki and ruudut[i+4][j-4] == merkki:
                        return -10
                    elif (i-1 >= 0 and j+1 < n and ruudut[i-1][j+1] == -1) and\
                        ruudut[i+3][j-3] == -1:
                        pisteet_x = -5

        if pisteet_x == -5:
            return pisteet_x
        return 0


    def minimax(self,ruudut, syvyys, maks_syvyys, maksimoija):
        siirrot = self.mahdolliset_siirrot(ruudut)
        pisteet = self.pisteyta(ruudut)

        if pisteet == 10:
            return pisteet + syvyys
        elif pisteet == -10:
            return pisteet - syvyys

        if syvyys == maks_syvyys or len(siirrot) == 0:
            return pisteet

        if maksimoija:
            paras_arvo = -1000
            merkki = "0"
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = merkki
                paras_arvo = max(paras_arvo, self.minimax(tmp_ruudut, syvyys+1, maks_syvyys, False))
            return paras_arvo
        else:
            paras_arvo = 1000
            merkki = "X"
            for siirto in siirrot:
                tmp_ruudut = copy.deepcopy(ruudut)
                tmp_ruudut[siirto[0]][siirto[1]] = merkki
                paras_arvo = min(paras_arvo, self.minimax(tmp_ruudut, syvyys+1, maks_syvyys, True))
            return paras_arvo
