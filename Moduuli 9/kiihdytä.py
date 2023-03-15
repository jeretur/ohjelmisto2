class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
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


auto = Auto("ABC-123", 142, 0, 0)
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f'Rekkari: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} \n'
      f'Nopeus: {auto.nopeus} Matka: {auto.matka}')

auto.kiihdyta()
print(f'Rekkari: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} \n'
      f'Nopeus: {auto.nopeus} Matka: {auto.matka}')