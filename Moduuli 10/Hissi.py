
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

hissi = Hissi(1,8)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(-1)