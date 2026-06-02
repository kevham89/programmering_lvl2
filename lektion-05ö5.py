class bicycle:
    def __init__(self, brand, model, year, gear_count):
        self.brand = brand
        self.model = model
        self.year = year
        self.gear_count = gear_count
    def change_gear(self, gear_count):
        self.gear_count = gear_count
    def display_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear:{self.year}\nGears: {self.gear_count}"
    
bike1 = bicycle("Trek", "Marlin 7", 2023, 21)
bike2 = bicycle("Giant", "Talon 1", 2022, 24)

print(bike1.change_gear(18))
print(bike1.display_info())
print(bike2.display_info())