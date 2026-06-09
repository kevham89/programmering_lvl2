import tkinter as tk

def change_text():
    if label.cget("text") == "Detta är ursprunglig text.":
        label.config(text="Texten har ändrats!")
    else:
        label.config(text="Detta är ursprunglig text.")

root = tk.Tk()
root.title("Enkelt Tkinter Exempel")
root.geometry("400x400")

button = tk.Button(root, text="Klicka här", command=change_text)
button.pack(pady=10)

label = tk.Label(root, text="Detta är ursprunglig text.")
label.pack(pady=10)

root.mainloop()
