zobrist_hash.py

import random


class Zobrist_hash:

    def __init__(self, id = None):
        self.zobrist_taulukko = [[random.randint(1,2**64 - 1) for i in range(2)] for j in range(400)]
        self.id = id
    

    def hash_lisaa(self, hash, x, y, merkki):
        hash ^= self.zobrist_taulukko[x*y][merkki]
        self.id = hash
        return hash


    def hash_poista(self, hash, x,y, merkki):
        return hash
    
    
    def hash_arvo(self, ruudukko):
        hash = 0
        for i in range(20):
            for j in range(20):
                if ruudukko[i][j] != -1:
                    merkki = 0
                    if ruudukko[i][j] == "X":
                        merkki = 1
                    hash ^= self.zobrist_taulukko[i*j][merkki]
        self.id = hash
        return hash

   