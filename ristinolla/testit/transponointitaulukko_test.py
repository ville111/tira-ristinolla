import unittest
from ristinolla.transponointitaulukko import Transponointitaulukko
from ristinolla.merkinta import Merkinta




class TransponointitaulukkoTest(unittest.TestCase):
    def setUp(self):
        self.taulukko = Transponointitaulukko()   
        self.ruudut =  [[-1]* 20 for i in range(20)]


    def test_tallenna_ruudukko(self):
        self.ruudut[0][0] = "X"
        self.ruudut[1][0] = "X"
        self.ruudut[2][0] = "X"
        hash = self.taulukko.tallenna(self.ruudut, Merkinta.MAKSIMOIJA, 10, True)
        self.assertEqual(self.taulukko.hae_hash(hash).id, hash)

