# -----------------------------------------------------------------
# Library modules
# -----------------------------------------------------------------
import os, csv

# -----------------------------------------------------------------
# Funktioner
# -----------------------------------------------------------------
def save_data(fNamn, eNamn, Kurs, Betyg):
    MyFolder = "c:/Skola/Git-repo/programmering_lvl2/datalagring"
    MyPath = os.path.join(MyFolder, "lektion-03ö2data.csv")
    HeaderExists = os.path.exists(MyPath)
    with open(MyPath, "a", newline="", encoding="utf-8") as fil:
        FileWrite = csv.writer(fil)
        if not HeaderExists:
            FileWrite.writerow(["Förnamn", "Efternamn", "Kurs", "Betyg"])
        FileWrite.writerow([fNamn, eNamn, Kurs, Betyg])    
def read_data():
    MyFolder = "c:/Skola/Git-repo/programmering_lvl2/datalagring"
    MyPath = os.path.join(MyFolder, "lektion-03ö2data.csv")
    with open(MyPath, "r", encoding="utf-8") as fil:
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
        fNamn = input("Ange förnamn: ").strip()
        eNamn = input("Ange efternamn: ").strip()
        Kurs = input("Ange Kurs: ").strip()
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
            for elev in MyData:
                save_data(elev["Förnamn"], elev["Efternamn"], elev["Kurs"], elev["Betyg"])
        except NameError:
            print("Det finns ingen data att spara.")
        print("Data Sparad!")
    elif val == 3:
        read_data()
    elif val == 4:
        break
    else:
        print("Ange ett giltigt nummer.")