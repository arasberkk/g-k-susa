class Baraj:
    def __init__ (self, b3, b8):
        self.b3 = b3
        self.b8 = b8



    def ndwi_hesapla(self):
        ndwi_payda = self.b3 + self.b8
        ndwi_pay = self.b3 - self.b8
        return ndwi_pay / ndwi_payda

        

