import tkinter as tk
from PIL import Image, ImageTk
import random, time

class TkinterLb:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path
        self.history = []

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_screen(self):
        self.root.attributes('-fullscreen', False)
        original_image = Image.open(self.image_path)
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth() - window_height
        resized_image = original_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")

    def makebutton(self, text, font, x, y, command):
        text_id = self.canvas.create_text(x, y, text=text, font=font, fill="white")
        self.canvas.tag_bind(text_id, "<Button-1>", lambda event: command()) 

    def buttonscreen(self):
        self.clear_screen()
        self.setup_screen()
        button_font = ("Comic Sans MS", 20, "bold")
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth() - window_height
        self.canvas.create_text(window_width / 2, window_height / 10, text="Controller", font=("Comic Sans MS", 80, "bold"), fill="white")

        self.makebutton("Start-Up Dice", button_font, window_width / 2, window_height / 2 - 80, command=self.startupdice)
        self.makebutton("Roll Dice", button_font, window_width / 2, window_height / 2, command=self.startupdice)
        self.makebutton("Balances/Properties", button_font, window_width / 2, window_height / 2 + 80, command=self.startupdice)
        self.makebutton("Start-Up Dice", button_font, window_width / 2, window_height / 2 + 160, command=self.startupdice)

    def startupdice(self):
        self.clear_screen()
        if "startupdice" in self.history:
            self.setup_screen()
            button_font = ("Comic Sans MS", 20, "bold")
            window_height = self.root.winfo_screenheight()
            window_width = self.root.winfo_screenwidth() - window_height
            self.canvas.create_text(window_width / 2, window_height / 10, text="You Already Did This", font=("Comic Sans MS", 20, "bold"), fill="white")
            self.makebutton("Back", button_font, window_width / 2, window_height / 2 + 100, command=self.buttonscreen)
        else:
            self.setup_screen()
            self.history.append("startupdice")
            button_font = ("Comic Sans MS", 20, "bold")
            window_height = self.root.winfo_screenheight()
            window_width = self.root.winfo_screenwidth() - window_height
            players = ["Player", "Bot 1", "Bot 2", "Bot 3"]
            max_roll = 0
            winning_player = None

            while True:
                self.clear_screen()
                self.setup_screen()
                rolls = []
                initial_y = window_height // 2 - 200
                y_increment = 50

                for player in players:
                    roll1 = random.randint(1, 6)
                    roll2 = random.randint(1, 6)
                    total_roll = roll1 + roll2
                    rolls.append((player, roll1, roll2, total_roll))

                for player, roll1, roll2, total_roll in rolls:
                    initial_y += y_increment
                    roll_text = f"{player} rolled: {roll1}, {roll2} | Total: {total_roll}"
                    self.canvas.create_text(window_width / 2, initial_y, text=roll_text, font=("Comic Sans MS", 20), fill="white")
                    self.root.update()
                    time.sleep(2)

                    if total_roll > max_roll:
                        max_roll = total_roll
                        winning_player = player
                    elif total_roll == max_roll:
                        max_roll = 0
                        winning_player = None
                        break

                if winning_player:
                    break

            self.canvas.create_text(window_width / 2, initial_y + y_increment, text=f"{winning_player} wins with {max_roll}!", font=("Comic Sans MS", 20), fill="white")
            self.makebutton("Back", button_font, window_width / 2, window_height / 2 + 160, command=self.buttonscreen)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monopoly Controls")
    app = TkinterLb(root, "data/images/b1.png")
    app.buttonscreen()
    root.mainloop()
