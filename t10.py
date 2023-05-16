import tkinter as tk

def button1_clicked():
    print("w1")

def button2_clicked():
    print("w2")

window = tk.Tk()
window.title("My Calculator")

button1 = tk.Button(window, width=30, height=50, command=button1_clicked)
button1.pack()

button2 = tk.Button(window, width=30, height=50, command=button2_clicked)
button2.pack()

window.mainloop()
