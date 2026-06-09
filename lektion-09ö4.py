import tkinter as tk

def show_message():
    user_input = entry.get()
    label.config(text=f"Hejsan {user_input}")

root = tk.Tk()
root.title("Extraövning")

label = tk.Label(root, text="Skriv in ditt namn")
label.pack(pady=10, padx=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10, padx=10)
button = tk.Button(root, text="Klicka här!", command=show_message)
button.pack(pady=10, padx=10)
root.mainloop()