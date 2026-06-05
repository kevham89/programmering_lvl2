class person: # Base-Class
    # Konstruktor för person-klassen, tar förnamn och efternamn som argument.
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
class student(person): # Sub-Class
    def __init__(self, fname, lname, ålder):
        super().__init__(fname, lname)
        self.ålder = ålder
    def printname(self):
        print(f"{self.firstname}, {self.lastname}, {self.ålder}")

student1 = student("Mike", "Hawk", 18)

student1.printname()