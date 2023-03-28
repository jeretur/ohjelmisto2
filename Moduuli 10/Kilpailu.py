import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = 100
        self.matka = matka

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

    def tulosta(self):

        print(f'Rekkari: {self.rekisteritunnus} Huippunopeus: {self.huippunopeus}km/h '
              f'Nopeus: {self.nopeus}km/h Matka: {self.matka}km')

class Kilpailu:
    def __init__(self, nimi, pituus, lkm):
        self.nimi = 'Suuri romuralli'
        self.pituus = 8000
        self.autot = []
        self.aika = 0

        for i in range (lkm):
            self.autot.append(Auto(f'ABC-{i + 1}', 0, 0, 0))
        while not self.kilpailu_ohi():
            self.tunti_kuluu()
            self.tulosta_tilanne()

    def tunti_kuluu(self):
        self.aika += 1
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        if self.aika % 10 == 0 or self.kilpailu_ohi():
            print(f'\nAika: {self.aika}h')
            for auto in self.autot:
                auto.tulosta()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka > self.pituus:
                return True

Kilpailu('Suuri romuralli', 8000, 10)