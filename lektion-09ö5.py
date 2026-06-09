import tkinter as tk
value = 0

def increase():
    global value
    value += 1
    label.config(text=f"{value}")
def decrease():
    global value
    value -= 1
    label.config(text=f"{value}")

root = tk.Tk()
root.title("Extraövning")

label = tk.Label(root, text="0")
label.pack(pady=10, padx=10)

button1 = tk.Button(root, text="increase", command=increase)
button1.pack(pady=10, padx=10)
button2 = tk.Button(root, text="decrease", command=decrease)
button2.pack(pady=10, padx=10)

root.mainloop()