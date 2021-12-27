from ristinolla.merkinta import Merkinta
import random


class Transponointitaulukko():

    def __init__(self):
        self.merkinnat = {}
        self.zobrist_taulukko = [[random.randint(1,2**64 - 1) \
                    for i in range(2)] for j in range(400)]


    def tallenna(self, ruudukko, selite:int, arvo:int, syvyys:int, paras_siirto = None):
        hash = self.hash_arvo(ruudukko)
        merkinta = self.hae_hash(hash)
        if merkinta is None:
            merkinta = Merkinta(hash)
        merkinta.aseta_arvo(arvo, syvyys, selite)
        self.paras_siirto = paras_siirto
        self.merkinnat[hash] = merkinta
        return hash


    def tallenna_avaimella(self, hash_key, selite:int, arvo:int, syvyys:int, maksimoija):
        merkinta = self.hae_hash(hash_key)
        if merkinta is None:
            merkinta = Merkinta(hash_key)
        merkinta.aseta_arvo(arvo, syvyys, selite, maksimoija)
        self.merkinnat[hash_key] = merkinta
        return hash_key


    def hae_hash(self, hash_key):
        """ hakee hakee merkinnän hashin perusteella 
        """
        if hash_key in self.merkinnat.keys():
            return self.merkinnat[hash_key]
        return None


    def hae_merkinta(self, ruudukko):
        return self.hae_hash(self.hash_arvo(ruudukko))


    def hae_arvo(self, ruudukko, syvyys:int, alfa:int, beta:int):
        merkinta =  self.hae_merkinta(ruudukko)
        if not merkinta is None:
            return merkinta.hae_arvo(syvyys, alfa, beta)
        return None


    def hash_lisaa(self, hash_key, x, y, merkki):
        z_merkki = 0
        if merkki == "X":
            z_merkki = 1
        hash_key ^= self.zobrist_taulukko[x*y][z_merkki]
        return hash_key
    

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




