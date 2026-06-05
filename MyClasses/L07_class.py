class djur:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder
    def äta(self):
        print("nom nom nom nom nom")
    def sova(self):
        print("snoorrrrrk.. mimimimimimi")
class hund(djur):
    def __init__(self, namn, ras, ålder):
        super().__init__(namn, ålder)
        self.ras = ras
    def skälla(self):
        print("Woff")
class general:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def printcar(self):
        return f"Märke: {self.brand}\nModel: {self.model}\nÅr: {self.year}"
class specific(general):
    def __init__(self, brand, model, year, doors):
        self.doors = doors
        super().__init__(brand, model, year)
    def printcar(self):
        generalinfo = super().printcar()
        return f"{generalinfo}\nDörrar: {self.doors}"