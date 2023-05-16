from tkinter import Tk, Label
from PIL import Image, ImageTk

window = Tk()

photo = Image.open("/photo/images.png")
tk_img = ImageTk.PhotoImage(photo)

photo2 = Image.open("/photo/images-1.png")
tk_img2 = ImageTk.PhotoImage(photo2)

photo3 = Image.open("/photo/images-2.png")
tk_img3 = ImageTk.PhotoImage(photo3)

label = Label(window, image=tk_img)
label2 = Label(window, image=tk_img2)
label3 = Label(window, image=tk_img3)

label.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

window.mainloop()