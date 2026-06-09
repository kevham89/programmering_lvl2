import tkinter as tk
from tkinter import messagebox

def show_message():
    user_input = entry.get()
    messagebox.showinfo("Meddelande", f"Du skrev: {user_input}")

root = tk.Tk()
root.title("Inmatningsfällt och knapp.")
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
button = tk.Button(root, text="Visa meddelande", command=show_message)
button.pack(pady=5)
root.mainloop()