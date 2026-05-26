from mina_funktioner import myaddition, mymultiplication, mydivision, mysubtraction, namn, pnamn

user = namn()
pnamn(user)

while True:
    värde = input("Skriv två tal ")
    if värde == "quit":
        break
    x, y = int(värde.split()[0]), int(värde.split()[1])

    print(f"{x} + {y} = {myaddition(x, y)}")
    print(f"{x} - {y} = {mysubtraction(x, y)}")
    print(f"{x} * {y} = {mymultiplication(x, y)}")
    print(f"{x} / {y} = {mydivision(x, y)}")


