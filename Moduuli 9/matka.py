class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = 2000

    def kiihdyta(self, nopeudenmuutos):
        if nopeudenmuutos < 0:
            uusinopeus = nopeudenmuutos + self.nopeus
            if uusinopeus < 0:
                self.nopeus = 0
            else:
                self.nopeus = uusinopeus
        else:
            uusinopeus = nopeudenmuutos + self.nopeus
            if uusinopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            else:
                self.nopeus = uusinopeus

    def kulje(self, matka_muutos):
        kuljettu = self.nopeus * matka_muutos
        uusi_matka = self.matka + kuljettu
        self.matka = uusi_matka


auto = Auto("ABC-123", 142, 60, 0)
auto.kulje(1.5)
auto.kiihdyta(30)
auto.kulje(2)
print(f'Rekkari: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus}km/h \n'
      f'Nopeus: {auto.nopeus}km/h Matka: {auto.matka}')
