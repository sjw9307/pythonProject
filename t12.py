from tkinter import *
from PIL import Image, ImageTk


def create_photo_label(window, img_path, row, column):
    # try:
        photo = Image.open(img_path)
        tk_img = ImageTk.PhotoImage(photo)
        label = Label(window, image=tk_img)
        label.image = tk_img  # keep a reference to the image to prevent garbage collection
        label.grid(row=row, column=column)
    # except Exception as e:
    #     print(f"Failed to load image {img_path}. Error: {e}")

def button_click_event():
    print("Button clicked!")

def main():
    window = Tk()

    image_paths = [
        "/Users/mac/PycharmProjects/pythonProject/photo/images.png",
        "/Users/mac/PycharmProjects/pythonProject/photo/images-1.png",
        "/Users/mac/PycharmProjects/pythonProject/photo/images-2.png",
        # Add more paths if needed
    ]

    for i, path in enumerate(image_paths):
        create_photo_label(window, path, 0, i)

    button = Button(window, text="Click me!", command=button_click_event)
    button.grid(row=1, column=0, columnspan=len(image_paths))  # span the button across all columns

    window.mainloop()

if __name__ == "__main__":
    main()