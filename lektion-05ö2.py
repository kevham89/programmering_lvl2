class customer: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hej, jag heter {self.name} och är {self.age} år gammal."
    
obj1 = customer("Alice", 30)

print(obj1.greet())
    