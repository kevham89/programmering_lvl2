### ÖVNING 1 ###
class person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder
    def printinfo(self):
        return f"Jag heter {self.namn}, är {self.ålder}"
class lärare(person):
    def __init__(self, namn, ålder, ämne):
        super().__init__(namn, ålder)
        self.ämne = ämne
    def printinfo(self):
        info = super().printinfo()
        return f"{info} och undervisar i {self.ämne}."
    
### ÖVNING 2 ###
class allmänna:
    def __init__(self, namn, avdelning, lön):
        self.namn = namn
        self.avdelning = avdelning
        self.lön = lön
    def printinfo(self):
        return f"Jag heter {self.namn}, jobbar på avdelningen {self.avdelning}, och jag har {self.lön}SEK i månadslön."

class chef(allmänna):
    def __init__(self, namn, avdelning, lön, chef, kostymer):
        super().__init__(namn, avdelning, lön)
        self.chef = chef
        self.kostymer = kostymer
    def printinfo(self):
        allmännainfo = super().printinfo()
        return f"{allmännainfo} Jag är chef på {self.avdelning}, och jag har {self.kostymer} stycken kostymer."
