class Peli:

    """ Pelilogiikka on pitkälti tässä luokassa. Se pitää kirjaa pelin kulusta.
    """

    def __init__(self, pelaaja1, pelaaja2, ruudukko):
        self.pelaajat = [pelaaja1, pelaaja2]
        self.vuoro = 0
        self.aloitusvuoro = 0
        self.ruudukko = ruudukko
        self.viimeisin_siirto = None


    def uusi_peli(self):
        if self.aloitusvuoro == 0:
            self.aloitusvuoro = 1
        else:
            self.aloitusvuoro = 0
        self.vuoro = self.aloitusvuoro


    def pelaaja(self):
        return self.pelaajat[self.vuoro]


    def tarkista_voittaja(self):
        return self.ruudukko.viiden_suora(self.pelaaja().merkki)


    def siirra(self, merkki:str, x:int, y:int):
        self.ruudukko.aseta_merkki(merkki, x, y)
        self.viimeisin_siirto = (merkki, x, y)


    def vaihda_vuoro(self):
        if self.vuoro == 0:
            self.vuoro = 1
        else:
            self.vuoro = 0
