from MyClasses import general, specific

bilar = []
while True:
    input_märke = input("Vilket märke?: ")
    input_model = input("Vilken model?: ")
    input_år = input("Vilket år?: ")
    input_dörrar = input("Hur många dörrar?:" )

    bilar.append(specific(input_märke, input_model, input_år, input_dörrar))

    fortsätt = input("Vill du lägga en till bil? (ja/nej): ")
    if fortsätt.lower() != "ja":
        break
    
for x in bilar:
    print(x.printcar())
