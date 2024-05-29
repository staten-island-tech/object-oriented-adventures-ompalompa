import tkinter as tk
from PIL import Image, ImageTk

class TkinterBoard:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path
        self.token_images = []

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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
        
        self.makebutton("Play", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 - 80, self.name)
        self.makebutton("Rules", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2, self.rules)
        self.makebutton("Credits", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 + 80, self.credits)
        self.makebutton("Quit", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 + 160, self.quit)

        self.root.bind("<Right>", lambda event: self.name())
        self.root.bind("<Up>", lambda event: self.name())

    def makebutton(self, text, font, x, y, command):
        text_id = self.canvas.create_text(x, y, text=text, font=font, fill="white")
        self.canvas.tag_bind(text_id, "<Button-1>", lambda event: command())

    def name(self):
        self.clear_screen()
        x = "Name"
        self.setup_screen(x)
        button_font = ("Comic Sans MS", 20, "bold")
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Enter A Name", font=("Comic Sans MS", 80, "bold"), fill="white")

        self.username = tk.Entry(self.root, font=("Comic Sans MS", 20), bg="light gray")
        self.username.place(relx=0.5,rely=0.3, anchor=tk.CENTER)

        self.makebutton("Enter", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 - 80, command=self.nametoken)

        self.root.bind("<Left>", lambda event: self.mainscreen())
        self.root.bind("<Down>", lambda event: self.mainscreen())
        self.root.bind("<Right>", lambda event: self.game("name"))
        self.root.bind("<Up>", lambda event: self.game("name"))

    def tokencharacter(self):
        self.clear_screen()
        x = "Token"
        self.setup_screen(x)
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Pick a Token", font=("Comic Sans MS", 80, "bold"), fill="white")
        
        tokens = [
            ("Battleship", "data/images/battleship.png"),
            ("Race Car", "data/images/racecar.png"),
            ("Top Hat", "data/images/tophat.png"),
            ("Scottish Terrier", "data/images/dog.png"),
            ("Cat", "data/images/cat.png"),
            ("Penguin", "data/images/penguin.png"),
            ("Rubber Ducky", "data/images/rubber_duck.png"),
            ("Thimble", "data/images/thimble.png")
        ]

        for i, (name, path) in enumerate(tokens):
            original_image = Image.open(path)
            resized_image = original_image.resize((100, 100), Image.Resampling.LANCZOS)
            tk_image = ImageTk.PhotoImage(resized_image)
            self.token_images.append(tk_image) 

            x_pos = self.root.winfo_screenwidth() / 4 + (i % 4) * (self.root.winfo_screenwidth() / 8)
            y_pos = self.root.winfo_screenheight() / 2 + (i // 4) * 150

            image_id = self.canvas.create_image(x_pos, y_pos, image=tk_image)
            text_id = self.canvas.create_text(x_pos, y_pos + 70, text=name, font=("Comic Sans MS", 20, "bold"), fill="white")

            self.canvas.tag_bind(image_id, "<Button-1>", lambda event, token=name: self.tokentoken(token))
            self.canvas.tag_bind(text_id, "<Button-1>", lambda event, token=name: self.tokentoken(token))

        self.root.bind("<Left>", lambda event: self.game("name"))
        self.root.bind("<Down>", lambda event: self.game("name"))
        self.root.bind("<Right>", lambda event: self.mainscreen())
        self.root.bind("<Up>", lambda event: self.mainscreen())

    def game(self, gt):
        self.clear_screen()
        x = "Game"
        self.setup_screen(x)
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Select a Game Type", font=("Comic Sans MS", 80, "bold"), fill="white")

        button_font = ("Comic Sans MS", 40, "bold")

        self.makebutton("Singleplayer", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 - 80, lambda: self.gametoken("Singleplayer"))
        self.makebutton("Multiplayer", button_font, self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 2 - 250, lambda: self.gametoken("Multiplyer"))

        self.root.bind("<Left>", lambda event: self.name())
        self.root.bind("<Down>", lambda event: self.name())
        self.root.bind("<Right>", lambda event: self.tokencharacter())
        self.root.bind("<Up>", lambda event: self.tokencharacter())
 
    def rules(self):
        self.clear_screen()
        x = "Rules"
        self.setup_screen(x)
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Rules", font=("Comic Sans MS", 80, "bold"), fill="white")

        frame = tk.Frame(self.canvas, fill=None)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=self.root.winfo_screenwidth() * 0.8, height=self.root.winfo_screenheight() * 0.6)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Comic Sans MS", 14))
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        with open("rules.txt", "r") as file:
            rules_text = file.read()
        
        text_widget.insert(tk.END, rules_text)
        text_widget.config(state=tk.DISABLED)

        self.root.bind("<Left>", lambda event: self.mainscreen())
        self.root.bind("<Down>", lambda event: self.mainscreen())

    def credits(self):
        self.clear_screen()
        x = "Credits"
        self.setup_screen(x)
        self.canvas.create_text(self.root.winfo_screenwidth() / 2, self.root.winfo_screenheight() / 10, text="Credits", font=("Comic Sans MS", 80, "bold"), fill="white")

        names = [
            ("Jonathan Ou"),
            ("Aaron Li"),
            ("Alvin Huang")
        ]
        start_y = self.root.winfo_screenheight() / 10 + 250
        y_offset = 100
        for i, name in enumerate(names):
            y_position = start_y + i * y_offset
            self.canvas.create_text(self.root.winfo_screenwidth() / 2, y_position, text=name, font=("Comic Sans MS", 40), fill="white")
 
        self.root.bind("<Left>", lambda event: self.mainscreen())
        self.root.bind("<Down>", lambda event: self.mainscreen())
    
    def quit(self):
        self.root.quit()

    def nametoken(self):
        user=self.username.get()
        print(user)
        self.game(None)

    def gametoken(self, gt):
        self.selected_game = gt
        print(self.selected_game)
        self.tokencharacter()

    def tokentoken(self, token):
        print(f"{token}")
        


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterBoard(root, "data/images/b1.png")
    app.mainscreen()
    root.mainloop()
