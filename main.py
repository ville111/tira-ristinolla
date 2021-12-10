import pygame
from ristinolla.ruudukko import Ruudukko
from ristinolla.pelaaja import Pelaaja
from ristinolla.tietokonepelaaja import Tietokonepelaaja
from ristinolla.peli import Peli



class Ristinolla:
    """ Pelin pääluokka
    """

    def __init__(self):
        self.ikkunan_leveys = 480
        self.ikkunan_korkeus = 480
        self.peli_jatkuu = True
        self.ruudukko = Ruudukko(20)
        self.tietokone_pelaaja = Tietokonepelaaja("0", "Pelaaja 2", self.ruudukko)
        self.peli = Peli(Pelaaja("X", "Pelaaja1"),
                        self.tietokone_pelaaja,
                        self.ruudukko)
        pygame.init()
        self.ikkuna = pygame.display.set_mode((self.ikkunan_leveys, self.ikkunan_korkeus+30))
        pygame.display.set_caption("Ristinolla")
        self.clock = pygame.time.Clock()
        self.fontti = pygame.font.SysFont("Arial", 24)


    def run(self):
        self.ikkuna.fill((100, 100, 100))

        while True:
            pelaaja = self.peli.pelaaja()

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.tunnista_ruutu(event.pos[0], event.pos[1])
                    if isinstance(pelaaja, Pelaaja) and\
                        x >= 0 and x< 20 and y>=0 and y<20 and \
                        not self.ruudukko.anna_merkki(x,y):
                        pelaaja.aseta_piste(x,y)
                    elif self.nappi_painettu(event.pos[0], event.pos[1]):
                        self.uusi_peli()
                        print("uusi peli")

                if event.type == pygame.QUIT:
                    exit()

            if self.peli_jatkuu:
                if isinstance(pelaaja, Tietokonepelaaja):
                    pelaaja.aseta_piste(1,1)
                siirto = pelaaja.siirra()
                if siirto:
                    self.ikkuna.fill((100, 100, 100))
                    merkki, x, y = siirto
                    self.peli.siirra(merkki, x, y)
                    if self.peli.tarkista_voittaja():
                        self.tilaviesti(f"{self.peli.pelaaja().nimi} on voittanut!")
                        self.peli_jatkuu = False
                    else:
                        self.peli.vaihda_vuoro()
                        self.tilaviesti(f"Pelivuorossa: {self.peli.pelaaja().nimi}")
            self.piirra_ruudukko()
            self.clock.tick(60)


    def uusi_peli(self):
        self.peli.uusi_peli()
        self.ruudukko.uusi_peli()
        self.tietokone_pelaaja.alusta_pelaaja()
        if not self.peli_jatkuu:
            self.peli_jatkuu = True
        self.piirra_ruudukko()


    def tunnista_ruutu(self, x, y):
        """ Kääntää näytön pikselikoordinaatin ruudukon avaimeksi.
            Ottaa paremetrina (x,y) hiiren koordinatin (mihin on klikattu)
            Palauttaa ruudukko-taulukon avaimet i ja j
        """

        n = self.ruudukko.n
        leveys = (self.ikkunan_korkeus) / n
        korkeus = (self.ikkunan_korkeus) / n
        ruutu_x =  int(x / leveys - (x / leveys)*0.001)
        ruutu_y =  int(y / korkeus - (y / korkeus)*0.001)
        return (ruutu_x, ruutu_y)


    def tilaviesti(self, viesti:str):
        self.ikkuna.blit(self.fontti.render(viesti, True, (0, 0, 0)),(4, self.ikkunan_korkeus+4))
    
    def nappi_painettu(self, a, b):
        x, y, w, h = 280, self.ikkunan_korkeus+1 , 195 , 25
        if a >= x and a < x+200 and b >=y and b < y+25:
            return True
        return False

    def nappi(self):
        viesti = "Uusi peli"
        napin_fontti = pygame.font.SysFont("Arial", 18)
        pygame.draw.rect(self.ikkuna, (255,0,0), (280, self.ikkunan_korkeus+1 , 195 , 25))
        self.ikkuna.blit(napin_fontti.render(viesti, True, (0, 0, 0)),(340, self.ikkunan_korkeus+5))


    def piirra_ruudukko(self):
        """ Piirtää itse ruudukon, sekä merkit (X tai 0) oikeisiin ruutuihin.
        """

        leveys = self.ikkunan_korkeus
        korkeus = self.ikkunan_korkeus
        pygame.draw.rect(self.ikkuna, (255, 255, 255), (0, 0 , leveys, korkeus), 1)
        for i in range (self.ruudukko.n):
            vaaka_positio = (korkeus) / self.ruudukko.n * i
            pygame.draw.line(self.ikkuna, (255,255,255),
                            (0, vaaka_positio),
                            (leveys, vaaka_positio),1)
            for j in range (self.ruudukko.n):
                pysty_positio = (leveys) / self.ruudukko.n * j
                pygame.draw.line(self.ikkuna,
                            (255,255,255),
                            (pysty_positio, 0),
                            (pysty_positio, korkeus-2),1)
                merkki = self.ruudukko.anna_merkki(i,j)
                if merkki:
                    vari = (255,0,0)
                    if merkki == "X":
                        vari = (255,255,255)
                    viim_merkki, viim_x, viim_y = self.peli.viimeisin_siirto
                    if viim_x == i and viim_y == j:
                        if merkki == "X":
                            vari = (150,150,150)
                        else:
                            vari = (150,0,0)
                    self.ikkuna.blit(self.fontti.render(merkki, True, vari),
                                                        (vaaka_positio+4, pysty_positio+2))
        self.nappi()
        pygame.display.flip()


rn = Ristinolla()
rn.run()
