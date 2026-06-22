class Ormanlik:
    def __init__(self, b4, b8):
        self.b4 = b4
        self.b8 = b8




    def hesapla(self):
        payda = self.b8 + self.b4
        pay = self.b8 - self.b4
        return pay / payda
