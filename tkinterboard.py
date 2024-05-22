from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class TkinterBoard:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

<<<<<<< Updated upstream:tkinterboard.py
    def setup_screen(self,title):
        global background_label
=======
    def setup_screen(self, title):
>>>>>>> Stashed changes:data/tkinterboard.py
        self.root.title(title)
        self.root.attributes('-fullscreen', True)
        

    def mainscreen(self):
        x = "Monopoly"
        self.setup_screen(x)

        original_image = Image.open(self.image_path)
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        resized_image = original_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
<<<<<<< Updated upstream:tkinterboard.py
        tk_image = ImageTk.PhotoImage(resized_image)
        background_label = tk.Label(self.root, image=tk_image)
        background_label.image = tk_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Monopoly", font=("Comic Sans MS", 80, "bold"), fill="white")
        canvas.place(relx=0,rely=0,relheight=1,relwidth=1)

=======
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")

    def mainscreen(self):
        x = "Monopoly"
        self.setup_screen(x)
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10,
                                text="Monopoly", font=("Comic Sans MS", 80, "bold"), fill="white")
>>>>>>> Stashed changes:data/tkinterboard.py

    def gameselection(self):
        print("hi")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterBoard(root, "data/images/b1.png")
    app.mainscreen()
    root.mainloop()
