from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class TkinterBoard:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

    def setup_screen(self,title):
        self.root.title(title)
        self.root.attributes('-fullscreen', True)
        original_image = Image.open(self.image_path)
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        resized_image = original_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        background_label = tk.Label(self.root, image=tk_image)
        background_label.image = tk_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        

    def mainscreen(self):
        x = "Monopoly"
        self.setup_screen(x)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterBoard(root, "data/images/b1.png")
    app.mainscreen()
    root.mainloop()
