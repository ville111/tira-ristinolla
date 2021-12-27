
class Merkinta:

    YLARAJA = 1
    ALARAJA = 0
    TARKKA = 2

    def __init__(self, id_hash):
        self.id = id_hash
        self.arvo = None
        self.selite = None
        self.syvyys = 0
        self.paras_siirto = None
        self.tietokonepelaaja = None

    def aseta_arvo(self, arvo:int, syvyys:int, selite:int, maksimoija):
        self.syvyys = syvyys
        self.arvo = arvo
        self.selite = selite
        self.tietokonepelaaja = maksimoija

    def hae_arvo(self, syvyys:int, alfa:int, beta:int):
        if self.syvyys >= syvyys:
            if self.selite == Merkinta.TARKKA:
                return self.arvo
            if self.selite == Merkinta.YLARAJA and self.arvo <= alfa:
                return alfa
            if self.selite == Merkinta.ALARAJA and self.arvo >= beta:
                return beta
        return None
