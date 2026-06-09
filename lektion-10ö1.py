import os, tkinter as tk

MyFolder = os.path.dirname(os.path.abspath(__file__)) # Hittar vart huvudmappen finns
MyDataFolder = os.path.join(MyFolder, "MyData") # Lägger till filmappen till sökvägen
MyDataFile = os.path.join(MyDataFolder, "resultat.txt") # lägger till filnamnet till sökvägen.

def SaveData(lista):
    os.makedirs(MyDataFolder, exist_ok=True)
    with open(MyDataFile, "a", newline="", encoding="utf-8") as content:
        for namn in lista:
            content.write(f"{namn} Antal bokstäver: {len(namn)}\n")
        print("Data sparad!")

deltagare = ["Anna", "Mohammed", "Elin", "Johan"]

def Save():
    SaveData(deltagare)
    label.config(text=f"Data Sparad!")
def Add():
    AddUser = entry.get()
    deltagare.append(AddUser)
    label.config(text=f"{AddUser} adderad!")
    print("Deltagare adderad!")

root = tk.Tk()
root.title("Deltagarlista")
root.geometry("400x400")

label = tk.Label(root, text="Vad vill du göra?")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10, padx=10)

button1 = tk.Button(root, text="Save", command=Save)
button1.pack(pady=10, padx=10)
button2 = tk.Button(root, text="Add", command=Add)
button2.pack(pady=10, padx=10)

root.mainloop()