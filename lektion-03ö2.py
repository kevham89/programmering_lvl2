import os, csv
def save_data(namn, betyg):
    MyFolder = "c:/Skola/Git-repo/programmering_lvl2/datalagring"
    MyPath = os.path.join(MyFolder, "lektion-03ö2data.csv")
    HeaderExists = os.path.exists(MyPath)
    with open(MyPath, "a", newline="", encoding="utf-8") as fil:
        FileWrite = csv.writer(fil)
        if not HeaderExists:
            FileWrite.writerow(["Namn", "Betyg"])
        FileWrite.writerow([namn, betyg])    
        print("Data Sparad!")
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
        namn = input("Ange elevnamn: ")
        betyg = input(f"Ange betyg för {namn}: ")
        MyData.append({"namn": namn, "betyg": betyg})
    return MyData
while True:
    print("1. Mata in data")
    print("2. Spara data till fil")
    print("3. Läs data från fil")
    print("4. Avsluta")
    try:
        val = int(input("Gör ett val: "))
    except ValueError:
        print("Ange ett giltigt nummer.")
        continue
    if val == 1:
        MyData = insert_data()
    elif val == 2:
        try:
            for elev in MyData:
                save_data(elev["namn"], elev["betyg"])
        except NameError:
            print("Det finns ingen data att spara.")
    elif val == 3:
        read_data()
    elif val == 4:
        break
    else:
        print("Ange ett giltigt nummer.")