class Julkaisu:

    julkaisu_maara = 0

    def __init__(self, nimi, kirjailija, sivut):
        Julkaisu.julkaisu_maara = Julkaisu.julkaisu_maara + 1
        self.kirjannro = Julkaisu.julkaisu_maara
        self.nimi = nimi
        self.kirjailija = kirjailija
        self.sivut = sivut
    def tulosta_tiedot(self):
        print(f'{self.kirjannro} {self.nimi} {self.kirjailija} {self.sivut}')
class Lehti(Julkaisu):

    def __init__(self, nimi, toimittaja):
        Lehti.julkaisu_maara = Lehti.julkaisu_maara + 1
        self.lehdennro = Lehti.julkaisu_maara
        self.nimi = nimi
        self.toimittaja = toimittaja
    def tulosta_tiedot(self):
        print(f'{self.lehdennro} {self.nimi} {self.toimittaja}')

julkaisut = []

julkaisut.append(Lehti('Aku Ankka', 'Aki Hyyppä'))
julkaisut.append(Julkaisu('Hytti n:o 6', 'Rosa Linksom', 200))

for i in julkaisut:
    i.tulosta_tiedot()