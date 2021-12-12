
class Merkinta:

    MAKSIMOIJA = True
    MINIMOIJA = False

    def __init__(self, id):
        self.id = id
        self.maksimi = None
        self.minimi = None
        self.syvyys = 0

    
    def maksimiarvo(self, arvo:int, syvyys:int):
        if syvyys > self.syvyys:
            self.syvyys = syvyys
            self.maximi = arvo

    
    def minimiarvo(self, arvo:int, syvyys:int):
        if syvyys > self.syvyys:
            self.syvyys = syvyys
            self.minimi = arvo





        