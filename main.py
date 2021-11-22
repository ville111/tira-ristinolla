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
        self.peli = Peli(Pelaaja("X", "Pelaaja1"),
                         Tietokonepelaaja("0", "Pelaaja 2", self.ruudukko),
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
                    if not self.ruudukko.anna_merkki(x,y):
                        pelaaja.aseta_piste(x,y)
                if event.type == pygame.QUIT:
                    exit()
            if self.peli_jatkuu:
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
                    self.ikkuna.blit(self.fontti.render(merkki, True, (255, 0, 0)),
                                                        (vaaka_positio+4, pysty_positio+2))

        pygame.display.flip()


rn = Ristinolla()
rn.run()
