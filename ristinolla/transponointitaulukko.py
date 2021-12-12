from ristinolla.merkinta import Merkinta
import random


class Transponointitaulukko():

    def __init__(self):
        self.merkinnat = {}
        self.zobrist_taulukko = [[random.randint(1,2**64 - 1) for i in range(2)] for j in range(400)]
    
    
    def tallenna(self, ruudukko, maximi:bool, arvo:int, syvyys:int):
        hash = self.hash_arvo(ruudukko)
        merkinta = self.hae_hash(hash)
        if merkinta is None:
            merkinta = Merkinta(hash) 
        if maximi == Merkinta.MAKSIMOIJA:
            merkinta.maksimiarvo(arvo, syvyys)
        else:
            merkinta.minimiarvo(arvo, syvyys)
        self.merkinnat[hash] = merkinta
        return hash


    def hae_hash(self, hash):
        """ hakee hakee merkinnän hashin perusteella 
        """
        if hash in self.merkinnat.keys():
            return self.merkinnat[hash]
        return None


    def hae(self, ruudukko, maksimi:bool):
        """ hakee ruudukon minimi- tai maksimi-arvon 
        """
        hash = self.hash_arvo(ruudukko)

        if hash in self.merkinnat.keys():
            merkinta = self.merkinnat[hash]
            if maksimi == Merkinta.MAKSIMOIJA and  not merkinta.maksimi is None:
                return merkinta.maksimi
            elif not merkinta.minimi is None:
                return merkinta.minimi
        return None


    def hash_arvo(self, ruudukko):
        hash = 0
        for i in range(20):
            for j in range(20):
                if ruudukko[i][j] != -1:
                    merkki = 0
                    if ruudukko[i][j] == "X":
                        merkki = 1
                    hash ^= self.zobrist_taulukko[i*j][merkki]
        return hash




