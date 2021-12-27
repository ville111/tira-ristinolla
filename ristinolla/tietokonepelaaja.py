
import copy
import time
from ristinolla.merkinta import Merkinta
from ristinolla.transponointitaulukko import Transponointitaulukko


class Tietokonepelaaja():
    """ Tämä luokka toteuttaa pelin tietokonepelaajan käyttäen minimax-algoritmia.
    """

    def __init__(self, merkki:str, merkki_vastustaja:str, nimi:str, ruudukko, syvyys=4):
        self.merkki = merkki
        self.merkki_vastustaja = merkki_vastustaja
        self.nimi = nimi
        self.ruudukko = ruudukko
        self.x = -1
        self.y = -1
        self.siirrot = {}
        self.tyhjat_ruudut = {}
        self.kirjanpito = [[-1]* 20 for i in range(20)]
        self.transposition_taulukko = Transponointitaulukko()
        self.minimax_syvyys = syvyys


    def alusta_pelaaja(self):
        """ Tämä metodi "nollaa"-pelaajan kun uusi peli aloitetaan.
        """
        self.siirrot = {}
        self.tyhjat_ruudut = {}
        self.kirjanpito = [[-1]* 20 for i in range(20)]
        self.transposition_taulukko = Transponointitaulukko()


    def aseta_piste(self, x:int, y:int):
        """ tätä metodia peli käyttää laittamaan x ja y arvoiksi jonkin muun kuin -1.
        Koska siirrä metodia saatetaan kutsua useammin kuin kerran (esim. kun hiirellä klikataan)
        niin tällä estetään siirrä-metodin tekemästä siirtoa kun sellaista ei haluta tehdä.
        """
        self.x = x
        self.y = y


    def siirra(self):
        """ Tämä metodi toteuttaa tietokonepelaajan
        siirron. Eli käytännössä palauttaa metodin kutsujalle tietokoneen siirrot.
        self.x ja self.y estävät metodin toiminnan silloin kun ei haluta, että tietokone tekee uutta
        siirtoa. Silloin arvot ovat -1. Muussa tapauksessa tietokone on ok tekemän siirron
        ja arvo on jokun muu (laitettu aseta_piste metodilla).
        """
        if not self.x == -1 and not self.y == -1:

            t_1 = time.perf_counter()
           

            viimeisin_siirto = self.ruudukko.viimeisin_siirto
            if len(self.siirrot) == 0 and viimeisin_siirto is None:
                i,j = (8,8)
                if self.kirjanpito[8][8] != -1:
                    i,j = (9,9)

                self.lisaa_siirto(i,j,self.merkki, self.siirrot,
                                self.kirjanpito, self.tyhjat_ruudut)
                return self.merkki, i, j

            elif not viimeisin_siirto is None:
                a, b, merkki = viimeisin_siirto
                self.lisaa_siirto(a,b,merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)

            mahd_siirrot = copy.deepcopy(self.tyhjat_ruudut)

            paras_siirto = None
            paras_arvo = -10000
            parhaat_siirrot = []


            if len(mahd_siirrot) == 1:
                x, y = mahd_siirrot[list(mahd_siirrot.keys())[0]]
                self.x = -1
                self.y = -1
                self.lisaa_siirto(x,y,self.merkki, self.siirrot,
                                self.kirjanpito, self.tyhjat_ruudut,False)
                return self.merkki, x, y

            pisteytetyt_siirrot = []
            hash = self.transposition_taulukko.hash_arvo(self.kirjanpito)
            positiiviset = []

            for siirto in mahd_siirrot:
                tmp_siirrot = copy.deepcopy(self.siirrot)
                tmp_kirjanpito = copy.deepcopy(self.kirjanpito)
                tmp_tyhjat_ruudut = copy.deepcopy(self.tyhjat_ruudut)
                x,y = siirto
    
                child_hash =  self.transposition_taulukko.hash_lisaa(hash, x,y, self.merkki)
                merkinta = self.transposition_taulukko.hae_hash(child_hash)
                merkinta_arvo = 0
                if not merkinta is None and  not merkinta.arvo is None:
                    merkinta_arvo = merkinta.arvo
                    if not merkinta.tietokonepelaaja:
                        merkinta_arvo = merkinta_arvo * (-1)

                self.lisaa_siirto(x,y, self.merkki, tmp_siirrot, tmp_kirjanpito, tmp_tyhjat_ruudut)

                uusi_arvo = self.valipisteytys(tmp_siirrot)
                if uusi_arvo < 0 or merkinta_arvo < 0:
                    uusi_arvo = min(uusi_arvo, merkinta_arvo)
                if uusi_arvo > 0 or merkinta_arvo > 0:
                    uusi_arvo = max(uusi_arvo, merkinta_arvo)
  
                pisteytetyt_siirrot.append((siirto, uusi_arvo))
                if uusi_arvo > 0:
                    positiiviset.append((siirto, uusi_arvo))

            pisteytetyt_siirrot.sort(key=lambda siirto: siirto[1], reverse=True)            
            #print("pisteytety", pisteytetyt_siirrot)
            #if len (positiiviset) > 0:
            #    pisteytetyt_siirrot = positiiviset

            alfa = -1000
            beta = 1000

            for siirto in positiiviset:

                tmp_siirrot = copy.deepcopy(self.siirrot)
                tmp_kirjanpito = copy.deepcopy(self.kirjanpito)
                tmp_tyhjat_ruudut = copy.deepcopy(self.tyhjat_ruudut)
                x,y = siirto[0]


                self.lisaa_siirto(x,y, self.merkki, tmp_siirrot, tmp_kirjanpito, tmp_tyhjat_ruudut)
                uusi_arvo = self.alfabeta(tmp_siirrot, tmp_kirjanpito,
                            tmp_tyhjat_ruudut, 0,self.minimax_syvyys, False,alfa, beta)

                if uusi_arvo >= beta:
                    paras_arvo = uusi_arvo
                    paras_siirto =  siirto[0]
                    break

                alfa = max(alfa, paras_arvo)

                parhaat_siirrot.append((siirto[0], uusi_arvo))
                if uusi_arvo > paras_arvo:
                    paras_arvo = uusi_arvo
                    paras_siirto = siirto[0]
            else:
                if paras_arvo <= 0:
                    for siirto in pisteytetyt_siirrot:
                        if siirto in positiiviset:
                            continue
                        tmp_siirrot = copy.deepcopy(self.siirrot)
                        tmp_kirjanpito = copy.deepcopy(self.kirjanpito)
                        tmp_tyhjat_ruudut = copy.deepcopy(self.tyhjat_ruudut)
                        x,y = siirto[0]
                        self.lisaa_siirto(x,y, self.merkki, tmp_siirrot, tmp_kirjanpito, tmp_tyhjat_ruudut)
                        uusi_arvo = self.alfabeta(tmp_siirrot, tmp_kirjanpito,
                                    tmp_tyhjat_ruudut, 0,self.minimax_syvyys, False,alfa, beta)
                        if uusi_arvo >= beta:
                            paras_arvo = uusi_arvo
                            paras_siirto =  siirto[0]
                            #print("ylin taso: break")
                            break
                        alfa = max(alfa, paras_arvo)
                        parhaat_siirrot.append((siirto[0], uusi_arvo))
                        if uusi_arvo > paras_arvo:
                            paras_arvo = uusi_arvo
                            paras_siirto = siirto[0]

            x, y = paras_siirto
            self.x = -1
            self.y = -1

            #print("parhaat siirrot:", len(parhaat_siirrot))
            #parhaat_siirrot.sort(key=lambda solu: solu[1])
            #print(parhaat_siirrot)

            print("siirrot")
            print(self.siirrot)
            print("tyhjat")
            print(self.tyhjat_ruudut)
            print("kirjanpito")
            print(self.kirjanpito)

            self.lisaa_siirto(x,y,self.merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
          
            t_2 = time.perf_counter()
            aika = t_2-t_1
            print("aika:", aika)
            #print("siirto:", (x,y,self.merkki, paras_arvo))

            return self.merkki, x, y
        return None


    def poista_siirto(self, x,y, siirrot, kirjanpito, tyhjat, poistettavat_tyhjat, palauta_tyhjiin):
        siirrot.pop((x,y))
        kirjanpito[x][y] = -1
        for poistettava in poistettavat_tyhjat:
            if poistettava in tyhjat:
                tyhjat.pop(poistettava)

        if palauta_tyhjiin:
            tyhjat[(x,y)] = (x,y)


    def lisaa_siirto(self, x, y, merkki, siirrot, kirjanpito, tyhjat):
        """ lisää siirron x,y ja merkki dictionary-taulukkoon siirrot ja kirjanpito.
        Lisäksi lisää tyhjiä taulukkoon tyhjat kaksi ruutua x,y joka suuntaan
        missä ei ole muuta merkkiä tai ruudukko lopu kesken.
        Jos (x,y) on taulussa tyhjät otetaan tämä pois.
        """
        if x < 0 or y < 0 or x > 19 or y > 19:
            raise ValueError("x:{x} y:{y}  for x and y correct value is 0 =< N < 20.")

        siirto_oli_tyhjissa = False

        if kirjanpito[x][y] == -1:
            if (x,y) in tyhjat.keys():
                tyhjat.pop((x,y))
                siirto_oli_tyhjissa = True
            siirrot[(x,y)] = (x,y,merkki)
            kirjanpito[x][y] = merkki


            lisatyt_tyhjat = []

            x1, y1, x2, y2 = (x-1, y-1, x+2, y+2)
           
            x1 = max(x1,0)
            y1 = max(y1,0)
            y2 = min(y2,19)
            x2 = min(x2,19)

            for i in range (x1, x2):
                for j in range(y1, y2):
                    if not (i == x and j == y) and kirjanpito[i][j] == -1:
                        tyhjat[(i,j)] = (i,j)
                        lisatyt_tyhjat.append((i,j))
        else:
            raise ValueError(f"kirjanpito{(x,y)} is not -1: {kirjanpito[x][y]} merkki: \
                {merkki} kirjanpito:\n{kirjanpito}")

        return (lisatyt_tyhjat, siirto_oli_tyhjissa)



    def alfabeta(self, tehdyt_siirrot, kirjanpito, tyhjat, syvyys,
                    maks_syvyys, maksimoija, alfa, beta):
        pisteet = self.pisteyta(tehdyt_siirrot)
        hash = self.transposition_taulukko.hash_arvo(kirjanpito)

        if pisteet == 10:
            self.transposition_taulukko.tallenna_avaimella(hash,
                        Merkinta.TARKKA, pisteet+pisteet, syvyys, maksimoija)
            return pisteet + syvyys
        elif pisteet == -10:
            self.transposition_taulukko.tallenna_avaimella(hash,
                        Merkinta.TARKKA, pisteet-pisteet, syvyys, maksimoija)
            return pisteet - syvyys

        if syvyys == maks_syvyys or len(tyhjat) == 0:
            if maksimoija:
                self.transposition_taulukko.tallenna_avaimella(hash,
                        Merkinta.TARKKA, pisteet+syvyys, syvyys, maksimoija)
                return pisteet + syvyys
            else: 
                self.transposition_taulukko.tallenna_avaimella(hash,
                        Merkinta.TARKKA, pisteet-syvyys, syvyys, maksimoija)
                return pisteet - syvyys
         

        mahdolliset_siirrot = copy.deepcopy(tyhjat)

        if maksimoija:
            paras_arvo = -1000
            merkki = self.merkki

            pisteytetyt_siirrot = []
            for siirto in mahdolliset_siirrot:
                x,y = siirto
                arvo = 0
                
                child_hash =  self.transposition_taulukko.hash_lisaa(hash, x,y, merkki)
                merkinta = self.transposition_taulukko.hae_hash(child_hash)
                merkinta_arvo = 0
                if not merkinta is None and  not merkinta.arvo is None:
                    merkinta_arvo = merkinta.arvo
                    if not merkinta.tietokonepelaaja:
                        merkinta_arvo *=-1
           
            
                lisatyt_tyhjat, oli_tyhjissa = self.lisaa_siirto(x,y, merkki,
                                    tehdyt_siirrot, kirjanpito, tyhjat)
                arvo = self.valipisteytys(tehdyt_siirrot)

                self.poista_siirto(x, y, tehdyt_siirrot, kirjanpito,
                                    tyhjat, lisatyt_tyhjat, oli_tyhjissa)
                if arvo < 0 or merkinta_arvo < 0:
                    arvo = min(arvo, merkinta_arvo)
                else:
                    arvo = max(arvo, merkinta_arvo)

                pisteytetyt_siirrot.append((siirto, arvo))
            
            pisteytetyt_siirrot.sort(key=lambda siirto: siirto[1], reverse=True)
            #print("maxer sorted", pisteytetyt_siirrot)

            for siirto in pisteytetyt_siirrot:
                x, y = siirto[0]
                lisatyt_tyhjat, oli_tyhjissa = self.lisaa_siirto(x,y, merkki,
                                    tehdyt_siirrot, kirjanpito, tyhjat)
                paras_arvo = max(paras_arvo,
                                    self.alfabeta(tehdyt_siirrot, kirjanpito,
                                    tyhjat, syvyys+1, maks_syvyys, False, alfa, beta))

                child_hash =  self.transposition_taulukko.hash_lisaa(hash, x,y, merkki)

                self.poista_siirto(x, y, tehdyt_siirrot, kirjanpito,
                                    tyhjat, lisatyt_tyhjat, oli_tyhjissa)

                if paras_arvo >= beta:
                    self.transposition_taulukko.tallenna_avaimella(child_hash,
                                   Merkinta.ALARAJA, paras_arvo, syvyys, maksimoija)
                    break
                alfa = max(alfa, paras_arvo)

            self.transposition_taulukko.tallenna_avaimella(hash,
                           Merkinta.TARKKA, paras_arvo, syvyys, maksimoija)
            return paras_arvo
        else:
            paras_arvo = 1000
            merkki = self.merkki_vastustaja

            pisteytetyt_siirrot = []
            for siirto in mahdolliset_siirrot:
                x,y = siirto
                arvo = 0

                
                child_hash =  self.transposition_taulukko.hash_lisaa(hash, x,y, merkki)
                merkinta = self.transposition_taulukko.hae_hash(child_hash)
                merkinta_arvo = 0
                if not merkinta is None and  not merkinta.arvo is None:
                    merkinta_arvo = merkinta.arvo
                    if merkinta.tietokonepelaaja:
                        merkinta_arvo *=-1
                    #if merkinta.selite == Merkinta.ALARAJA:
                    #    merkinta_arvo = 9
                    #if merkinta.selite == Merkinta.YLARAJA:
                    #    merkinta_arvo -9
              
                lisatyt_tyhjat, oli_tyhjissa = self.lisaa_siirto(x,y, merkki,
                                    tehdyt_siirrot, kirjanpito, tyhjat)
                arvo = self.valipisteytys(tehdyt_siirrot)
                self.poista_siirto(x, y, tehdyt_siirrot, kirjanpito,
                                    tyhjat, lisatyt_tyhjat, oli_tyhjissa)
                if arvo > 0 or merkinta_arvo > 0:
                    arvo = max(merkinta_arvo, arvo)
                else:
                    arvo = min(merkinta_arvo, arvo)

                pisteytetyt_siirrot.append((siirto, arvo))
            
            pisteytetyt_siirrot.sort(key=lambda siirto: siirto[1])
            #print("miner sorted", pisteytetyt_siirrot)

            for siirto in mahdolliset_siirrot:
                x, y = siirto

                lisatyt_tyhjat, oli_tyhjissa = self.lisaa_siirto(x,y, merkki,
                                    tehdyt_siirrot, kirjanpito, tyhjat)
                paras_arvo = min(paras_arvo,
                                    self.alfabeta(tehdyt_siirrot, kirjanpito,
                                        tyhjat, syvyys+1, maks_syvyys, True, alfa, beta))

                child_hash =  self.transposition_taulukko.hash_lisaa(hash, x,y, merkki)
                self.poista_siirto(x, y, tehdyt_siirrot, kirjanpito,
                                tyhjat, lisatyt_tyhjat, oli_tyhjissa)

                if paras_arvo <= alfa:
                    self.transposition_taulukko.tallenna_avaimella(child_hash,
                               Merkinta.YLARAJA, paras_arvo, syvyys, maksimoija)
                    break
                beta = min(beta, paras_arvo)

            self.transposition_taulukko.tallenna_avaimella(hash,
                   Merkinta.TARKKA, paras_arvo, syvyys, maksimoija)
            return paras_arvo


    def valipisteytys(self, kaikki_siirrot):
        pisteet_pelaaja = 0
        pisteet_tietokone = 0
        pelaaja_3_rivit = 0
        pelaaja_vapaat_3_rivit = 0
        tietokone_3_rivit = 0
        tietokone_vapaat_3_rivit = 0
        pelaaja_4_rivit = 0
        tietokone_4_rivit = 0

        kaikki_siirrot_keys = kaikki_siirrot.keys()
        for siirto in kaikki_siirrot_keys:
            x, y, merkki = kaikki_siirrot.get(siirto)

            # 5 rivit
            pisteet_p = self.viiden_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)[0]
            pisteet_t  = self.viiden_rivit(x, y, self.merkki, kaikki_siirrot)[1]
            if  pisteet_p == -10:
                return -10
            if pisteet_t  == 10:
                return 10

            # 4 rivit
            pisteet_p = self.neljan_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)[0]
            pisteet_t = self.neljan_rivit(x, y, self.merkki, kaikki_siirrot)[1]
            if pisteet_p < pisteet_pelaaja:
                pisteet_pelaaja = pisteet_p
            if pisteet_t > pisteet_tietokone:
                pisteet_tietokone = pisteet_t

            # 3 rivit
            pisteet_p, tmp, vapaa_3_p = self.kolmen_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)
            tmp, pisteet_t, vapaa_3_t = self.kolmen_rivit(x, y, self.merkki, kaikki_siirrot)
            if pisteet_p < pisteet_pelaaja:
                pelaaja_3_rivit += 1
                pisteet_pelaaja = pisteet_p
            if pisteet_t > pisteet_tietokone:
                tietokone_3_rivit += 1
                pisteet_tietokone = pisteet_t
            if vapaa_3_p:
                pelaaja_vapaat_3_rivit += 1
            if vapaa_3_t:
                tietokone_vapaat_3_rivit += 1

            # 2 rivit
            #pisteet_p = self.kahden_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)[0]
            #pisteet_t = self.kahden_rivit(x, y, self.merkki, kaikki_siirrot)[1]
            #if pisteet_p < pisteet_pelaaja:     
            #    pisteet_pelaaja = pisteet_p
            #if pisteet_t > pisteet_tietokone:
            #    pisteet_tietokone = pisteet_t

        # koitetaan tunnistaa/luoda/estää tupla-3-rivejä
           
        if pelaaja_vapaat_3_rivit >= 2:
            pisteet_pelaaja = -10
        if (pelaaja_vapaat_3_rivit > 0 and pelaaja_4_rivit > 0):
            pisteet_pelaaja = -10
        if tietokone_vapaat_3_rivit >= 2:
            pisteet_tietokone = 10
        if  (tietokone_vapaat_3_rivit > 0 and tietokone_4_rivit > 0):
            pisteet_tietokone = 10 


        if pisteet_tietokone == 10:
            return pisteet_tietokone

        if pisteet_pelaaja == -10:
            return pisteet_pelaaja

        if pisteet_pelaaja == -5:
            return pisteet_pelaaja
        if pisteet_tietokone == 5:
           return pisteet_tietokone
        if pisteet_tietokone == 3:
           return pisteet_tietokone
        if pisteet_pelaaja == 1:
            return pisteet_pelaaja
        if pisteet_tietokone == 1:
            return pisteet_tietokone
        return 0
    
    
    def pisteyta(self, kaikki_siirrot):
        pisteet_pelaaja = 0
        pisteet_tietokone = 0
        pelaaja_3_rivit = 0
        pelaaja_vapaat_3_rivit = 0
        tietokone_3_rivit = 0
        tietokone_vapaat_3_rivit = 0
        pelaaja_4_rivit = 0
        tietokone_4_rivit = 0

        kaikki_siirrot_keys = kaikki_siirrot.keys()
        for siirto in kaikki_siirrot_keys:
            x, y, merkki = kaikki_siirrot.get(siirto)

            # 5 rivit
            pisteet_p = self.viiden_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)[0]
            pisteet_t  = self.viiden_rivit(x, y, self.merkki, kaikki_siirrot)[1]
            if  pisteet_p == -10:
                return -10
            if pisteet_t  == 10:
                return 10

            # 4 rivit
            
            pisteet_p = self.neljan_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)[0]
            pisteet_t = self.neljan_rivit(x, y, self.merkki, kaikki_siirrot)[1]
            if pisteet_p < pisteet_pelaaja:
                pisteet_pelaaja = pisteet_p
                pelaaja_4_rivit += 1
            if pisteet_t > pisteet_tietokone:
                pisteet_tietokone = pisteet_t
                tietokone_4_rivit += 1
            

            # 3 rivit
            """
            pisteet_p, tmp, vapaa_3_p = self.kolmen_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)
            tmp, pisteet_t, vapaa_3_t = self.kolmen_rivit(x, y, self.merkki, kaikki_siirrot)
            if pisteet_p < pisteet_pelaaja:
                pelaaja_3_rivit += 1
                pisteet_pelaaja = pisteet_p
            if pisteet_t > pisteet_tietokone:
                tietokone_3_rivit += 1
                pisteet_tietokone = pisteet_t
            if vapaa_3_p:
                pelaaja_vapaat_3_rivit += 1
            if vapaa_3_t:
                tietokone_vapaat_3_rivit += 1
            """

        # koitetaan tunnistaa/luoda/estää tupla-3-rivejä
        """
        if pelaaja_vapaat_3_rivit >= 2:
            pisteet_pelaaja = -10
        if (pelaaja_vapaat_3_rivit > 0 and pelaaja_4_rivit > 0):
            pisteet_pelaaja = -10
        if tietokone_vapaat_3_rivit >= 2:
            pisteet_tietokone = 10
        if  (tietokone_vapaat_3_rivit > 0 and tietokone_4_rivit > 0):
            pisteet_tietokone = 10 
        """


        if pisteet_tietokone == 10:
            return pisteet_tietokone

        if pisteet_pelaaja == -10:
            return pisteet_pelaaja

        #if pisteet_pelaaja == -5:
        #    return pisteet_pelaaja
        #if pisteet_tietokone == 5:
        #   return pisteet_tietokone
        #if pisteet_tietokone == 3:
        #   return pisteet_tietokone
        return 0


    def viiden_rivit(self, x:int, y:int, merkki:str, kaikki_siirrot):
        kaikki_siirrot_keys = kaikki_siirrot.keys()
        pisteet_tietokone = 0
        pisteet_pelaaja = 0

        if x+4 < 20 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+1,y)][2] == merkki and\
            (x+2,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+2,y)][2] == merkki and\
            (x+3,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+3,y)][2] == merkki and\
            (x+4,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+4,y)][2] == merkki:
            if merkki == self.merkki_vastustaja:
                pisteet_pelaaja = -10
            else:
                pisteet_tietokone = 10
        if y+4 < 20 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x,y+1) in kaikki_siirrot_keys and kaikki_siirrot[(x,y+1)][2] == merkki and\
            (x,y+2) in kaikki_siirrot_keys and kaikki_siirrot[(x,y+2)][2] == merkki and\
            (x,y+3) in kaikki_siirrot_keys and kaikki_siirrot[(x,y+3)][2] == merkki and\
            (x,y+4) in kaikki_siirrot_keys and kaikki_siirrot[(x,y+4)][2] == merkki:
            if merkki == self.merkki_vastustaja:
                pisteet_pelaaja = -10
            else:
                pisteet_tietokone = 10
        if x+4 < 20 and y+4 < 20 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y+1) in kaikki_siirrot_keys and kaikki_siirrot[(x+1,y+1)][2] == merkki and\
            (x+2,y+2) in kaikki_siirrot_keys and kaikki_siirrot[(x+2,y+2)][2] == merkki and\
            (x+3,y+3) in kaikki_siirrot_keys and kaikki_siirrot[(x+3,y+3)][2] == merkki and\
            (x+4,y+4) in kaikki_siirrot_keys and kaikki_siirrot[(x+4,y+4)][2] == merkki:
            if merkki == self.merkki_vastustaja:
                pisteet_pelaaja = -10
            else:
                pisteet_tietokone = 10
        if x+4 < 20 and y-4 > 0 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y-1) in kaikki_siirrot_keys and kaikki_siirrot[(x+1,y-1)][2] == merkki and\
            (x+2,y-2) in kaikki_siirrot_keys and kaikki_siirrot[(x+2,y-2)][2] == merkki and\
            (x+3,y-3) in kaikki_siirrot_keys and kaikki_siirrot[(x+3,y-3)][2] == merkki and\
            (x+4,y-4) in kaikki_siirrot_keys and kaikki_siirrot[(x+4,y-4)][2] == merkki:
            if merkki == self.merkki_vastustaja:
                pisteet_pelaaja = -10
            else:
                pisteet_tietokone = 10
        return (pisteet_pelaaja, pisteet_tietokone)


    def neljan_rivit(self, x, y, merkki, kaikki_siirrot):

        kaikki_siirrot_keys = kaikki_siirrot.keys()
        pisteet_tietokone = 0
        pisteet_pelaaja = 0

        if x+3 < 20 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+1,y)][2] == merkki and\
            (x+2,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+2,y)][2] == merkki and\
            (x+3,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+3,y)][2] == merkki:
            if (x+4 < 20 and (x+4,y) in kaikki_siirrot_keys and \
                    kaikki_siirrot[(x+4,y)][2] != merkki) and \
                (x > 0 and (x-1,y) in kaikki_siirrot_keys and kaikki_siirrot[(x-1,y)][2] != merkki):
                if merkki == self.merkki:
                    pisteet_tietokone = 0
                else:
                    pisteet_pelaaja =  0

            elif (x+4 < 20 and not (x+4,y) in kaikki_siirrot_keys) and \
                (x > 0 and not (x-1,y) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 10
                else:
                    pisteet_pelaaja =  -10

            elif (x+4 < 20 and (x+4,y) in kaikki_siirrot_keys and \
                kaikki_siirrot[(x+4,y)][2] != merkki) or \
                (x > 0 and (x-1,y) in kaikki_siirrot_keys and kaikki_siirrot[(x-1,y)][2] != merkki):
                if merkki == self.merkki:
                    pisteet_tietokone = 0
                else:
                    pisteet_pelaaja =  -5


        if y+3 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x,y+1) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+1)][2] == merkki and\
            (x,y+2) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+2)][2] == merkki and\
            (x,y+3) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+3)][2] == merkki:
            if (y+4 < 20 and not (x,y+4) in kaikki_siirrot_keys) and \
                (y > 0 and not (x,y-1) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 10
                else:
                    pisteet_pelaaja =  -10
        if x+3 < 20 and y+3 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y+1) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y+1)][2] == merkki and\
            (x+2,y+2) in kaikki_siirrot.keys() and kaikki_siirrot[(x+2,y+2)][2] == merkki and\
            (x+3,y+3) in kaikki_siirrot.keys() and kaikki_siirrot[(x+3,y+3)][2] == merkki:
            if (x+4 < 20 and y+4 < 20 and not (x+4,y+4) in kaikki_siirrot_keys) and \
                (x > 0 and y >0 and not (x-1,y-1) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 10
                else:
                    pisteet_pelaaja =  -10
        if x+3 < 20 and y-3 >0 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y-1) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y-1)][2] == merkki and\
            (x+2,y-2) in kaikki_siirrot.keys() and kaikki_siirrot[(x+2,y-2)][2] == merkki and\
            (x+3,y-3) in kaikki_siirrot.keys() and kaikki_siirrot[(x+3,y-3)][2] == merkki:
            if (x+4 < 20 and y-3>=0 and not (x+4,y-4) in kaikki_siirrot_keys) and \
                (x > 0 and y+1<20 and not (x-1,y+1) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 10
                else:
                    pisteet_pelaaja =  -10
        return (pisteet_pelaaja, pisteet_tietokone)


    def kolmen_rivit(self, x, y, merkki, kaikki_siirrot):
        kaikki_siirrot_keys = kaikki_siirrot.keys()
        pisteet_tietokone = 0
        pisteet_pelaaja = 0
        vapaa_kolmonen = False

        if x+3 < 20 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+1,y)][2] == merkki and\
            (x+2,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+2,y)][2] == merkki:

            if (x+3,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+3,y)][2] != merkki and \
                (x > 0 and (x-1,y) in kaikki_siirrot_keys and kaikki_siirrot[(x-1,y)][2] != merkki):
                if merkki == self.merkki:
                    pisteet_tietokone = 0
                else:
                    pisteet_pelaaja =  0
            elif not (x+3,y) in kaikki_siirrot_keys or \
                    (x > 0 and not (x-1,y) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 5
                else:
                    pisteet_pelaaja =  -5
            if not (x+3,y) in kaikki_siirrot_keys and \
                    (x > 0 and not (x-1,y) in kaikki_siirrot_keys):
                vapaa_kolmonen = True

        if y+3 < 20 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x,y+1) in kaikki_siirrot_keys and kaikki_siirrot[(x,y+1)][2] == merkki and\
            (x,y+2) in kaikki_siirrot_keys and kaikki_siirrot[(x,y+2)][2] == merkki:

            if not (x,y+3) in kaikki_siirrot_keys or \
                    (y > 0 and not (x,y-1) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 5
                else:
                    pisteet_pelaaja =  -5

            if not (x,y+3) in kaikki_siirrot_keys and \
                    (y > 0 and not (x,y-1) in kaikki_siirrot_keys):
                vapaa_kolmonen = True

        if x+3 < 20 and y+3 < 20 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y+1) in kaikki_siirrot_keys and kaikki_siirrot[(x+1,y+1)][2] == merkki and\
            (x+2,y+2) in kaikki_siirrot_keys and kaikki_siirrot[(x+2,y+2)][2] == merkki:

            if not (x+3,y+3) in kaikki_siirrot_keys or \
                    (x > 0 and y > 0 and not (x-1,y-1) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 5
                else:
                    pisteet_pelaaja =  -5
            if not (x+3,y+3) in kaikki_siirrot_keys and \
                    (x > 0 and y > 0 and not (x-1,y-1) in kaikki_siirrot_keys):
                vapaa_kolmonen = True

        if x+3 < 20 and y-3 > 0 and \
            (x,y) in kaikki_siirrot_keys and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y-1) in kaikki_siirrot_keys and kaikki_siirrot[(x+1,y-1)][2] == merkki and\
            (x+2,y-2) in kaikki_siirrot_keys and kaikki_siirrot[(x+2,y-2)][2] == merkki:
            if  not (x+3,y-3) in kaikki_siirrot_keys or \
                    (x > 0 and y < 20 and not (x-1,y+1) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                    pisteet_tietokone = 5
                else:
                    pisteet_pelaaja =  -5
            if  not (x+3,y-3) in kaikki_siirrot_keys and \
                    (x > 0 and y < 20 and not (x-1,y+1) in kaikki_siirrot_keys):
                vapaa_kolmonen = True

        return (pisteet_pelaaja, pisteet_tietokone, vapaa_kolmonen)


    def kahden_rivit(self, x, y, merkki, kaikki_siirrot):
        kaikki_siirrot_keys = kaikki_siirrot.keys()
        pisteet_tietokone = 0
        pisteet_pelaaja = 0

        if x+2 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y)][2] == merkki:

             if not (x+2,y) in kaikki_siirrot.keys() or \
                    (x > 0 and not (x-1,y) in kaikki_siirrot.keys()):
                if merkki == self.merkki:
                    pisteet_tietokone = 1
                else:
                    pisteet_pelaaja =  -1

        if y+2 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x,y+1) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+1)][2] == merkki:

            if not (x,y+2) in kaikki_siirrot.keys() or \
                    (y > 0 and not (x,y-1) in kaikki_siirrot.keys()):
                if merkki == self.merkki:
                    pisteet_tietokone = 1
                else:
                    pisteet_pelaaja =  -1

        if x+2 < 20 and y+2 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y+1) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y+1)][2] == merkki:

            if not (x+2,y+2) in kaikki_siirrot.keys() or \
                    (x > 0 and y > 0 and not (x-1,y-1) in kaikki_siirrot.keys()):
                if merkki == self.merkki:
                    pisteet_tietokone = 1
                else:
                    pisteet_pelaaja =  -1
        if x+2 < 20 and y-2 > 0 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y-1) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y-1)][2] == merkki:
            if  not (x+2,y-2) in kaikki_siirrot.keys() or \
                    (x > 0 and y < 20 and not (x-1,y+1) in kaikki_siirrot.keys()):
                if merkki == self.merkki:
                    pisteet_tietokone = 1
                else:
                    pisteet_pelaaja =  -1
        return (pisteet_pelaaja, pisteet_tietokone)