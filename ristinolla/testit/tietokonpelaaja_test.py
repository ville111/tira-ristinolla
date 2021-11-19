import unittest
from ristinolla.tietokonepelaaja import Tietokonepelaaja
from ristinolla.ruudukko import Ruudukko


class TietokonepelaajaTest(unittest.TestCase):
    def setUp(self):
        self.pelaaja = Tietokonepelaaja("X", "nimi", Ruudukko(20))
        self.ruudut =  [[-1]* 20 for i in range(20)]

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
