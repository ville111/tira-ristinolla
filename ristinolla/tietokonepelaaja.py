
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
        Koska siirrä metodia saatetaan kutsua useammin kuin kerran (esim. aina kun hiirellä klikataan)
        niin tällä estetään siirrä-metodin tekemästä siirtoa kun sellaista ei haluta tehdä.
        """
        self.x = x
        self.y = y


    def siirra(self):
        """ Tämä metodi toteuttaa tietokonepelaajan 
        siirron. Eli käytännössä palauttaa metodin kutsujalle tietokoneen siirrot.
        self.x ja self.y estävät metodin toiminnan silloin kun ei haluta, että tietokone tekee uutta
        siirtoa. Silloin arvot ovat -1. Muussa tapauksessa tietokone on ok tekemän siirron ja arvo on
        jokun muu (laitettu aseta_piste metodilla).
        """
        if not self.x == -1 and not self.y == -1:

            t1 = time.perf_counter()

            viimeisin_siirto = self.ruudukko.viimeisin_siirto
            if viimeisin_siirto is None:
                i,j = (8,8)
                if self.kirjanpito[8][8] != -1:
                    i,j = (9,9)

                self.lisaa_siirto(i,j,self.merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
                return self.merkki, i, j

            else:
                a, b, merkki = viimeisin_siirto
                self.lisaa_siirto(a,b,merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)

            mahd_siirrot = self.tyhjat_ruudut

            paras_siirto = None
            paras_arvo = -10000
            parhaat_siirrot = []

            # debugataan
            """
            for tyhja in self.tyhjat_ruudut:
                if tyhja in self.siirrot:
                    print(f"virhe: {tyhja} löytyi siirroista")
                x, y = tyhja
                if self.kirjanpito[x][y] != -1:
                    print(f"virhe: {tyhja} ei ole tyhjä kirjanpidossa")
            
            for siirto in self.siirrot.keys():
                if siirto in self.tyhjat_ruudut:
                    print(f"virhe: {siirto} löytyi tyhjistä")
                x, y, merkki = self.siirrot[siirto]
                if self.kirjanpito[x][y] != merkki:
                    print(f"virhe: {siirto} on väärin kirjanpidossa {self.kirjanpito[x][y]}")

            for i in range(20):
                for j in range(20):
                    if self.kirjanpito[i][j] != self.ruudukko.ruudut[i][j]:
                        print(f"virhe:{(i,j)} in kirjanpito {self.kirjanpito[i][j]} !=  ruudukko {self.ruudukko.ruudut[i][j]}")
            """
            # end debugataan

            if len(mahd_siirrot) == 1:
                x, y = mahd_siirrot[list(mahd_siirrot.keys())[0]]
                self.x = -1
                self.y = -1
                self.lisaa_siirto(x,y,self.merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
                return self.merkki, x, y

            minimax_syvyys = self.minimax_syvyys
            if len(self.siirrot) < 4:
                minimax_syvyys -=1

            for siirto in mahd_siirrot:
                tmp_siirrot = copy.deepcopy(self.siirrot)
                tmp_kirjanpito = copy.deepcopy(self.kirjanpito)
                tmp_tyhjat_ruudut = copy.deepcopy(self.tyhjat_ruudut)
                x,y = siirto

                self.lisaa_siirto(x,y, self.merkki, tmp_siirrot, tmp_kirjanpito, tmp_tyhjat_ruudut)   
                uusi_arvo = self.alfabeta(tmp_siirrot, tmp_kirjanpito,
                            tmp_tyhjat_ruudut, 0,minimax_syvyys, False,-1000, 1000)

                parhaat_siirrot.append((siirto, uusi_arvo))
                if uusi_arvo > paras_arvo:
                    paras_arvo = uusi_arvo
                    paras_siirto = siirto

            x, y = paras_siirto
            self.x = -1
            self.y = -1

            #print("parhaat siirrot:", len(parhaat_siirrot))
            #parhaat_siirrot.sort(key=lambda solu: solu[1])
            #print(parhaat_siirrot)

            self.lisaa_siirto(x,y,self.merkki, self.siirrot, self.kirjanpito, self.tyhjat_ruudut)
            t2 = time.perf_counter()
            print("aika:", t2-t1)
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
        Lisäksi lisää tyhjiä taulukkoon tyhjat kaksi ruutua x,y joka suuntaan missä ei ole muuta merkkiä
        tai ruudukko lopu kesken.
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
            x1, y1, x2, y2 = (x-1, y-1, x+2, y+2)

            lisatyt_tyhjat = []

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
                        lisatyt_tyhjat.append((i,j))
        else:
            raise ValueError(f"kirjanpito{(x,y)} is not -1: {kirjanpito[x][y]} merkki: {merkki} kirjanpito:\n{kirjanpito}")


        # tarkistetaan, että kaikki taulukot ovat synkassa. Debug proseduuri.
        """
        for tyhja in tyhjat:
            if tyhja in siirrot.keys():
                print(f"virhe: {tyhja} löytyi siirroista")
            x, y = tyhja
            if kirjanpito[x][y] != -1:
                print(f"virhe: {tyhja} ei ole tyhjä kirjanpidossa")

        for siirto in siirrot.keys():
            if siirto in tyhjat.keys():
                print(f"virhe: {siirto} löytyi tyhjistä")
                tyhjat.pop(siirto)
            x, y, merkki = siirrot[siirto]
            if kirjanpito[x][y] != merkki:
                print(f"virhe: {siirto} on väärin kirjanpidossa {kirjanpito[x][y]}")
        """
        return (lisatyt_tyhjat, siirto_oli_tyhjissa)


    def pisteyta(self, kaikki_siirrot):
        pisteet_pelaaja = 0
        pisteet_tietokone = 0

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

            pisteet_p = self.kolmen_rivit(x, y, self.merkki_vastustaja, kaikki_siirrot)[0]
            pisteet_t = self.kolmen_rivit(x, y, self.merkki, kaikki_siirrot)[1]
            if pisteet_p < pisteet_pelaaja:
                pisteet_pelaaja = pisteet_p
            if pisteet_t > pisteet_tietokone:
                pisteet_tietokone = pisteet_t


        if pisteet_pelaaja == -10:
            return pisteet_pelaaja
        if pisteet_tietokone == 10:
            return pisteet_tietokone

        if pisteet_pelaaja == -5:
            return pisteet_pelaaja

        if pisteet_tietokone == 5:
           return pisteet_tietokone

        if pisteet_tietokone == 3:
           return pisteet_tietokone
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

        if x+3 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y)][2] == merkki and\
            (x+2,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x+2,y)][2] == merkki:
            if (x+3,y) in kaikki_siirrot_keys and kaikki_siirrot[(x+3,y)][2] != merkki and \
                    (x > 0 and (x-1,y) in kaikki_siirrot_keys and kaikki_siirrot[(x-1,y)][2] != merkki):
                    if merkki == self.merkki:
                        pisteet_tietokone = 0
                    else:
                        pisteet_pelaaja =  0
            elif not (x+3,y) in kaikki_siirrot.keys() or \
                    (x > 0 and not (x-1,y) in kaikki_siirrot_keys):
                if merkki == self.merkki:
                        pisteet_tietokone = 0
                else:
                        pisteet_pelaaja =  -5
        if y+3 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x,y+1) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+1)][2] == merkki and\
            (x,y+2) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y+2)][2] == merkki:
            if not (x,y+3) in kaikki_siirrot.keys() or \
                    (y > 0 and not (x,y-1) in kaikki_siirrot.keys()):
                if merkki == self.merkki:
                        pisteet_tietokone = 0
                else:
                        pisteet_pelaaja =  -5
        if x+3 < 20 and y+3 < 20 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y+1) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y+1)][2] == merkki and\
            (x+2,y+2) in kaikki_siirrot.keys() and kaikki_siirrot[(x+2,y+2)][2] == merkki:
            if not (x+3,y+3) in kaikki_siirrot.keys() or \
                    (x > 0 and y > 0 and not (x-1,y-1) in kaikki_siirrot.keys()):
                if merkki == self.merkki:
                        pisteet_tietokone = 0
                else:
                        pisteet_pelaaja =  -5
        if x+3 < 20 and y-3 > 0 and \
            (x,y) in kaikki_siirrot.keys() and kaikki_siirrot[(x,y)][2] == merkki and\
            (x+1,y-1) in kaikki_siirrot.keys() and kaikki_siirrot[(x+1,y-1)][2] == merkki and\
            (x+2,y-2) in kaikki_siirrot.keys() and kaikki_siirrot[(x+2,y-2)][2] == merkki:
            if  not (x+3,y-3) in kaikki_siirrot.keys() or \
                    (x > 0 and y < 20 and not (x-1,y+1) in kaikki_siirrot.keys()):
                if merkki == self.merkki:
                        pisteet_tietokone = 0
                else:
                        pisteet_pelaaja =  -5
        return (pisteet_pelaaja, pisteet_tietokone)


    def alfabeta(self, tehdyt_siirrot, kirjanpito, tyhjat, syvyys, maks_syvyys, maksimoija, alfa, beta):
        pisteet = self.pisteyta(tehdyt_siirrot)

        if pisteet == 10:
            #self.transposition_taulukko.tallenna(kirjanpito, Merkinta.TARKKA, pisteet, syvyys)
            return pisteet + syvyys
        elif pisteet == -10:
            #self.transposition_taulukko.tallenna(kirjanpito, Merkinta.TARKKA, pisteet, syvyys)
            return pisteet - syvyys

        if syvyys == maks_syvyys or len(tyhjat) == 0:
            #self.transposition_taulukko.tallenna(kirjanpito, Merkinta.TARKKA, pisteet, syvyys)
            if maksimoija:
                return pisteet + syvyys
            else:
                return pisteet - syvyys

        """
        hash = self.transposition_taulukko.hash_arvo(kirjanpito)
        merkinta = self.transposition_taulukko.hae_hash(hash)

        if not merkinta is None:
            merkinta_arvo = merkinta.hae_arvo(syvyys, alfa, beta)
            if not merkinta_arvo is None and merkinta_arvo == 10:
                return merkinta_arvo + syvyys
            elif not merkinta_arvo is None and merkinta_arvo == -10:
                return merkinta_arvo - syvyys
            
        """   
            #elif not merkinta_arvo is None:
            #    if maksimoija and Merkinta.ALARAJA:
            #        return merkinta_arvo + syvyys
            #    else:
            #        return merkinta_arvo - syvyys
             
        """if maksimoija:
            if not merkinta.maksimi is None:
                    return merkinta.maksimi + syvyys
        else:
            if not merkinta.minimi is None:
                    return merkinta.minimi + syvyys
        """
            

        mahdolliset_siirrot = copy.deepcopy(tyhjat)


        if maksimoija:
            paras_arvo = -1000
            merkki = self.merkki

            #paras_siirto = None

            for siirto in mahdolliset_siirrot:
                x, y = siirto

                lisatyt_tyhjat, oli_tyhjissa = self.lisaa_siirto(x,y, merkki, 
                                    tehdyt_siirrot, kirjanpito, tyhjat)
                paras_arvo = max(paras_arvo,
                                    self.alfabeta(tehdyt_siirrot, kirjanpito, 
                                                    tyhjat, syvyys+1, maks_syvyys, False, alfa, beta))

                #child_hash =  self.transposition_taulukko.hash_lisaa(hash, x,y, merkki)

                self.poista_siirto(x, y, tehdyt_siirrot, kirjanpito, tyhjat, lisatyt_tyhjat, oli_tyhjissa)

                if paras_arvo >= beta:
                    #self.transposition_taulukko.tallenna_avaimella(child_hash, Merkinta.ALARAJA, paras_arvo, syvyys, siirto)
                    paras_siirto = siirto
                    break
                alfa = max(alfa, paras_arvo)

            #self.transposition_taulukko.tallenna_avaimella(hash, Merkinta.TARKKA, paras_arvo, syvyys, paras_siirto)
            return paras_arvo
        else:
            paras_arvo = 1000
            merkki = self.merkki_vastustaja

            paras_siirto  = None
            for siirto in mahdolliset_siirrot:
                x, y = siirto

                lisatyt_tyhjat, oli_tyhjissa = self.lisaa_siirto(x,y, merkki,
                                    tehdyt_siirrot, kirjanpito, tyhjat)
                paras_arvo = min(paras_arvo,
                                    self.alfabeta(tehdyt_siirrot, kirjanpito, 
                                                    tyhjat, syvyys+1, maks_syvyys, True, alfa, beta))

                #child_hash =  self.transposition_taulukko.hash_lisaa(hash, x,y, merkki)
                self.poista_siirto(x, y, tehdyt_siirrot, kirjanpito, tyhjat, lisatyt_tyhjat, oli_tyhjissa)

                if paras_arvo <= alfa:
                    #paras_siirto = siirto
                    #self.transposition_taulukko.tallenna_avaimella(child_hash, Merkinta.YLARAJA, paras_arvo, syvyys, siirto)
                    break
                beta = min(beta, paras_arvo)

            #self.transposition_taulukko.tallenna_avaimella(hash, Merkinta.TARKKA, paras_arvo, syvyys, paras_siirto)
            return paras_arvo
