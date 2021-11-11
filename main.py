import pygame


class Ruudukko:
   
    def __init__(self, n:int): 
       self.n = n
       self.ruudut = [[-1]*n] * n

    def aseta_merkki(self, merkki, x, y):
        if self.ruudut[x][y] == -1:
            self.ruudut[x][y] = merkki


class Pelaaja:

    def __init__(self, merkki:str):
        self.merkki = merkki
        self.x = -1
        self.y = -1

    def aseta_piste(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def siirra(self):
        if not self.x == -1 and not self.y == -1:
            x = self.x
            y = self.y
            self.x = -1
            self.y = -1

            return self.merkki, x, y
        else:
            return None
    



class Peli:

    def __init__(self, pelaaja1, pelaaja2, ruudukko):
        self.pelaajat = [pelaaja1, pelaaja2]
        self.vuoro = 0
        self.aloitusvuoro = 0
        self.ruudukko = ruudukko
    
    def uusi_peli(self):        
        if self.aloitusvuoro == 0:
            self.aloitusvuoro = 1
        else:
            self.aloitusvuoro = 0
        self.vuoro = self.aloitusvuoro

    def pelaaja(self):
        return self.pelaajat[self.vuoro]


    def siirra(self, merkki:str, x:int, y:int):
        self.ruudukko.aseta_merkki(merkki, x, y)
        if self.vuoro == 0:
            self.vuoro = 1
        else:
            self.vuoro = 0



class Ristinolla:
    """ Pelin pääluokka 
    """

    def __init__(self):
        self.ikkunan_leveys = 480
        self.ikkunan_korkeus = 480

        self.ruudukko = Ruudukko(4)
        self.peli = Peli(Pelaaja("X"), Pelaaja("0"), self.ruudukko)
       
      
        pygame.init()
        self.ikkuna = pygame.display.set_mode((self.ikkunan_leveys, self.ikkunan_korkeus))
        pygame.display.set_caption("Ristinolla")
        self.clock = pygame.time.Clock()




    def run(self):
        
        while True:

            pelaaja = self.peli.pelaaja()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.tunnista_ruutu(event.pos[0], event.pos[1])
                    pelaaja.aseta_piste(x,y)
                   
                    print(self.peli.ruudukko.ruudut)

                if event.type == pygame.QUIT:
                    exit()  
            
            siirto = pelaaja.siirra()
            if siirto != None:
                print(f"siirretään: {siirto}")
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

        pygame.display.flip()


rn = Ristinolla()
rn.run()
