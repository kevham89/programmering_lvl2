class car: 
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
def get_brand(self):
    return self.__brand
def set_model(self, model):
    self.model = model
    print("Modellen har bytts till:", self.model)

car = car("Toyota", "RAV4")
print(car.get_brand())
car.set_model("Corolla")