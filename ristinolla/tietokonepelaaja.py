
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
        self.siirrot = {}


    def aseta_piste(self, x:int, y:int):
        self.x = x
        self.y = y


    def siirra(self):
        if not self.x == -1 and not self.y == -1:
        
            aika_1 = time.perf_counter()
            ruudut = copy.deepcopy(self.ruudukko.ruudut)
            aika_2 = time.perf_counter()
            mahd_siirrot =  self.mahdolliset_siirrot(ruudut)
            print("mahdolliset siirrot", mahd_siirrot)
            aika_3 = time.perf_counter()
            paras_siirto = None
            paras_arvo = -10000
            parhaat_siirrot = []

            aika_4 = time.perf_counter()
            if len(mahd_siirrot) == 1:
                x, y = mahd_siirrot[list(mahd_siirrot.keys())[0]]
                self.x = -1
                self.y = -1
                return self.merkki, x, y

            for siirto in mahd_siirrot:
                tmp_siirrot = copy.deepcopy(self.siirrot)
                x,y = siirto
                tmp_siirrot[(x,y)] = (x,y,"0")

                aika_minimax_1 = time.perf_counter()
                uusi_arvo = self.alfabeta(tmp_siirrot, 0, 5, False,-1000, 1000)
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


    def mahdolliset_siirrot(self, tehdyt_siirrot):
        n = 20
        neloset = {}
        kolmoset = {}
        kakkoset = {}
        vapaat = {}

        ruudut = copy.deepcopy(self.ruudukko.ruudut)
        for siirto in tehdyt_siirrot:
            x, y = siirto[0], siirto[1]
            ruudut[x][y] = 0


        for i in range(n):
            for j in range(n):
                if ruudut[i][j] != -1:

                    neloset_tmp = self.neljan_rivit(ruudut, i, j, n) 
                    if len(neloset_tmp) > 0:
                        neloset.update(neloset_tmp)
                    kolmoset_tmp = self.kolmen_rivit(ruudut, i, j, n)
                    if len(kolmoset_tmp) > 0:
                        kolmoset.update(kolmoset_tmp)
                    kakkoset_tmp = self.kahden_rivit(ruudut, i, j, n)
                    if len(kakkoset_tmp) > 0:
                        kakkoset.update(kakkoset_tmp)
        
        if len(neloset) > 0:
            return neloset
        if len(kolmoset) > 0:
            vapaat.update(kolmoset)
        if len(kakkoset)>0:
            vapaat.update(kakkoset)

        if len(vapaat) > 0:
            return vapaat
        
        for i in range(n):
            for j in range(n):
                if ruudut[i][j] != -1:
                    if i+1 <n and ruudut[i+1][j] == -1:
                        return {(i+1,j):(i+1,j)}
                    if j+1<n and ruudut[i][j+1] == -1:
                        return {(i,j+1):(i,j+1)}
                    if i+1<n and j+1 <n and ruudut[i+1][j+1] == -1:
                        return {(i+1,j+1):(i+1,j+1)}
                    if i>0 and ruudut[i-1][j] == -1:
                        return {(i-1,j):(i-1,j)}
                    if i>0 and j>0 and ruudut[i-1][j-1] == -1:
                        return {(i-1,j-1):(i-1,j-1)}     
                     

        return {(5,5):(5,5)}

        
    def neljan_rivit(self, ruudut, i, j, n):  
        vapaat = {}
    
        if (i+4<n)  and (\
            ruudut[i][j] == ruudut[i+1][j] and \
            ruudut[i+1][j] == ruudut[i+2][j] and \
            ruudut[i+2][j] == ruudut[i+3][j] ):
            if ruudut[i+4][j] == -1:
                vapaat[(i+4,j)] = (i+4,j)
            if i-1 >=0 and ruudut[i-1][j] == -1:
                vapaat[(i-1,j)]  = (i-1,j)

        if (j+4<n) and  (\
            ruudut[i][j] == ruudut[i][j+1] and \
            ruudut[i][j+1] == ruudut[i][j+2] and \
            ruudut[i][j+2] == ruudut[i][j+3] ):
            if ruudut[i][j+4] == -1:
                vapaat[(i,j+4)] = (i,j+4)
            if j-1 >=0 and ruudut[i][j-1] == -1:
                vapaat[(i,j-1)] = (i,j-1)
        
        if i+4<n and j+4<n and (\
            ruudut[i][j] == ruudut[i+1][j+1] and \
            ruudut[i+1][j+1] == ruudut[i+2][j+2] and \
            ruudut[i+2][j+2] == ruudut[i+3][j+3]):
            if ruudut[i+4][j+4] == -1:
                vapaat[(i+4,j+4)] = (i+4,j+4)
            if i-1 >=0 and j-1>=0 and ruudut[i-1][j-1] == -1:
                vapaat[(i-1,j-1)] = (i-1,j-1)
            
        if i+4<n and j-4>=0 and (\
            ruudut[i][j] == ruudut[i+1][j-1] and \
            ruudut[i+1][j-1] == ruudut[i+2][j-2] and \
            ruudut[i+2][j-2] == ruudut[i+3][j-3]):
            if ruudut[i+4][j-4] == -1:
                vapaat[(i+4,j-4)] = (i+4,j-4)
            if i-1 >=0 and j+1<n and ruudut[i-1][j+1] == -1:
                vapaat[(i-1,j+1)] = (i-1,j+1)

        return vapaat


    def kolmen_rivit(self, ruudut, i, j, n):
        vapaat = {}
   
        if (i+3<n) and (\
            ruudut[i][j] == ruudut[i+1][j] and \
            ruudut[i+1][j] == ruudut[i+2][j] ): 
            if ruudut[i+3][j] == -1:
                vapaat[(i+3,j)] = (i+3,j)
            if i-1 >=0 and ruudut[i-1][j] == -1:
                vapaat[(i-1,j)] = (i-1,j)
           
        if (j+3<n) and (\
            ruudut[i][j] == ruudut[i][j+1] and \
            ruudut[i][j+1] == ruudut[i][j+2] ):
            if ruudut[i][j+3] == -1:
                vapaat[(i,j+3)] = (i,j+3)
            if j-1 >=0 and ruudut[i][j-1] == -1:
                vapaat[(i,j-1)] = (i,j-1)
           
        if i+3<n and j+3<n and (\
            ruudut[i][j] == ruudut[i+1][j+1] and \
            ruudut[i+1][j+1] == ruudut[i+2][j+2]):
            if ruudut[i+3][j+3] == -1:
                vapaat[(i+3,j+3)] = (i+3,j+3)
            if i-1 >=0 and j-1>=0 and ruudut[i-1][j-1] == -1:
                vapaat[(i-1,j-1)] = (i-1,j-1)
      
        if i+3<n and j-3>=0 and (\
            ruudut[i][j] == ruudut[i+1][j-1] and \
            ruudut[i+1][j-1] == ruudut[i+2][j-2]):
            if ruudut[i+3][j-3] == -1:
                vapaat[(i+3,j-3)] = (i+3,j-3)
            if i-1 >=0 and j+1<n and ruudut[i-1][j+1] == -1:
                vapaat[(i-1,j+1)] = (i-1,j+1)

        return vapaat


    def kahden_rivit(self, ruudut, i, j, n): 
        vapaat = {}
 
        if (i+2<n) and (\
            ruudut[i][j] == ruudut[i+1][j] ):
            if ruudut[i+2][j] == -1:
                vapaat[(i+2,j)] = (i+2,j)
            if i-1 >=0 and ruudut[i-1][j] == -1:
                vapaat[(i-1,j)] = (i-1,j) 
        
        if (j+2<n) and (\
            ruudut[i][j] == ruudut[i][j+1] ):
            if ruudut[i][j+2] == -1:
                vapaat[(i,j+2)] = (i,j+2)
            if j-1 >=0 and ruudut[i][j-1] == -1:
                vapaat[(i,j-1)] = (i,j-1)
 
        if i+2<n and j+2<n and (\
            ruudut[i][j] == ruudut[i+1][j+1] ):
            if ruudut[i+2][j+2] == -1:
                vapaat[(i+2,j+2)] = (i+2,j+2)
            if i-1 >=0 and j-1>=0 and ruudut[i-1][j-1] == -1:
                vapaat[(i-1,j-1)] = (i-1,j-1)
    
        if i+2<n and j-2>=0 and  (\
            ruudut[i][j] == ruudut[i+1][j-1]):
            if ruudut[i+2][j-2] == -1:
                vapaat[(i+2,j-2)] = (i+2,j-2)
            if i-1 >=0 and j+1<n and ruudut[i-1][j+1] == -1:
                vapaat[(i-1,j+1)] = (i-1,j+1)
    
        return vapaat



    def pisteyta(self, kaikki_siirrot):
      
        syvyydet_pelaaja = []
        syvyydet_tietokone = []

        for siirto in kaikki_siirrot.keys():
            x, y, merkki = kaikki_siirrot.get(siirto)
        
            syvyys_x = 1
            while (x+syvyys_x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x+syvyys_x,y)][2] == merkki:
                syvyys_x += 1 
            if syvyys_x > 1:
                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_x)
                else:
                    syvyydet_tietokone.append(syvyys_x)

            syvyys_y = 1
            while (x,y+syvyys_y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+syvyys_y)][2] == merkki:
                syvyys_y += 1 
            if syvyys_y > 1:
                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_y)
                else:
                    syvyydet_tietokone.append(syvyys_y)

            syvyys_xy = 1
            while (x+syvyys_xy,y+syvyys_xy) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x+syvyys_xy,y+syvyys_xy)][2] == merkki:
                syvyys_xy += 1 
            if syvyys_xy > 1:
                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_xy)
                else:
                    syvyydet_tietokone.append(syvyys_xy)

            syvyys_x_y = 1
            while (x+syvyys_x_y,y-syvyys_x_y) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x+syvyys_x_y,y-syvyys_x_y)][2] == merkki:
                syvyys_x_y += 1 
            if syvyys_x_y > 1:
                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_x_y)
                else:
                    syvyydet_tietokone.append(syvyys_x_y)

        syvyydet_pelaaja.sort(reverse=True)
        syvyydet_tietokone.sort(reverse=True)

        if len(syvyydet_pelaaja) > 0:
            if syvyydet_pelaaja[0] == 5:
                return -10
            elif syvyydet_pelaaja[0] == 3:
                return -5
        if len(syvyydet_tietokone) > 0:
            if syvyydet_tietokone[0] == 5:
                return 10
        return 0


    def alfabeta(self,tehdyt_siirrot, syvyys, maks_syvyys, maksimoija, alfa, beta):
        mahdolliset_siirrot = self.mahdolliset_siirrot(tehdyt_siirrot)
        pisteet = self.pisteyta(tehdyt_siirrot)
       

        if pisteet == 10:
            return pisteet + syvyys
        elif pisteet == -10:
            return pisteet - syvyys

        if syvyys == maks_syvyys or len(mahdolliset_siirrot) == 0:
            return pisteet

        if maksimoija:
            paras_arvo = -1000
            merkki = "0"
            for siirto in mahdolliset_siirrot:
                tmp_siirrot = copy.deepcopy(tehdyt_siirrot)
                tmp_siirrot[(siirto[0],siirto[1])] = (siirto[0],siirto[1],merkki)
                paras_arvo = max(paras_arvo, 
                                self.alfabeta(tmp_siirrot, syvyys+1, maks_syvyys, False, alfa, beta))
                if paras_arvo >= beta:
                    break
                alfa = max(alfa, paras_arvo)
            return paras_arvo
        else:
            paras_arvo = 1000
            merkki = "X"
            for siirto in mahdolliset_siirrot:
                tmp_siirrot = copy.deepcopy(tehdyt_siirrot)
                tmp_siirrot[(siirto[0],siirto[1])] = (siirto[0],siirto[1],merkki)
                paras_arvo = min(paras_arvo, 
                            self.alfabeta(tmp_siirrot, syvyys+1, maks_syvyys, True, alfa, beta))
                if paras_arvo <= alfa:
                    break
                beta = min(beta, paras_arvo)
            return paras_arvo
