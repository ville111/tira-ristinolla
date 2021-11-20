import unittest
from ristinolla.ruudukko import Ruudukko


class RuudukkoTest(unittest.TestCase):
    def setUp(self):
        self.ruudukko = Ruudukko(20)

    
    def test_aseta_merkki(self):
        x, y = (1,1)
        merkki = "x"
        self.ruudukko.aseta_merkki(merkki, x, y)
        self.assertEqual(self.ruudukko.ruudut[x][y], merkki)   

    def test_anna_merkki(self):
        x, y = (1,1)
        merkki = "x"
        self.ruudukko.ruudut[x][y] = merkki
        self.assertEqual(self.ruudukko.anna_merkki(x,y), merkki)   

    
    def test_viiden_suora(self):
        ruudut =  [[-1]* 20 for i in range(20)]
        merkki = "0"
        self.ruudukko.ruudut[0][0] = merkki
        self.ruudukko.ruudut[1][0] = merkki
        self.ruudukko.ruudut[2][0] = merkki
        self.ruudukko.ruudut[3][0] = merkki
        self.ruudukko.ruudut[4][0] = merkki
        self.assertTrue(self.ruudukko.viiden_suora(merkki))
