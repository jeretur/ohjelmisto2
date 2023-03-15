class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirry_kerrokseen(self, tavoite_kerros):
        while self.kerros < tavoite_kerros:
            if tavoite_kerros > self.ylinkerros:
                tavoite_kerros = self.ylinkerros
            self.kerros_ylos()
        while self.kerros > tavoite_kerros:
            if tavoite_kerros < self.alinkerros:
                tavoite_kerros = self.alinkerros
            self.kerros_alas()

    def kerros_ylos(self):
        self.kerros += 1
        print(f'Hissi on kerroksessa {self.kerros}')

    def kerros_alas(self):
         self.kerros -= 1
         print(f'Hissi on kerroksessa {self.kerros}')
class Talo:

    def __init__(self, alinkerros, ylinkerros, hissi_lukumr):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissi_lukumr = hissi_lukumr
        self.hissit = []
        for i in range (hissi_lukumr):
            self.hissit.append(Hissi(alinkerros, ylinkerros))

    def ajahissia(self, hissi_numero, kohdekerros):
        self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen(self.alinkerros)
            print(f"\n")


talo = Talo(1, 8, 3)

talo.ajahissia(1, 5)
print(f"\n")
talo.ajahissia(2, 7)
print(f"\n")
print(f"Talo palaa, kaikki hissit pohjakerrokseen!")
talo.palohalytys()