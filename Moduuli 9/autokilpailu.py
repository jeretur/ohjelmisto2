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
lista = []
i = 1
moi = int(input('Syötä numero 1, jotta voit jatkaa: '))
if moi == 1:
    while i <= 10:
        auto = Auto(f"ABC-{i}", 0, 0, 0)

        i += 1
        lista.append(auto)

moi1 = int(input('Syötä numero 2, jotta voit jatkaa: '))
if moi1 == 2:
    while auto.matka < 10000:
        for auto in lista:

            auto.kiihdyta(random.randint(-10, 15))
            if auto.matka > 10000:
                break
            else:
                auto.kulje(1)
for auto in lista:
    print(f'Rekkari: {auto.rekisteritunnus} \nHuippunopeus: {auto.huippunopeus}km/h \n'
          f'Nopeus: {auto.nopeus}km/h \nMatka: {auto.matka} kilometriä \n')

