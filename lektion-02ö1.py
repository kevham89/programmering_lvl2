from mina_funktioner import namn, pnamn, pnummer, save_file, read_file
while True:
    print("1. Ange data")
    print("2. Spara data")
    print("3. Läs data")
    print("4. Stoppa programmet")
    val = input("Mata in ditt val: ")
    try:
        val = int(val)
    except ValueError:
        print("Ange en siffra!")
        continue        
    if val == 1:
        input_namn = namn()
        pnamn(input_namn)
        input_nummer = pnummer()
    elif val == 2:
        save_file(input_namn, input_nummer)
    elif val == 3:
        read_file()
    elif val == 4:
        break
    else:
        print("fel val")