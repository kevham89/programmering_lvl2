class book:
    def __init__(self, title, author, year): # init method
        #self måste alltid vara första parametern i alla metoder. Detta är för att berätta till programmet att metoden tillhör ett objekt i klassen.
        # attribut = parameter
        self.title = title
        self.author = author
        self.year = year

    def describe(self): # Method
        return f"{self.title} by {self.author}, published in {self.year}"
    
# outside class /
# Skapa ett objekt/instans av klassen bok

book1 = book("The Stockholm City", "Pierre Gergi", 2018) # object
print(book1.title) # får attributen direkt
print(book1.desribe()) # kallar metoden "describe" som retunerar alla 3 attribut.

