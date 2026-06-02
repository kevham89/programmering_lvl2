class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def drive(self, speed):
        self.speed = speed
        return f"{self.brand} {self.model} kör i {self.speed} km/h"
    def stop(self):
        self.speed = 0
        return f"{self.brand} {self.model} har stannat. Hastighet = {self.speed} km/h"

car1 = car("Toyota", "Corolla", 2022)
car2 = car("Honda", "Civic", 2021)

print(car1.drive(50))
print(car2.drive(100))

print(car1.stop())
print(car2.stop())