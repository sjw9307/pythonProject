from tkinter import *

window = Tk()
image1 = PhotoImage("/Users/mac/Downloads/IMG_0173.png")
label = Label(window, image=image1)
label.pack()
window.mainloop()