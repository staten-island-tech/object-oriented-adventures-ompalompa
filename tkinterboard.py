import tkinter as tk
from PIL import Image, ImageTk

class TkinterBoard:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

    def setup_screen(self, title):
        self.root.title(title)
        self.root.attributes('-fullscreen', True)
        original_image = Image.open(self.image_path)
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        resized_image = original_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")

    def mainscreen(self):
        x = "Monopoly"
        self.setup_screen(x)
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10,
                                text="Monopoly", font=("Comic Sans MS", 80, "bold"), fill="white")

    def gameselection(self):
        print("hi")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterBoard(root, "data/images/b1.png")
    app.mainscreen()
    root.mainloop()
