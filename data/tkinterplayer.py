import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinterboard import TkinterBoard 

class TkinterPlayer:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path
        self.token_images = []
        self.players = []
        self.current_player_index = 0
        self.properties = []
        self.chance_cards = []
        self.community_chest_cards = []
        self.app = TkinterBoard(root, "data/images/b1.png")    

    def setup_screen(self):
        self.root.attributes('-fullscreen', False)
        original_image = Image.open(self.image_path)
        window_height = self.root.winfo_screenheight()
        window_width = window_height
        resized_image = original_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")

        self.place_player_tokens()

    def place_player_tokens(self):
        tokens = [
            ("data/images/battleship.png"),
            ("data/images/racecar.png"),
            ("data/images/tophat.png"),
            ("data/images/dog.png"),
            ("data/images/cat.png"),
            ("data/images/penguin.png"),
            ("data/images/rubber_duck.png"),
            ("data/images/thimble.png")
        ]
        selected_tokens = random.sample(tokens, 3)
        token1, token2, token3 = selected_tokens

        with open("selected_token.txt", "r") as file:
            player_token_name = file.read().strip()
            player_token_path = next(path for name, path in zip(["Battleship", "Race Car", "Top Hat", "Scottish Terrier", "Cat", "Penguin", "Rubber Ducky", "Thimble"], tokens) if name == player_token_name)
        
        player_positions = {
            "Player": (self.root.winfo_screenwidth() - 620, self.root.winfo_screenheight() - 100),
            "Bot 1": (self.root.winfo_screenwidth() -580, self.root.winfo_screenheight() -100 ),
            "Bot 2": (self.root.winfo_screenwidth() - 620, self.root.winfo_screenheight() - 60),
            "Bot 3": (self.root.winfo_screenwidth() - 580, self.root.winfo_screenheight() - 60)
        }

        poriginal_image = Image.open(player_token_path)
        presized_image = poriginal_image.resize((50, 50), Image.Resampling.LANCZOS)
        self.player_token_image = ImageTk.PhotoImage(presized_image)

        for i, (path) in enumerate(selected_tokens):
            original_image = Image.open(path)
            resized_image = original_image.resize((50, 50), Image.Resampling.LANCZOS)
            tk_image = ImageTk.PhotoImage(resized_image)
            self.token_images.append(tk_image)

        player_token_images = {
            "Player": self.player_token_image,
            "Bot 1": self.token_images[0],
            "Bot 2": self.token_images[1],
            "Bot 3": self.token_images[2]
        }


        for player, position in player_positions.items():
            x, y = position
            image = player_token_images[player]
            if image:
                self.canvas.create_image(x, y, anchor=tk.CENTER, image=image)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monopoly Controls")
    app = TkinterPlayer(root, "data/images/boards/monopony.gif")
    app.setup_screen()
    root.mainloop()
