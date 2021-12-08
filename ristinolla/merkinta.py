
class Merkinta:

    MAKSIMOIJA = True
    MINIMOIJA = False

    def __init__(self, id):
        self.id = id
        self.maksimi = None
        self.minimi = None
    
    def maksimiarvo(self, arvo:int):
        self.maximi = arvo
    
    def minimiarvo(self, arvo:int):
        self.minimi = arvo





        