# -----------------------------------------------------------------
# Library modules
# -----------------------------------------------------------------
import os, csv

# -----------------------------------------------------------------
# Sökväg
# -----------------------------------------------------------------
MyFolder    = os.path.dirname(os.path.abspath(__file__))
DataFolder  = os.path.join(MyFolder, "datalagring")
FilePath    = os.path.join(DataFolder, "lektion-03ö2data.csv")
# -----------------------------------------------------------------
# Funktioner
# -----------------------------------------------------------------
def save_data(fNamn, eNamn, Kurs, Betyg):
    os.makedirs(DataFolder, exist_ok=True)
    HeaderExists = os.path.exists(FilePath)
    with open(FilePath, "a", newline="", encoding="utf-8") as fil:
        FileWrite = csv.writer(fil)
        if not HeaderExists:
            FileWrite.writerow(["Förnamn", "Efternamn", "Kurs", "Betyg"])
        FileWrite.writerow([fNamn, eNamn, Kurs, Betyg])    
def read_data():
    if not os.path.exists(FilePath):
        print("Filen finns inte än.")
        return
    with open(FilePath, "r", encoding="utf-8") as fil:
        MyContent = fil.read()
        if MyContent == "":
            print("Filen är tom.")
        else:
            print(MyContent)
def insert_data():
    MyData = []
    try:
        antal = int(input("Hur många elever vill du registrera?: "))
    except ValueError:
        print("Fel värde, mata endast en siffra.")
        return []
    for x in range(antal):
        fNamn = input("Ange förnamn: ").strip().capitalize()
        eNamn = input("Ange efternamn: ").strip().capitalize()
        Kurs = input("Ange Kurs: ").strip().capitalize()
        while True:
            Betyg = input(f"Ange Betyg (A-F) för {fNamn} {eNamn} i {Kurs}: ").strip().upper()
            if Betyg in ['A', 'B', 'C', 'D', 'E', 'F']:
                break
            print("Ogiltigt betyg: ")
        MyData.append({"Förnamn": fNamn, "Efternamn": eNamn, "Kurs": Kurs, "Betyg": Betyg})
    return MyData
def nav():
    print("1. Mata in data")
    print("2. Spara data till fil")
    print("3. Läs data från fil")
    print("4. Avsluta")
    try:
        val = int(input("Gör ett val: "))
        return val
    except ValueError:
        print("Ange ett giltigt nummer.")
        return None
# -----------------------------------------------------------------
# Huvudprogram
# -----------------------------------------------------------------
while True:
    val = nav()
    if val == 1:
        MyData = insert_data()
    elif val == 2:
        try:
            if not MyData:
                print("Det finns ingen data att spara")
            else:
                for elev in MyData:
                    save_data(elev["Förnamn"], elev["Efternamn"], elev["Kurs"], elev["Betyg"])
                print("Data Sparad!")
        except NameError:
            print("Det finns ingen data att spara.")
    elif val == 3:
        read_data()
    elif val == 4:
        break
    else:
        print("Ange ett giltigt nummer.")