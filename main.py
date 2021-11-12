import pygame
from ristinolla.ruudukko import Ruudukko 
from ristinolla.pelaaja import Pelaaja
from ristinolla.peli import Peli



class Ristinolla:
    """ Pelin pääluokka 
    """

    def __init__(self):
        self.ikkunan_leveys = 480
        self.ikkunan_korkeus = 480
        self.ruudukko = Ruudukko(20)
        self.peli = Peli(Pelaaja("X"), Pelaaja("0"), self.ruudukko)
        pygame.init()
        self.ikkuna = pygame.display.set_mode((self.ikkunan_leveys, self.ikkunan_korkeus))
        pygame.display.set_caption("Ristinolla")
        self.clock = pygame.time.Clock()
        self.fontti = pygame.font.SysFont("Arial", 24)


    def run(self):        
        while True:
            pelaaja = self.peli.pelaaja()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.tunnista_ruutu(event.pos[0], event.pos[1])
                    pelaaja.aseta_piste(x,y)
                if event.type == pygame.QUIT:
                    exit()  
            siirto = pelaaja.siirra()
            if siirto:
                merkki, x, y = siirto
                self.peli.siirra(merkki, x, y)
            self.piirra_ruudukko()
            self.clock.tick(60)    


    def tunnista_ruutu(self, x, y):
        x1 = 0
        y1 = 0
        n = self.ruudukko.n
        leveys = (self.ikkunan_korkeus - x1*2) / n
        korkeus = (self.ikkunan_korkeus - y1*2) / n
        ruutu_x =  int(x / leveys - (x / leveys)*0.001)
        ruutu_y =  int(y / korkeus - ( y / korkeus)*0.001)
        return (ruutu_x, ruutu_y)


    def piirra_ruudukko(self):
        self.ikkuna.fill((100, 100, 100))
        x1 = 0
        y1 = 0
        leveys = self.ikkunan_korkeus - x1*2
        korkeus = self.ikkunan_korkeus - y1*2

        pygame.draw.rect(self.ikkuna, (255, 255, 255), (x1, y1 , leveys, korkeus), 1)

        for i in range (self.ruudukko.n):
            vaaka_positio = (korkeus) / self.ruudukko.n * i + y1 
            pygame.draw.line(self.ikkuna, (255,255,255), (x1, vaaka_positio), (leveys+x1, vaaka_positio),1)
            for j in range (self.ruudukko.n):   
                    pysty_positio = (leveys) / self.ruudukko.n * j + y1 
                    pygame.draw.line(self.ikkuna, (255,255,255), (pysty_positio, y1), (pysty_positio, korkeus+y1),1)
                    
                    merkki = self.ruudukko.anna_merkki(i,j)
                    if merkki:
                        self.ikkuna.blit(self.fontti.render(merkki, True, (255, 0, 0)),(vaaka_positio+4, pysty_positio+2))

        pygame.display.flip()


rn = Ristinolla()
rn.run()
