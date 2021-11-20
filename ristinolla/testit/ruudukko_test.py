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

    
    def test_viiden_suora_x(self):
        ruudut =  [[-1]* 20 for i in range(20)]
        merkki = "0"
        self.ruudukko.ruudut[0][0] = merkki
        self.ruudukko.ruudut[1][0] = merkki
        self.ruudukko.ruudut[2][0] = merkki
        self.ruudukko.ruudut[3][0] = merkki
        self.ruudukko.ruudut[4][0] = merkki
        self.assertTrue(self.ruudukko.viiden_suora(merkki))


    def test_viiden_suora_y(self):
        ruudut =  [[-1]* 20 for i in range(20)]
        merkki = "0"
        self.ruudukko.ruudut[0][0] = merkki
        self.ruudukko.ruudut[0][1] = merkki
        self.ruudukko.ruudut[0][2] = merkki
        self.ruudukko.ruudut[0][3] = merkki
        self.ruudukko.ruudut[0][4] = merkki
        self.assertTrue(self.ruudukko.viiden_suora(merkki))
    
    
    def test_viiden_suora_viisto(self):
        ruudut =  [[-1]* 20 for i in range(20)]
        merkki = "0"
        self.ruudukko.ruudut[0][0] = merkki
        self.ruudukko.ruudut[1][1] = merkki
        self.ruudukko.ruudut[2][2] = merkki
        self.ruudukko.ruudut[3][3] = merkki
        self.ruudukko.ruudut[4][4] = merkki
        self.assertTrue(self.ruudukko.viiden_suora(merkki))
    

    def test_viiden_suora_viisto2(self):
        ruudut =  [[-1]* 20 for i in range(20)]
        merkki = "0"
        self.ruudukko.ruudut[10][10] = merkki
        self.ruudukko.ruudut[11][9] = merkki
        self.ruudukko.ruudut[12][8] = merkki
        self.ruudukko.ruudut[13][7] = merkki
        self.ruudukko.ruudut[14][6] = merkki
        self.assertTrue(self.ruudukko.viiden_suora(merkki))
