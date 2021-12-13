
class Merkinta:

    YLARAJA = 1
    ALARAJA = 0
    TARKKA = 2

    def __init__(self, id):
        self.id = id
        self.arvo = None
        self.selite = None
        self.syvyys = 0
        self.paras_siirto = None

    def aseta_arvo(self, arvo:int, syvyys:int, selite:int):
        self.syvyys = syvyys
        self.arvo = arvo
        self.selite = selite

    def hae_arvo(self, syvyys:int, alfa:int, beta:int):
        if self.syvyys >= syvyys:
            if self.selite == Merkinta.TARKKA:
                return self.arvo
            if self.selite == Merkinta.YLARAJA and self.arvo <= alfa:
                return alfa
            if self.selite == Merkinta.ALARAJA and self.arvo >= beta:
                return beta
        return None


    







        