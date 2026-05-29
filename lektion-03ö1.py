import os

def save_data(x1,x2,x3,x4,x5):
    MyFolder = "c:/Skola/Git-repo/programmering_lvl2/datalagring"
    MyPath = os.path.join(MyFolder, "lektion-03data.txt")
    with open(MyPath, "a") as fil:
        fil.write(str(x[1]) + "," + str(x[2]) + "," + str(x[3]) + "," + str(x[4]) + "," + str(x[5]) + "\n")
        print("Data Sparad!")

def read_data():
    MyFolder = "c:/Skola/Git-repo/programmering_lvl2/datalagring"
    MyPath = os.path.join(MyFolder, "lektion-03data.txt")
    with open(MyPath, "r") as fil:
        MyContent = fil.read()
        if MyContent == "":
            print("Filen är tom.")
        else:
            print(MyContent)

while True:
    print("1. Mata in data")
    print("2. Spara data till fil")
    print("3. Läs data från fil")
    print("4. Avsluta")
    try:
        val = int(input("Gör ett val: "))
    except ValueError:
        print("Fel värde, mata endast en siffra.")
        continue
    if val == 1:
        x = {}
        for c in range(1, 6):
            while True:
                try:
                    x[c] = int(input(f"Mata in x{c}: "))
                    break
                except ValueError:
                    print("Fel värde, mata endast en siffra.")
    elif val == 2:
        try:
            save_data(x[1],x[2],x[3],x[4],x[5])
        except NameError:
            print("Det finns ingen data att spara.")
    elif val == 3:
        read_data()
    elif val == 4:
        break
