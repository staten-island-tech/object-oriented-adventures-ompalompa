import tkinter as tk
from PIL import Image, ImageTk

class TkinterBoard:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

    def clear_screen(self):
        self.canvas.delete("all")

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
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Monopoly", font=("Comic Sans MS", 80, "bold"), fill="white")

        button_font = ("Comic Sans MS", 40, "bold")
        
        self.makebutton("Play", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 - 80, self.token)
        self.makebutton("Rules", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2, self.rules)
        self.makebutton("Credits", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 + 80, self.credits)
        self.makebutton("Quit", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 + 160, self.quit)

    def makebutton(self, text, font, x, y, command):
        text_id = self.canvas.create_text(x, y, text=text, font=font, fill="white")
        self.canvas.tag_bind(text_id, "<Button-1>", lambda event: command())

    def token(self):
        print("play")

 
    def rules(self):
        self.clear_screen()
        x = "Rules"
        self.setup_screen(x)
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Rules", font=("Comic Sans MS", 80, "bold"), fill="white")

        frame = tk.Frame(self.canvas, bg="white")
        frame_window = self.canvas.create_window(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2,  window=frame, width=self.root.winfo_screenwidth() * 0.8, height=self.root.winfo_screenheight() * 0.6)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Comic Sans MS", 14))
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        with open("rules.txt", "r") as file:
            rules_text = file.read()
        
        text_widget.insert(tk.END, rules_text)
        text_widget.config(state=tk.DISABLED)

    def credits(self):
        print("credit")

    def quit(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterBoard(root, "data/images/b1.png")
    app.mainscreen()
    root.mainloop()
