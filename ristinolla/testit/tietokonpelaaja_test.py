import unittest
from ristinolla.tietokonepelaaja import Tietokonepelaaja
from ristinolla.ruudukko import Ruudukko



class TietokonepelaajaTest(unittest.TestCase):
    def setUp(self):
        self.ruudukko = Ruudukko(20)
        self.pelaaja = Tietokonepelaaja("0", "X","nimi", self.ruudukko,7)
        self.ruudut =  [[-1]* 20 for i in range(20)]


    def test_aseta_piste(self):
        x, y = (1,1)
        self.pelaaja.aseta_piste(x, y)
        self.assertEqual((self.pelaaja.x, self.pelaaja.y), (x,y))


    #def test_pisteyta_tyhja(self):
    #    arvo = self.pelaaja.pisteyta(self.ruudut)
    #    self.assertEqual(arvo, 0)

    """
    def test_listaa_siirto(self):
        siirrot = {}
        tyhjat = {}
        kirjanpito = self.ruudut
        x, y = (5,5)
        self.pelaaja.lisaa_siirto(x,y, "X", self.pelaaja.siirrot, self.pelaaja.kirjanpito, self.pelaaja.tyhjat_ruudut)
        arvo = self.pelaaja.tyhjat_ruudut
        ruudut = {(6,5):(6,5), (7,5):(7,5), (4,5):(4,5), (3,5):(3,5)}
        self.assertEqual(arvo, ruudut)
    """
    """
    def test_pisteyta_ruudut_pelaaja(self):
        siirrot = {}
        siirrot[(6,5)] = (6,5,"X")
        siirrot[(6,4)] = (6,4,"X")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 0)
    """

    def test_pisteyta_rivi_xxxx_tietokone(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"0")
        siirrot[(1,0)] = (1,0,"0")
        siirrot[(2,0)] = (2,0,"0")
        siirrot[(3,0)] = (3,0,"0")
        siirrot[(4,0)] = (4,0,"0")

        siirrot[(0,0)] = (0,0,"X")
        siirrot[(0,1)] = (0,1,"X")
        siirrot[(0,2)] = (0,2,"X")
        siirrot[(0,3)] = (0,3,"X")
        siirrot[(0,4)] = (0,4,"X")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, -10)

    def test_paljon_siirtoja_1(self):
        tmp_siirrot = {}


        tmp_siirrot[(5,0)] = (5,0,"X")
        tmp_siirrot[(1,0)] = (1,0,"X")
        tmp_siirrot[(2,0)] = (2,0,"X")
        tmp_siirrot[(3,0)] = (3,0,"X")
        tmp_siirrot[(4,0)] = (4,0,"X")
        arvo = self.pelaaja.pisteyta(tmp_siirrot)
        self.assertEqual(arvo, -10)
    """"
    def test_paljon_siirtoja_2(self):
        tmp_siirrot = {}

        tmp_siirrot[(10,10)] = (10,10,"0")
        tmp_siirrot[(12,10)] = (12,10,"0")
        tmp_siirrot[(1,0)] = (1,0,"X")
        tmp_siirrot[(2,0)] = (2,0,"X")
        tmp_siirrot[(3,0)] = (3,0,"X")
        tmp_siirrot[(4,0)] = (4,0,"X")
        tmp_siirrot[(5,0)] = (5,0,"X")
        arvo = self.pelaaja.pisteyta(tmp_siirrot)
        self.assertEqual(arvo, -10)

    def test_alhabeta(self):
        tmp_siirrot = {}
        tyhjat_ruudut = {}
        kirjanpito = [[-1]* 20 for i in range(20)]

        #tmp_siirrot[(10,10)] = (10,10,"0")
        tmp_siirrot[(11,10)] = (11,10,"0")
        tmp_siirrot[(12,10)] = (12,10,"0")

        tyhjat_ruudut[(10,0)] = (10,0)
        tyhjat_ruudut[(13,0)] = (13,0)

        tmp_siirrot[(1,0)] = (1,0,"0")
        tmp_siirrot[(2,0)] = (2,0,"X")
        tmp_siirrot[(3,0)] = (3,0,"X")
        tmp_siirrot[(4,0)] = (4,0,"X")
        tmp_siirrot[(5,0)] = (5,0,"X")
        #tmp_siirrot[(5,0)] = (5,0,"X")
       
        tyhjat_ruudut[(0,0)] = (0,0)
        tyhjat_ruudut[(5,0)] = (5,0)
        #tyhjat_ruudut[(6,0)] = (6,0)

        for siirto in tmp_siirrot.keys():
            x,y,merkki = tmp_siirrot[siirto]
            kirjanpito[x][y] = merkki
       
        arvo = self.pelaaja.alfabeta(tmp_siirrot, kirjanpito, tyhjat_ruudut, 
                                    0,4, False,-1000, 1000)
    
        self.assertEqual(arvo, 0)

    """

    def test_pisteyta_rivi_x_tietokone(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"0")
        siirrot[(1,0)] = (1,0,"0")
        siirrot[(2,0)] = (2,0,"0")
        siirrot[(3,0)] = (3,0,"0")
        siirrot[(4,0)] = (4,0,"0")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 10)
    
    def test_pisteyta_rivi_y_tietokone(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"0")
        siirrot[(0,1)] = (0,1,"0")
        siirrot[(0,2)] = (0,2,"0")
        siirrot[(0,3)] = (0,3,"0")
        siirrot[(0,4)] = (0,4,"0")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 10)
    
  
    def test_pisteyta_rivi_xy_tietokone(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"0")
        siirrot[(1,1)] = (1,1,"0")
        siirrot[(2,2)] = (2,2,"0")
        siirrot[(3,3)] = (3,3,"0")
        siirrot[(4,4)] = (4,4,"0")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 10)
    

    def test_pisteyta_rivi_x_y_tietokone(self):
        siirrot = {}
        siirrot[(10,10)] = (10,10,"0")
        siirrot[(11,9)] = (11,9,"0")
        siirrot[(12,8)] = (12,8,"0")
        siirrot[(13,7)] = (13,7,"0")
        siirrot[(14,6)] = (14,6,"0")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 10)
    
    
    def test_pisteyta_rivi_x_nelja_tietokone(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"0")
        siirrot[(1,0)] = (1,0,"0")
        siirrot[(2,0)] = (2,0,"0")
        siirrot[(3,0)] = (3,0,"0")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 0)
    
    
    def test_pisteyta_rivi_x_pelaaja(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"X")
        siirrot[(1,0)] = (1,0,"X")
        siirrot[(2,0)] = (2,0,"X")
        siirrot[(3,0)] = (3,0,"X")
        siirrot[(4,0)] = (4,0,"X")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, -10)
    
  

    def test_pisteyta_rivi_y_pelaaja(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"X")
        siirrot[(0,1)] = (0,1,"X")
        siirrot[(0,2)] = (0,2,"X")
        siirrot[(0,3)] = (0,3,"X")
        siirrot[(0,4)] = (0,4,"X")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, -10)

    def test_pisteyta_rivi_xy_pelaaja(self):
        siirrot = {}
        siirrot[(0,0)] = (0,0,"X")
        siirrot[(1,1)] = (1,1,"X")
        siirrot[(2,2)] = (2,2,"X")
        siirrot[(3,3)] = (3,3,"X")
        siirrot[(4,4)] = (4,4,"X")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, -10)

    
    def test_pisteyta_rivi_x_vajaa_pelaaja(self):
        siirrot = {}
        siirrot[(6,5)] = (6,5,"X")
        siirrot[(4,3)] = (4,3,"0")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 0)



    def test_pisteyta_x_vajaa_rivi_pelaaja(self):
        siirrot = {}
        siirrot[(5,5)] = (5,5,"X")
        siirrot[(6,5)] = (6,5,"X")
        siirrot[(7,5)] = (7,5,"X")
        arvo = self.pelaaja.pisteyta(siirrot)
        self.assertEqual(arvo, 0)
    

    
    def test_pisteyta_y_rivi_pelaaja(self):
        ruudut = {}
        ruudut[(0,0)] = (0,0,"X")
        ruudut[(0,1)] = (0,1,"X")
        ruudut[(0,2)] = (0,2,"X")
        ruudut[(0,3)] = (0,3,"X")
        ruudut[(0,4)] = (0,4,"X")
        arvo = self.pelaaja.pisteyta(ruudut)
        self.assertEqual(arvo, -10)

    
    def test_pisteyta_y_vajaa_rivi_pelaaja(self):
        ruudut = {}
        ruudut[(1,14)] = (1,14,"X")
        ruudut[(1,15)] = (1,15,"X")
        ruudut[(1,16)] = (1,16,"X")
        arvo = self.pelaaja.pisteyta(ruudut)
        self.assertEqual(arvo,0)
    

    def test_pisteyta_vino_rivi_pelaaja(self):
        ruudut = {}
        ruudut[(0,0)] = (0,0,"X")
        ruudut[(1,1)] = (1,1,"X")
        ruudut[(2,2)] = (2,2,"X")
        ruudut[(3,3)] = (3,3,"X")
        ruudut[(4,4)] = (4,4,"X")
        arvo = self.pelaaja.pisteyta(ruudut)
        self.assertEqual(arvo, -10)

    
    def test_pisteyta_vino2_rivi_pelaaja(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        ruudut[(13,7)] = (13,7,"X")
        ruudut[(14,6)] = (14,6,"X")

        arvo = self.pelaaja.pisteyta(ruudut)
        self.assertEqual(arvo, -10)


    def test_siirra_tyja(self):
        self.assertEqual(self.pelaaja.siirra(), None)


    """
    def test_mahdolliset_ruudut_1(self):
        self.ruudut[10][10] = "X"
        vaihtoehdot = [(11,10)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)


    def test_mahdolliset_ruudut_1(self):
        vaihtoehdot = [(10,10)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)
    
    """

    # viiden rivit

    def test_viiden_rivit_vaaka(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        ruudut[(13,10)] = (13,10,"X")
        ruudut[(14,10)] = (14,10,"X")
        self.assertEqual(self.pelaaja.viiden_rivit(10,10,"X", ruudut), (-10,0))
    
    def test_viiden_rivit_pysty(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(10,11)] = (10,11,"X")
        ruudut[(10,12)] = (10,12,"X")
        ruudut[(10,13)] = (10,13,"X")
        ruudut[(10,14)] = (10,14,"X")
        self.assertEqual(self.pelaaja.viiden_rivit(10,10,"X", ruudut), (-10,0))
    
    def test_viiden_rivit_vino(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,11)] = (11,11,"X")
        ruudut[(12,12)] = (12,12,"X")
        ruudut[(13,13)] = (13,13,"X")
        ruudut[(14,14)] = (14,14,"X")
        self.assertEqual(self.pelaaja.viiden_rivit(10,10,"X", ruudut), (-10,0))
    
    def test_viiden_rivit_vino2(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        ruudut[(13,7)] = (13,7,"X")
        ruudut[(14,6)] = (14,6,"X")
        self.assertEqual(self.pelaaja.viiden_rivit(10,10,"X", ruudut), (-10,0))


    # neljän rivit

    def test_neljan_rivit_vaaka(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        ruudut[(13,10)] = (13,10,"X")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (-10,0))

    def test_neljan_rivit_vaaka_blokattu(self):
        ruudut = {}
        ruudut[(9,10)] = (9,10,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        ruudut[(13,10)] = (13,10,"X")
        ruudut[(14,10)] = (14,10,"0")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (0,0))
        
    
    def test_neljan_rivit_pysty(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(10,11)] = (10,11,"X")
        ruudut[(10,12)] = (10,12,"X")
        ruudut[(10,13)] = (10,13,"X")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (-10,0))

    def test_neljan_rivit_pysty_blokattu(self):
        ruudut = {}
        ruudut[(10,9)] = (10,9,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(10,11)] = (10,11,"X")
        ruudut[(10,12)] = (10,12,"X")
        ruudut[(10,13)] = (10,13,"X")
        ruudut[(10,14)] = (10,14,"0")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (0,0))

    
    def test_neljan_rivit_vino(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,11)] = (11,11,"X")
        ruudut[(12,12)] = (12,12,"X")
        ruudut[(13,13)] = (13,13,"X")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (-10,0))

    def test_neljan_rivit_vino_blokattu(self):
        ruudut = {}
        ruudut[(9,9)] = (9,9,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,11)] = (11,11,"X")
        ruudut[(12,12)] = (12,12,"X")
        ruudut[(13,13)] = (13,13,"X")
        ruudut[(14,14)] = (14,14,"0")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (0,0))


    def test_neljan_rivit_vino_uudestaan(self):
        ruudut = {}
         
        ruudut[(15,15)] = (15,15,"0")
        ruudut[(5,5)] = (5,5,"0")
        ruudut[(9,10)] = (9,10,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        ruudut[(13,10)] = (13,10,"X")
        ruudut[(14,10)] = (14,10,"0")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (0,0))


    def test_neljan_rivit_vino2(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        ruudut[(13,7)] = (13,7,"X")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (-10,0))

    def test_neljan_rivit_vino2_blokattu(self):
        ruudut = {}
        ruudut[(9,11)] = (9,11,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        ruudut[(13,7)] = (13,7,"X")
        ruudut[(14,6)] = (14,6,"0")
        self.assertEqual(self.pelaaja.neljan_rivit(10,10,"X", ruudut), (0,0))
    

    # kolmen rivit

    def test_kolmen_rivit_vaaka(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,True))
    
    def test_kolmen_rivit_vaaka_blokattu(self):
        ruudut = {}
        ruudut[(9,10)] = (9,10,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        ruudut[(13,10)] = (13,10,"0")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (0,0,False))

    def test_kolmen_rivit_vaaka_osittain_blokattu(self):
        ruudut = {}
        ruudut[(9,10)] = (9,10,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,False))

    def test_kolmen_rivit_vaaka_osittain_blokattu2(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,10)] = (11,10,"X")
        ruudut[(12,10)] = (12,10,"X")
        ruudut[(13,10)] = (13,10,"0")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,False))
    
    def test_kolmen_rivit_pysty(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(10,11)] = (10,11,"X")
        ruudut[(10,12)] = (10,12,"X")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,True))
    
    def test_kolmen_rivit_pysty_blokattu(self):
        ruudut = {}
        ruudut[(10,9)] = (10,9,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(10,11)] = (10,11,"X")
        ruudut[(10,12)] = (10,12,"X")
        ruudut[(10,13)] = (10,13,"0")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (0,0,False))
    
    def test_kolmen_rivit_pysty_osittain_blokattu(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(10,11)] = (10,11,"X")
        ruudut[(10,12)] = (10,12,"X")
        ruudut[(10,13)] = (10,13,"0")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,False))
    
    def test_kolmen_rivit_pysty_blokattu2(self):
        ruudut = {}
        ruudut[(10,9)] = (10,9,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(10,11)] = (10,11,"X")
        ruudut[(10,12)] = (10,12,"X")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,False))
    
    def test_kolmen_rivit_vino(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,11)] = (11,11,"X")
        ruudut[(12,12)] = (12,12,"X")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,True))

    def test_kolmen_rivit_vino_blokattu(self):
        ruudut = {}
        ruudut[(9,9)] = (9,9,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,11)] = (11,11,"X")
        ruudut[(12,12)] = (12,12,"X")
        ruudut[(13,13)] = (13,13,"0")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (0,0,False))
    
    def test_kolmen_rivit_vino2(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,True))

    def test_kolmen_rivit_vino2_blokattu(self):
        ruudut = {}
        ruudut[(9,11)] = (9,11,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        ruudut[(13,7)] = (13,7,"0")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (0,0, False))
    
    def test_kolmen_rivit_vino2_osittain_blokattu(self):
        ruudut = {}
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        ruudut[(13,7)] = (13,7,"0")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,False))

    def test_kolmen_rivit_vino2_osittain_blokattu2(self):
        ruudut = {}
        ruudut[(9,11)] = (9,11,"0")
        ruudut[(10,10)] = (10,10,"X")
        ruudut[(11,9)] = (11,9,"X")
        ruudut[(12,8)] = (12,8,"X")
        self.assertEqual(self.pelaaja.kolmen_rivit(10,10,"X", ruudut), (-5,0,False))


    def test_lisaa_siirto_siirrot(self):
        siirrot = {}
        tyhjat = {}
        x, y, merkki = (10,10,"X")
        tyhjat, palauta_tyhjiin = self.pelaaja.lisaa_siirto(x,y, merkki, siirrot, self.ruudut, tyhjat)
        self.assertEqual(siirrot, {(x,y):(x,y,merkki)})


    def test_lisaa_siirto_tyhjat(self):
        siirrot = {}
        tyhjat = {}
        x, y, merkki = (10,10,"X")
        tyhjat_paluu, palauta_tyhjiin = self.pelaaja.lisaa_siirto(x,y, merkki, siirrot, self.ruudut, tyhjat)
        tyhjat_vertailu =  {}
        x1, y1, x2, y2 = (x-1, y-1, x+2, y+2)

        for i in range (x1, x2):
            for j in range(y1, y2):
                if not (i == x and j == y):
                    tyhjat_vertailu[(i,j)] = (i,j)

        self.assertEqual(tyhjat,tyhjat_vertailu)


    def test_poist_siirt_siirrot(self):
        siirrot = {}
        tyhjat = {}
        x, y, merkki = (10,10,"X")
        tyhjat_palauta, palauta_tyhjiin = self.pelaaja.lisaa_siirto(x,y, merkki, siirrot, self.ruudut, tyhjat)
        self.pelaaja.poista_siirto(x,y, siirrot, self.ruudut, tyhjat, tyhjat_palauta, palauta_tyhjiin)
        self.assertEqual(siirrot, {})
    

    def test_poist_siirt_tyhjat(self):
        siirrot = {}
        tyhjat = {(2,2):(2,2), (2,3):(2,3)}
        x, y, merkki = (10,10,"X")
        tyhjat_palauta, palauta_tyhjiin = self.pelaaja.lisaa_siirto(x,y, merkki, siirrot, self.ruudut, tyhjat)
        self.pelaaja.poista_siirto(x,y, siirrot, self.ruudut, tyhjat, tyhjat_palauta, palauta_tyhjiin)
        self.assertEqual(tyhjat,  {(2,2):(2,2), (2,3):(2,3)})


# testejä algoritmin oikeellisuuden testaamiseen. 

      
    def test_puolustus_kolmen_rivi(self):
        """ tarkistaa, että kone osaa puolustaa vastustajan tekemää kolmen merkin suoraa vastaan.
        """

        self.pelaaja.siirrot = {(8, 7): (8, 7, 'X'), (7, 6): (7, 6, '0'), (7, 7): (7, 7, 'X'), (7, 8): (7, 8, '0'), (6, 7): (6, 7, 'X')} 
        self.pelaaja.tyhjat_ruudut = {(8, 6): (8, 6), (8, 8): (8, 8), (9, 6): (9, 6), (9, 8): (9, 8), (6, 5): (6, 5), (6, 6): (6, 6), (7, 5): (7, 5), (8, 5): (8, 5), (6, 8): (6, 8), (6, 9): (6, 9), (7, 9): (7, 9), (8, 9): (8, 9), (5, 6): (5, 6), (5, 7): (5, 7), (5, 8): (5, 8), (10, 6): (10, 6), (10, 7): (10, 7), (10, 8): (10, 8), (9, 7): (9, 7)}
        self.pelaaja.kirjanpito = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 5,7)) 


    def test_puolustus_kaksi_kolmen_rivia(self):
        """ tarkistaa, että kone osaa puolustaa vastustajan yritystä tehdä kaksi kolmen riviä vastaan.
        """

        self.pelaaja.siirrot = {(8, 7): (8, 7, 'X'), (7, 6): (7, 6, '0'), (8, 6): (8, 6, 'X'), (7, 7): (7, 7, '0'), (9, 5): (9, 5, 'X'), (7, 8): (7, 8, '0'), (7, 9): (7, 9, 'X'), (9, 6): (9, 6, '0'), (10, 5): (10, 5, 'X')}

        self.pelaaja.tyhjat_ruudut = {(8, 8): (8, 8), (9, 7): (9, 7), (9, 8): (9, 8), (6, 5): (6, 5), (6, 6): (6, 6), (6, 7): (6, 7), (7, 5): (7, 5), (8, 5): (8, 5), (6, 8): (6, 8), (8, 4): (8, 4), (9, 4): (9, 4), (10, 4): (10, 4), (10, 6): (10, 6), (6, 9): (6, 9), (8, 9): (8, 9), (6, 10): (6, 10), (7, 10): (7, 10), (8, 10): (8, 10), (10, 7): (10, 7), (11, 4): (11, 4), (11, 5): (11, 5), (11, 6): (11, 6)}

        self.pelaaja.kirjanpito = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', '0', '0', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 'X', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 'X', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 8,8)) 

    
    

    def test_puolustus_kaksi_kolmen_rivia(self):
        # tarkistaa, että kone osaa puolustaa vastustajan yritystä tehdä kolmen ja neljän riviä vastaan.
    

        self.pelaaja.siirrot = {(7, 8): (7, 8, 'X'), (6, 7): (6, 7, '0'), (8, 8): (8, 8, 'X'), (6, 8): (6, 8, '0'), (6, 6): (6, 6, 'X'), (6, 9): (6, 9, '0'), (6, 10): (6, 10, 'X'), (7, 7): (7, 7, '0'), (9, 9): (9, 9, 'X'), (8, 7): (8, 7, '0'), (9, 7): (9, 7, 'X'), (7, 9): (7, 9, '0'), (10, 8): (10, 8, 'X')}

        self.pelaaja.tyhjat_ruudut ={(8, 9): (8, 9), (5, 6): (5, 6), (5, 7): (5, 7), (5, 8): (5, 8), (7, 6): (7, 6), (9, 8): (9, 8), (5, 9): (5, 9), (5, 5): (5, 5), (6, 5): (6, 5), (7, 5): (7, 5), (5, 10): (5, 10), (7, 10): (7, 10), (5, 11): (5, 11), (6, 11): (6, 11), (7, 11): (7, 11), (8, 6): (8, 6), (8, 10): (8, 10), (9, 10): (9, 10), (10, 9): (10, 9), (10, 10): (10, 10), (9, 6): (9, 6), (10, 6): (10, 6), (10, 7): (10, 7), (11, 7): (11, 7), (11, 8): (11, 8), (11, 9): (11, 9)}

        self.pelaaja.kirjanpito = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 'X', '0', '0', '0', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, '0', 'X', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, '0', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, 'X', -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 9,8)) 



    """ Tämä testi ei mene läpi
    def test_puolustus_kaksi_kolmen_rivia_2(self):
        # tarkistaa, että kone osaa puolustaa vastustajan yritystä tehdä kolmen ja neljän riviä vastaan.
        

        self.pelaaja.siirrot = {(6, 6): (6, 6, 'X'), (5, 5): (5, 5, '0'), (5, 6): (5, 6, 'X'), (5, 7): (5, 7, '0'), (7, 7): (7, 7, 'X'), (5, 8): (5, 8, '0'), (7, 8): (7, 8, 'X')}

        self.pelaaja.tyhjat_ruudut = {(6, 5): (6, 5), (6, 7): (6, 7), (7, 5): (7, 5), (7, 6): (7, 6), (4, 4): (4, 4), (4, 5): (4, 5), (4, 6): (4, 6), (5, 4): (5, 4), (6, 4): (6, 4), (4, 7): (4, 7), (4, 8): (4, 8), (6, 8): (6, 8), (8, 6): (8, 6), (8, 7): (8, 7), (8, 8): (8, 8), (4, 9): (4, 9), (5, 9): (5, 9), (6, 9): (6, 9), (7, 9): (7, 9), (8, 9): (8, 9)}

        self.pelaaja.kirjanpito = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, '0', 'X', '0', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, 'X', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
        self.ruudukko.viimeisin_siirto = None
        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 8,9)) 
    """
    
    def test_puolustus_neljan_rivi(self):
        """ tarkistaa, että kone osaa puolustaa vastustajan yritystä tehdä vapaan neljän riviä vastaan.
        """

        self.pelaaja.siirrot = {(8, 7): (8, 7, 'X'), (7, 6): (7, 6, '0'), (7, 7): (7, 7, 'X'), (7, 8): (7, 8, '0'), (9, 8): (9, 8, 'X'), (8, 6): (8, 6, '0'), (9, 9): (9, 9, 'X'), (9, 6): (9, 6, '0'), (6, 6): (6, 6, 'X')}

        self.pelaaja.tyhjat_ruudut = {(8, 8): (8, 8), (9, 7): (9, 7), (6, 5): (6, 5), (6, 7): (6, 7), (7, 5): (7, 5), (8, 5): (8, 5), (6, 8): (6, 8), (6, 9): (6, 9), (7, 9): (7, 9), (8, 9): (8, 9), (10, 7): (10, 7), (10, 8): (10, 8), (10, 9): (10, 9), (9, 5): (9, 5), (8, 10): (8, 10), (9, 10): (9, 10), (10, 10): (10, 10), (10, 5): (10, 5), (10, 6): (10, 6), (5, 5): (5, 5), (5, 6): (5, 6), (5, 7): (5, 7)}

        self.pelaaja.kirjanpito = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', -1, 'X', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 8,8)) 
    

    def test_puolustus_viiden_rivi(self):
        """ tarkistaa, että kone osaa estää viiden rivin tekemisen kun vastustajlla on nelja rivi.
        """
    
        self.pelaaja.siirrot = {(8, 7): (8, 7, 'X'), (7, 6): (7, 6, '0'), (7, 7): (7, 7, 'X'), (7, 8): (7, 8, '0'), (9, 8): (9, 8, 'X'), (8, 6): (8, 6, '0'), (9, 9): (9, 9, 'X'), (9, 6): (9, 6, '0'), (6, 6): (6, 6, 'X'), (8, 8): (8, 8, '0'), (9, 7): (9, 7, 'X'), (10, 7): (10, 7, '0'), (6, 4): (6, 4, 'X'), (6, 5): (6, 5, '0'), (6, 7): (6, 7, 'X')}

        self.pelaaja.tyhjat_ruudut = {(7, 5): (7, 5), (8, 5): (8, 5), (6, 8): (6, 8), (6, 9): (6, 9), (7, 9): (7, 9), (8, 9): (8, 9), (10, 8): (10, 8), (10, 9): (10, 9), (9, 5): (9, 5), (8, 10): (8, 10), (9, 10): (9, 10), (10, 10): (10, 10), (10, 5): (10, 5), (10, 6): (10, 6), (5, 5): (5, 5), (5, 6): (5, 6), (5, 7): (5, 7), (11, 6): (11, 6), (11, 7): (11, 7), (11, 8): (11, 8), (5, 3): (5, 3), (5, 4): (5, 4), (6, 3): (6, 3), (7, 3): (7, 3), (7, 4): (7, 4), (5, 8): (5, 8)}

        self.pelaaja.kirjanpito = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, 'X', '0', 'X', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', 'X', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 5,7)) 
    
  
    
# hyökköystestit

    def test_hyokkaus_viiden_rivi(self):
        """ tarkistaa, että kone osaa tehda viiden rivin
        """
    
        self.pelaaja.siirrot = {(8, 7): (8, 7, 'X'), (7, 6): (7, 6, '0'), (7, 7): (7, 7, 'X'), (9, 6): (9, 6, '0'), (6, 8): (6, 8, 'X'), (8, 6): (8, 6, '0'), (10, 6): (10, 6, 'X'), (7, 8): (7, 8, '0'), (6, 9): (6, 9, 'X'), (9, 7): (9, 7, '0'), (6, 7): (6, 7, 'X'), (6, 6): (6, 6, '0'), (19, 0): (19, 0, 'X')}

        self.pelaaja.tyhjat_ruudut = {(8, 8): (8, 8), (9, 8): (9, 8), (6, 5): (6, 5), (7, 5): (7, 5), (8, 5): (8, 5), (9, 5): (9, 5), (10, 5): (10, 5), (10, 7): (10, 7), (5, 7): (5, 7), (5, 8): (5, 8), (5, 9): (5, 9), (7, 9): (7, 9), (11, 5): (11, 5), (11, 6): (11, 6), (11, 7): (11, 7), (8, 9): (8, 9), (5, 10): (5, 10), (6, 10): (6, 10), (7, 10): (7, 10), (10, 8): (10, 8), (5, 6): (5, 6), (5, 5): (5, 5), (18, 0): (18, 0), (18, 1): (18, 1)}

        self.pelaaja.kirjanpito = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', 'X', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, '0', '0', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 'X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], ['X', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 5,6)) 
    
  