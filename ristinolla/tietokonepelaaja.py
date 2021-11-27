
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
        self.tyhjat_ruudut = {}
        self.kirjanpito = [[-1]* 20 for i in range(20)]



    def aseta_piste(self, x:int, y:int):
        self.x = x
        self.y = y


    def siirra(self):
        if not self.x == -1 and not self.y == -1:
            aika_1 = time.perf_counter()

            viimeisin_siirto = self.ruudukko.viimeisin_siirto
            if viimeisin_siirto == None:
                self.lisaa_siirto(8,8,self.merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
                return self.merkki, 8, 8
            else:
                a, b, merkki = viimeisin_siirto   
                self.lisaa_siirto(a,b,merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)  
           
            aika_2 = time.perf_counter()

            mahd_siirrot =  self.kaikki_mahdolliset_siirrot(self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
        
            aika_3 = time.perf_counter()

            paras_siirto = None
            paras_arvo = -10000
            parhaat_siirrot = []

            aika_4 = time.perf_counter()

            if len(mahd_siirrot) == 1:
                x, y = mahd_siirrot[list(mahd_siirrot.keys())[0]]
                self.x = -1
                self.y = -1
                self.lisaa_siirto(x,y,self.merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
                return self.merkki, x, y

            for siirto in mahd_siirrot:
                tmp_siirrot = copy.deepcopy(self.siirrot)
                x,y = siirto
                tmp_siirrot[(x,y)] = (x,y,self.merkki)

                aika_minimax_1 = time.perf_counter()

                # minimax maksimi taso nyt 0
                uusi_arvo = self.alfabeta(tmp_siirrot, self.kirjanpito, self.tyhjat_ruudut, 0, 0, False,-1000, 1000)
                aika_minimax_2 = time.perf_counter()
                parhaat_siirrot.append((siirto, paras_arvo))
                if uusi_arvo > paras_arvo:
                    paras_arvo = uusi_arvo
                    paras_siirto = siirto

            #print("parhaat siirrot", parhaat_siirrot)
            print ("paras siirto on:", paras_siirto, "paras arvo:", paras_arvo)
            x, y = paras_siirto
            self.x = -1
            self.y = -1
            aika_5 = time.perf_counter()

            print(" ")
            print("kokonaisaika:", aika_5-aika_1)
            #print("mahdolliset siirrot:", aika_3-aika_2)
            #print("paras siirto:", aika_5-aika_4)
            #print("minimax:", aika_minimax_2-aika_minimax_1)
            print(" ")
            
            self.lisaa_siirto(x,y,self.merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
            return self.merkki, x, y
        return None


    def lisaa_siirto(self, x, y, merkki, siirrot, kirjanpito, tyhjat):
        siirrot[(x,y)] = (x,y,merkki)
        kirjanpito[x][y] = merkki

        if (x,y) in tyhjat:
            tyhjat.pop((x,y))

        x1, y1, x2, y2 = (x-2, y-2, x+2, y+2)

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 > 19:
            x2 = 19
        if y2 > 19:
            y2 = 19 

        for i in range (x1, x2):
            for j in range(y1, y2):
                if not (i == x and j == y) and kirjanpito[i][j] == -1:
                    tyhjat[(i,j)] = (i,j)



    def kaikki_mahdolliset_siirrot(self, siirrot, kirjanpito, tyhjat):
        return tyhjat


    def pisteyta(self, kaikki_siirrot):
      
        syvyydet_pelaaja = []
        syvyydet_tietokone = []

        for siirto in kaikki_siirrot.keys():
            x, y, merkki = kaikki_siirrot.get(siirto)
        
            syvyys_x = 1
            while (x+syvyys_x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x+syvyys_x,y)][2] == merkki:
                syvyys_x += 1 
            if syvyys_x > 1:
                if syvyys_x == 3 and (x+syvyys_x,y) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x+syvyys_x,y)][2] != merkki:
                    syvyys_x = 2
                elif syvyys_x == 3 and (x-1,y) in kaikki_siirrot.keys() and \
                    kaikki_siirrot[(x-1,y)][2] != merkki:
                    syvyys_x = 2
                elif syvyys_x == 3 and (x+syvyys_x,y) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x+syvyys_x,y)][2] != merkki and \
                    (x-1,y) in kaikki_siirrot.keys() and \
                    kaikki_siirrot[(x-1,y)][2] != merkki:
                    print("blocked 3")
                    syvyys_x = 1

                elif syvyys_x == 4 and (x+syvyys_x,y) in kaikki_siirrot.keys() and\
                     kaikki_siirrot[(x+syvyys_x,y)][2] != merkki and \
                    (x-1,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x-1,y)][2] != merkki:
                    syvyys_x = 1
                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_x)
                else:
                    syvyydet_tietokone.append(syvyys_x)

            syvyys_y = 1
            while (x,y+syvyys_y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+syvyys_y)][2] == merkki:
                syvyys_y += 1 
            if syvyys_y > 1:
                if syvyys_y == 3 and (x,y+syvyys_y) in kaikki_siirrot.keys() and \
                    kaikki_siirrot[(x,y+syvyys_y)][2] != merkki:
                    syvyys_y = 2
                elif syvyys_y == 3 and (x,y-1) in kaikki_siirrot.keys() and \
                    kaikki_siirrot[(x,y-1)][2] != merkki:
                    syvyys_y = 2
                elif syvyys_y == 4 and (x, y+syvyys_y) in kaikki_siirrot.keys() and \
                    kaikki_siirrot[(x, y+syvyys_y)][2] != merkki and \
                    (x,y-1) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y-1)][2] != merkki:
                    syvyys_y = 1

                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_y)
                else:
                    syvyydet_tietokone.append(syvyys_y)

            syvyys_xy = 1
            while (x+syvyys_xy,y+syvyys_xy) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x+syvyys_xy,y+syvyys_xy)][2] == merkki:
                syvyys_xy += 1 
            if syvyys_xy > 1:
                if syvyys_xy == 3 and (x+syvyys_xy,y+syvyys_xy) in kaikki_siirrot.keys() and \
                    kaikki_siirrot[(x+syvyys_xy,y+syvyys_xy)][2] != merkki:
                    syvyys_xy = 2
                elif syvyys_xy == 3 and (x-1,y-1) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x-1,y-1)][2] != merkki:
                    syvyys_xy = 2
                elif syvyys_xy == 4 and (x+syvyys_xy,y+syvyys_xy) in kaikki_siirrot.keys() and\
                     kaikki_siirrot[(x+syvyys_xy,y+syvyys_xy)][2] != merkki and \
                    (x-1,y-1) in kaikki_siirrot.keys() and kaikki_siirrot[(x-1,y-1)][2] != merkki:
                    syvyys_xy = 1
                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_xy)
                else:
                    syvyydet_tietokone.append(syvyys_xy)

            syvyys_x_y = 1
            while (x+syvyys_x_y,y-syvyys_x_y) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x+syvyys_x_y,y-syvyys_x_y)][2] == merkki:
                syvyys_x_y += 1 
            if syvyys_x_y > 1:
                if syvyys_x_y == 3 and (x+syvyys_x_y,y-syvyys_x_y) in kaikki_siirrot.keys() and \
                    kaikki_siirrot[(x+syvyys_x_y,y-syvyys_x_y)][2] != merkki:
                    syvyys_x_y = 2
                elif syvyys_x_y == 3 and (x-1,y+1) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x-1,y+1)][2] != merkki:
                    syvyys_x_y = 2
                elif syvyys_x_y == 4 and (x+syvyys_x_y, y-syvyys_x_y) in kaikki_siirrot.keys() and\
                    kaikki_siirrot[(x+syvyys_x_y, y-syvyys_x_y)][2] != merkki and \
                    (x-1,y+1) in kaikki_siirrot.keys() and kaikki_siirrot[(x-1,y+1)][2] != merkki:
                    syvyys_x_y = 1
                if merkki == "X":
                    syvyydet_pelaaja.append(syvyys_x_y)
                else:
                    syvyydet_tietokone.append(syvyys_x_y)

        syvyydet_pelaaja.sort(reverse=True)
        syvyydet_tietokone.sort(reverse=True)

        print("syvyydet peli", syvyydet_pelaaja)
        print("syvyydet tietokone", syvyydet_tietokone)
        if len(syvyydet_pelaaja) > 0 and syvyydet_pelaaja[0] == 5:
            return -10
        if len(syvyydet_tietokone) > 0 and syvyydet_tietokone[0] == 5:
            return 10
        if len(syvyydet_pelaaja) > 0 and syvyydet_pelaaja[0] == 4:
            return -5
        if len(syvyydet_tietokone) > 0 and syvyydet_tietokone[0] == 4:   
            return 5
        if len(syvyydet_pelaaja) > 0 and syvyydet_pelaaja[0] == 3 :
            return -3
        if len(syvyydet_tietokone) > 0 and syvyydet_tietokone[0] == 3:
            return 3

        return 0


    def alfabeta(self,tehdyt_siirrot, kirjanpito, tyhjat, syvyys, maks_syvyys, maksimoija, alfa, beta):
        mahdolliset_siirrot =  tyhjat
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
                tmp_tyhjat = copy.deepcopy(tyhjat)
                tmp_kirjanpito = copy.deepcopy(kirjanpito)
                x, y = siirto
                #print(f"maximoia: x:{x} y:{y} merkki:{merkki}")
                self.lisaa_siirto(x,y, merkki, tmp_siirrot, tmp_kirjanpito, tmp_tyhjat)
             
                paras_arvo = max(paras_arvo, 
                                self.alfabeta(tmp_siirrot, tmp_kirjanpito, tmp_tyhjat, syvyys+1, maks_syvyys, False, alfa, beta))
                if paras_arvo >= beta:
                    break
                alfa = max(alfa, paras_arvo)
                #print("alpha", alfa, "beta", beta, "paras arvo", paras_arvo)
            return paras_arvo
        else:
            paras_arvo = 1000
            merkki = "X"
           
            for siirto in mahdolliset_siirrot:
                tmp_siirrot = copy.deepcopy(tehdyt_siirrot)
                tmp_tyhjat = copy.deepcopy(tyhjat)
                tmp_kirjanpito = copy.deepcopy(kirjanpito)
                x, y = siirto
                self.lisaa_siirto(x,y, merkki, tmp_siirrot, tmp_kirjanpito, tmp_tyhjat)
               
                paras_arvo = min(paras_arvo, 
                            self.alfabeta(tmp_siirrot, tmp_kirjanpito, tmp_tyhjat, syvyys+1, maks_syvyys, True, alfa, beta))
                if paras_arvo <= alfa:
                    break
                beta = min(beta, paras_arvo)
            return paras_arvo
