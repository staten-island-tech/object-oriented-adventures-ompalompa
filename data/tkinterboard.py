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
        self.label = tk.Label(self.root, text="Monopoly", font=("Comic Sans MS", 48, "bold"), fg="white", bg="black")
        self.label.config(bg='black')  # Set background color to black
        self.label.pack(expand=True)
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.label.bind("<Button-1>", self.gameselection)

    def gameselection(self):
        print("Hi")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterBoard(root, "data/images/Monopoly.png")
    app.mainscreen()
    root.mainloop()
