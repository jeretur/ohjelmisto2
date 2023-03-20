class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kulje(self, matka_muutos):
        kuljettu = self.nopeus * matka_muutos
        uusi_matka = self.matka + kuljettu
        self.matka = uusi_matka

    def kiihdyta(self, muutos):
        if self.nopeus + muutos >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + muutos < 0:
            self.nopeus = 0
        else:
            self.nopeus += muutos

class Sahko(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akku = akku


class Bensa(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki):
        self.tankki = tankki
        super().__init__(rekisteritunnus, huippunopeus)

sahko = Sahko('ABC-123', 180, 52.5)
auto2 = Bensa('ABC-321', 165, 32.2)
sahko.kiihdyta(50)
auto2.kiihdyta(30)
sahko.kulje(1)
auto2.kulje(3)
print(f'Kuljettu matka {sahko.matka} Nopeus {sahko.nopeus} Huippunopeus {sahko.huippunopeus}')
print(f'Kuljettu matka {auto2.matka} Nopeus {auto2.nopeus} Huippunopesu {auto2.huippunopeus}')