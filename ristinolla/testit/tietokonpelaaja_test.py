import unittest
from ristinolla.tietokonepelaaja import Tietokonepelaaja
from ristinolla.ruudukko import Ruudukko


class TietokonepelaajaTest(unittest.TestCase):
    def setUp(self):
        self.pelaaja = Tietokonepelaaja("X", "nimi", Ruudukko(20))

    def test_pisteyta(self):
        ruudukko =  [[-1]* 20 for i in range(20)]
        arvo = self.pelaaja.pisteyta(ruudukko)
        self.assertEqual(arvo, 0)

    """
    def test_aseta_piste(self):
        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.x, 1)
        self.assertEqual(self.pelaaja.y, 1)   


    def test_siirra(self):
       pass  
   

    def test_siirra_ei_pistetta(self):
        pass
        #self.assertIsNone(self.pelaaja.siirra()) 

    """