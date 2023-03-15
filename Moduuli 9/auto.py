class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
auto = Auto("ABC-123", '142km/h', 0, 0)
print(f'Rekkari: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} \n'
      f'Nopeus: {auto.nopeus} Matka: {auto.matka}')