from tkinter import *
counter = 0

def process():
    global counter
    counter += 1
    label["text"] = "clicked times:" + str(counter)
    # print("button clicked.", counter)

w = Tk()
w.title("Button event")

label = Label(w)
b1 = Button(w, text="click here", command = process)

b1.pack()
label.pack()

w.mainloop()