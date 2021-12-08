from ristinolla.merkinta import Merkinta
import random


class Transponointitaulukko():

    def __init__(self):
        self.merkinnat = {}
        self.zobrist_taulukko = [[random.randint(1,2**64 - 1) for i in range(2)] for j in range(400)]
    
    
    def tallenna(self, ruudukko, maximi:bool, arvo:int):
        hash = self.hash_arvo(ruudukko)
        merkinta = Merkinta(hash)
        if maximi == Merkinta.MAKSIMOIJA:
            merkinta.maksimiarvo(arvo)
        else:
            merkinta.minimiarvo(arvo)
        self.merkinnat[hash] = merkinta
        return hash


    def hae_hash(self, hash):
        """ hakee ruudukon minimi- tai maksimi-arvon 
        """
        return self.merkinnat[hash]
    
    def hae(self, ruudukko, maksimi):
        hash = self.hash_arvo(ruudukko)
    
        if hash in self.merkinnat.keys():
            merkinta = self.merkinnat[hash]
            if maksimi == Merkinta.MAKSIMOIJA and  not merkinta.maximi is None:
                return merkinta.maximi
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




