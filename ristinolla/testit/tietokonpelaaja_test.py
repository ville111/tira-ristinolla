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


    def test_pisteyta_tyhja(self):
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, 0)


    def test_pisteyta_rivi_tietokone(self):
        self.ruudut[0][0] = "0"
        self.ruudut[1][0] = "0"
        self.ruudut[2][0] = "0"
        self.ruudut[3][0] = "0"
        self.ruudut[4][0] = "0"
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, 10)


    def test_pisteyta_x_rivi_pelaaja(self):
        self.ruudut[0][0] = "X"
        self.ruudut[1][0] = "X"
        self.ruudut[2][0] = "X"
        self.ruudut[3][0] = "X"
        self.ruudut[4][0] = "X"
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, -10)


    def test_pisteyta_x_vajaa_rivi_pelaaja(self):
        self.ruudut[10][1] = "X"
        self.ruudut[11][1] = "X"
        self.ruudut[12][1] = "X"
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, -5)


    def test_pisteyta_y_rivi_pelaaja(self):
        self.ruudut[0][0] = "X"
        self.ruudut[0][1] = "X"
        self.ruudut[0][2] = "X"
        self.ruudut[0][3] = "X"
        self.ruudut[0][4] = "X"
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, -10)


    def test_pisteyta_y_vajaa_rivi_pelaaja(self):
        self.ruudut[1][14] = "X"
        self.ruudut[1][15] = "X"
        self.ruudut[1][16] = "X"
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, -5)


    def test_pisteyta_vino_rivi_pelaaja(self):
        self.ruudut[0][0] = "X"
        self.ruudut[1][1] = "X"
        self.ruudut[2][2] = "X"
        self.ruudut[3][3] = "X"
        self.ruudut[4][4] = "X"
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, -10)


    def test_pisteyta_vino2_rivi_pelaaja(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][9] = "X"
        self.ruudut[12][8] = "X"
        self.ruudut[13][7] = "X"
        self.ruudut[14][6] = "X"
        arvo = self.pelaaja.pisteyta(self.ruudut)
        self.assertEqual(arvo, -10)

    def test_siirra_tyja(self):
        self.assertEqual(self.pelaaja.siirra(), None)

    def test_siirra_nelja_rivi(self):
        self.ruudukko.ruudut[0][0] = "X"
        self.ruudukko.ruudut[1][0] = "X"
        self.ruudukko.ruudut[2][0] = "X"
        self.ruudukko.ruudut[3][0] = "X"
        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.siirra(), ("0", 4,0))


    def test_mahdolliset_ruudut_1(self):
        self.ruudut[10][10] = "X"
        vaihtoehdot = [(11,10)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)
    
    def test_mahdolliset_ruudut_vaaka(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][10] = "X"
        self.ruudut[12][10] = "X"
        self.ruudut[13][10] = "X"
        vaihtoehdot = [(14,10),(9,10)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)
    
    def test_mahdolliset_ruudut_pysty(self):
        self.ruudut[10][10] = "X"
        self.ruudut[10][11] = "X"
        self.ruudut[10][12] = "X"
        self.ruudut[10][13] = "X"
        vaihtoehdot = [(10,14),(10,9)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)
    
    def test_mahdolliset_ruudut_vino(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][11] = "X"
        self.ruudut[12][12] = "X"
        self.ruudut[13][13] = "X"
        vaihtoehdot = [(14,14),(9,9)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)
    
    def test_mahdolliset_ruudut_vino(self):
        self.ruudut[10][10] = "X"
        self.ruudut[11][9] = "X"
        self.ruudut[12][8] = "X"
        self.ruudut[13][7] = "X"
        vaihtoehdot = [(14,6),(9,11)]
        self.assertEqual(self.pelaaja.mahdolliset_siirrot(self.ruudut), vaihtoehdot)






