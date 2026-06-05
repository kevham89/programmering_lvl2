from MyClasses import allmänna, chef
anställda = []
while True:
    input_namn = input("Vad heter du?: ")
    input_avdelning = input("Vilken avdelning jobbar du på?: ")
    try:
        input_lön = int(input("Hur mycket tjänar du?: "))
    except ValueError:
        print("Fel värde, mata endast en siffra.")
        continue
    input_chef = input("Är du chef på avdelningen?:" )
    if input_chef == "ja":
        try:
            input_kostymer = int(input("Hur många kostymer har du?"))
        except ValueError:
            print("Fel värde, mata endast en siffra.")
            continue
        anställda.append(chef(input_namn, input_avdelning, input_lön, input_chef, input_kostymer))
    else:
        anställda.append(allmänna(input_namn, input_avdelning, input_lön))

    fortsätt = input("Vill du lägga till fler anställda? (ja/nej): ")
    if fortsätt.lower() != "ja":
        break
    
for personer in anställda:
    print(personer.printinfo())
