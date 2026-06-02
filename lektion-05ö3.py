class student:
    def __init__(self, namn, år):
        self.namn = namn
        self.år = år
    
    def greet(self):
        return f"Hej, jag heter {self.namn} och går årskurs {self.år}."
    
obj1 = student("Emma", 9)

print(obj1.greet())