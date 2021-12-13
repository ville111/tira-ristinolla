import unittest
from ristinolla.transponointitaulukko import Transponointitaulukko
from ristinolla.merkinta import Merkinta




class TransponointitaulukkoTest(unittest.TestCase):
    def setUp(self):
        self.taulukko = Transponointitaulukko()   
        self.ruudut =  [[-1]* 20 for i in range(20)]



