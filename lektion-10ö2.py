import tkinter as tk

class Bok():
    def __init__(self, title, författare):
        self.title = title
        self.författare = författare
    def visa_info(self):
        return (f"{self.title} av {self.författare}")
    def läsa(self):
        return ("Läser boken.")

class EBok(Bok):
    def __init__(self, title, författare, filstorlek):
        super().__init__(title, författare)
        self.filstorlek = filstorlek
    def visa_info(self):
        return (f"{self.title} av {self.författare}, Filstorlek: {self.filstorlek}")
    def ladda_ner(self):
        return ("Laddar ner boken.")

bok1 = Bok("Parry Hotter", "J.K. Bowling")
bok2 = EBok("Parry Hotter 2", "J.K. Bowling", "198GB")

def Bok1():
    label.config(text={bok1.visa_info()})
def Bok2():
    label.config(text={bok2.visa_info()})

root = tk.Tk()
root.title("Deltagarlista")
root.geometry("800x400")

label = tk.Label(root, text="Välj bok!", font=("Arial", 24))
label.pack(pady=10)

button1 = tk.Button(root, text="Bok - 1", command=Bok1)
button1.pack(pady=10, padx=10)
button2 = tk.Button(root, text="EBok - 2", command=Bok2)
button2.pack(pady=10, padx=10)

root.mainloop()