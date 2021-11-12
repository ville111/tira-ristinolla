import unittest
from ristinolla.pelaaja import Pelaaja



class PelaajaTest(unittest.TestCase):
    def setUp(self):
        self.pelaaja = Pelaaja("X")

    
    def test_aseta_piste(self):
        self.pelaaja.aseta_piste(1,1)
        self.assertEqual(self.pelaaja.x, 1)
        self.assertEqual(self.pelaaja.y, 1)   


    def test_siirra(self):
        self.pelaaja.aseta_piste(2,2)
        merkki, x, y = self.pelaaja.siirra()
        tulos = f"{merkki} {x} {y}"
        vakio = "X 2 2"
        self.assertEqual(tulos, vakio)   
   

    def test_siirra_ei_pistetta(self):
        self.pelaaja = Pelaaja("X")
        self.assertIsNone(self.pelaaja.siirra()) 
