class Pelaaja:
    """ Pelaaja mallintava luokka. Tätä käytetään pelilogiikassa
        kun pitää tietä mikä merkki pelaajalla ja myös välittämään hiirellä valitut ruudut. Kun käyttäjä
        valitsee pelikentältä ruudun tieto tallennetaan aseta_piste-metodilla. Ja pelilogiikka kysyy siirrä-metodilla
        mihin ruutuun merkki laitettiin. Tuleva tietokone pelaaja tulee käytämään tätä samaa formaattia (rajapintana).
    
    """

    def __init__(self, merkki:str, nimi:str):
        self.merkki = merkki
        self.nimi = nimi
        self.x = -1
        self.y = -1


    def aseta_piste(self, x:int, y:int):
        self.x = x
        self.y = y
    

    def siirra(self):
        if not self.x == -1 and not self.y == -1:
            x = self.x
            y = self.y
            self.x = -1
            self.y = -1
            return self.merkki, x, y
        else:
            return None
    