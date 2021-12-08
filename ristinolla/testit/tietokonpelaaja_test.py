import unittest
from ristinolla.tietokonepelaaja import Tietokonepelaaja
from ristinolla.ruudukko import Ruudukko


class TietokonepelaajaTest(unittest.TestCase):
    def setUp(self):
        self.ruudukko = Ruudukko(20)
        self.pelaaja = Tietokonepelaaja("0", "nimi", self.ruudukko)
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
        self.assertEqual(arvo, 8)
    
    
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
        self.assertEqual(arvo, -5)
    

    
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
        self.assertEqual(arvo, -5)
    

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


    def test_siirra_nelja_rivi(self):

        self.pelaaja.siirrot = {(0,0):(0,0,"X"), 
                                (1,0):(1,0,"X"), 
                                (2,0):(2,0,"X"), 
                                (3,0):(3,0,"X")}
        self.pelaaja.tyhjat_ruudut = {(0,1):(0,1),
                                    (0,2):(0,2),(1,1):(1,1),
                                    (1,2):(1,2),(2,1):(2,1),
                                    (2,2):(2,2),(3,1):(3,1),
                                    (3,2):(3,2),(4,0):(4,0),
                                    (4,1):(4,1),(4,2):(4,2)}
                                    
        self.ruudukko.ruudut[0][0] = "X"
        self.ruudukko.ruudut[1][0] = "X"
        self.ruudukko.ruudut[2][0] = "X"
        self.ruudukko.ruudut[3][0] = "X"
        self.ruudukko.viimeisin_siirto = (3,0, "X")
        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 4,0))

    """
    def test_mahdolliset_ruudut_1(self):
        self.ruudut[10][10] = "X"
        vaihtoehdot = [(11,10)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)


    def test_mahdolliset_ruudut_1(self):
        vaihtoehdot = [(10,10)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)
    

    def test_neljan_rivit_vaaka(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][10] = "X"
        self.ruudut[12][10] = "X"
        vaihtoehdot = []
        self.assertEqual(self.pelaaja.neljan_rivit(self.ruudut,10,10,20), vaihtoehdot)


    def test_neljan_rivit_vaaka(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][10] = "X"
        self.ruudut[12][10] = "X"
        self.ruudut[13][10] = "X"
        vaihtoehdot = [(14,10),(9,10)]
        self.assertEqual(self.pelaaja.neljan_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_neljan_rivit_pysty(self):
        self.ruudut[10][10] = "X"
        self.ruudut[10][11] = "X"
        self.ruudut[10][12] = "X"
        self.ruudut[10][13] = "X"
        vaihtoehdot = [(10,14),(10,9)]
        self.assertEqual(self.pelaaja.neljan_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_neljan_rivit_vino(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][11] = "X"
        self.ruudut[12][12] = "X"
        self.ruudut[13][13] = "X"
        vaihtoehdot = [(14,14),(9,9)]
        self.assertEqual(self.pelaaja.neljan_rivit(self.ruudut,10,10,20), vaihtoehdot)
    
    
    def test_neljan_rivit_vino2(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][9] = "X"
        self.ruudut[12][8] = "X"
        self.ruudut[13][7] = "X"
        vaihtoehdot = [(14,6),(9,11)]
        self.assertEqual(self.pelaaja.neljan_rivit(self.ruudut,10,10,20), vaihtoehdot)


    def test_kolmen_rivit_vaaka(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][10] = "X"
        vaihtoehdot = []
        self.assertEqual(self.pelaaja.kolmen_rivit(self.ruudut,10,10,20), vaihtoehdot)


    def test_kolmen_rivit_vaaka(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][10] = "X"
        self.ruudut[12][10] = "X"
        vaihtoehdot = [(13,10),(9,10)]
        self.assertEqual(self.pelaaja.kolmen_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_kolmen_rivit_pysty(self):
        self.ruudut[10][10] = "X"
        self.ruudut[10][11] = "X"
        self.ruudut[10][12] = "X"
        vaihtoehdot = [(10,13),(10,9)]
        self.assertEqual(self.pelaaja.kolmen_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_kolmen_rivit_vino(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][11] = "X"
        self.ruudut[12][12] = "X"
        vaihtoehdot = [(13,13),(9,9)]
        self.assertEqual(self.pelaaja.kolmen_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_kolmen_rivit_vino2(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][9] = "X"
        self.ruudut[12][8] = "X"
        vaihtoehdot = [(13,7),(9,11)]
        self.assertEqual(self.pelaaja.kolmen_rivit(self.ruudut,10,10,20), vaihtoehdot)


    def test_kahden_rivit_vaaka(self):
        self.ruudut[10][10] = "X"
        vaihtoehdot = []
        self.assertEqual(self.pelaaja.kahden_rivit(self.ruudut,10,10,20), vaihtoehdot)


    def test_kahden_rivit_vaaka(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][10] = "X"
        vaihtoehdot = [(12,10),(9,10)]
        self.assertEqual(self.pelaaja.kahden_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_kahden_rivit_pysty(self):
        self.ruudut[10][10] = "X"
        self.ruudut[10][11] = "X"
        vaihtoehdot = [(10,12),(10,9)]
        self.assertEqual(self.pelaaja.kahden_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_kahden_rivit_vino(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][11] = "X"
        vaihtoehdot = [(12,12),(9,9)]
        self.assertEqual(self.pelaaja.kahden_rivit(self.ruudut,10,10,20), vaihtoehdot)
    

    def test_kahden_rivit_vino2(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][9] = "X"
        vaihtoehdot = [(12,8),(9,11)]
        self.assertEqual(self.pelaaja.kahden_rivit(self.ruudut,10,10,20), vaihtoehdot)


"""


