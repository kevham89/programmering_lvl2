def namn():
    return input("Vad heter du? ")
def pnamn(input_namn):
    print(f"Hejsan {input_namn.title()}!")
def pnummer():
    while True:
        try:
            return int(input("Vad har du för nummer? "))
        except ValueError:
            print("Ogiligt nummer, försök igen!")
def save_file(pnamn, pnummer):
    with open("save.txt", "a") as fil:
        fil.write(pnamn + "," + str(pnummer) + "\n")
        print("Data sparad!")
def read_file():
    with open("save.txt", "r") as fil:
        MyContent = fil.read()
        print(MyContent)
def myaddition(x, y):
    return x + y
def mysubtraction(x, y):
    return x - y
def mymultiplication(x, y):
    return x * y
def mydivision(x, y):
    if x == 0:
        print("du kan inte dela med 0")
        return 0
    return x / y
