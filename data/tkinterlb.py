import tkinter as tk
from PIL import Image, ImageTk
import random, json

class TkinterLb:
    def __init__(self, root, image_path, board_data_path, chance_data_path, chest_data_path):
        self.root = root
        self.image_path = image_path
        self.history = []
        self.playerorder = []
        self.balances = []
        self.properties = []
        with open(board_data_path, encoding="utf8") as file:
            self.board_data = json.load(file)
        with open(chance_data_path, encoding="utf8") as file:
            self.chance_data = json.load(file)
        with open(chest_data_path, encoding="utf8") as file:
            self.chest_data = json.load(file)
        with open("user_info.txt", "r") as file:
            lines = file.readlines()
            self.username = lines[0].strip().split(": ")[1] 
        self.player_data = [
            {"name": self.username, "position": 0},
            {"name": "Bot 1", "position": 0},
            {"name": "Bot 2", "position": 0},
            {"name": "Bot 3", "position": 0}
        ]
        self.balances = [{"name": player["name"], "balance": 1500} for player in self.player_data]

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
        self.makebutton("Roll Dice", button_font, window_width / 2, window_height / 2, command=self.diceroll)
        self.makebutton("Balances/Properties", button_font, window_width / 2, window_height / 2 + 80, command=self.show_balances_properties)

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
            self.canvas.create_text(window_width / 2, window_height / 10, text="Controller", font=("Comic Sans MS", 80, "bold"), fill="white")

            players = [self.username, "Bot 1", "Bot 2", "Bot 3"]

            def roll_dice_for_players(players_list):
                rolls = []
                for player in players_list:
                    roll1 = random.randint(1, 6)
                    roll2 = random.randint(1, 6)
                    total_roll = roll1 + roll2
                    rolls.append((player, total_roll))
                return rolls

            def display_rolls(rolls):
                window_height = self.root.winfo_screenheight()
                window_width = self.root.winfo_screenwidth() - window_height
                initial_y = window_height // 2 - 200
                rolls_sorted = sorted(rolls, key=lambda x: x[1], reverse=True)
                for player, total_roll in rolls_sorted:
                    roll_text = f"{player} rolled: {total_roll}"
                    self.canvas.create_text(window_width / 2, initial_y, text=roll_text, font=("Comic Sans MS", 20), fill="white")
                    initial_y += 50
                self.root.after(2000, lambda: None)
                return [player for player, _ in rolls_sorted]

            rolls = roll_dice_for_players(players)
            sorted_players = display_rolls(rolls)
            self.playerorder = sorted_players

            self.canvas.create_text(window_width / 2, window_height // 2 + 100, text=f"Order: {', '.join(self.playerorder)}", font=("Comic Sans MS", 20), fill="white")
            self.makebutton("Back", button_font, window_width / 2, window_height / 2 + 160, command=self.buttonscreen)

    def diceroll(self):
        if not self.playerorder:
            return

        current_player = self.playerorder.pop(0)  
        self.playerorder.append(current_player)  

        import random
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total_roll = roll1 + roll2

        current_position = 0
        for player_info in self.player_data:
            if player_info['name'] == current_player:
                current_position = player_info['position']
                break

        new_position = (current_position + total_roll) % 40
        for player_info in self.player_data:
            if player_info['name'] == current_player:
                player_info['position'] = new_position
                break

        new_location = None
        for location in self.board_data:
            if location['position'] == new_position:
                new_location = location['name']
                break


        special_action = ""
        if new_location:
            location_info = next((loc for loc in self.board_data if loc['name'] == new_location), None)
            if location_info:
                if location_info['type'] == 'corner':
                    special_action = "Corner action: " + location_info['name']
                elif location_info['type'] == 'community_chest':
                    self.communitychest()
                    return
                elif location_info['type'] == 'chance':
                    self.chance()
                    return
                elif location_info['type'] == 'tax':
                    tax_amount = location_info.get('tax_amount', 0)
                    self.pay_tax(current_player, tax_amount)
                    special_action = f"Pay ${tax_amount} in taxes"

        self.clear_screen()
        self.setup_screen()
        button_font = ("Comic Sans MS", 20, "bold")
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth() - window_height

        self.canvas.create_text(window_width / 2, window_height / 2 - 100, text=f"{current_player} rolled: {roll1} + {roll2} = {total_roll}", font=("Comic Sans MS", 20), fill="white")
        self.canvas.create_text(window_width / 2, window_height / 2, text=f"{current_player}'s new position: {new_location} ({new_position})", font=("Comic Sans MS", 20), fill="white")
        self.canvas.create_text(window_width / 2, window_height / 2 + 100, text=f"Action: {special_action}", font=("Comic Sans MS", 20), fill="white")
        self.makebutton("Back", button_font, window_width / 2, window_height / 2 + 200, command=self.buttonscreen)

    def pay_tax(self, player_name, tax_amount):
        for player in self.balances:
            if player['name'] == player_name:
                player['balance'] -= tax_amount
                break

    def show_balances_properties(self):
        self.clear_screen()
        self.setup_screen()
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth() - window_height
        button_font = ("Comic Sans MS", 20, "bold")

        start_y = window_height / 10
        spacing = 140

        for index, player in enumerate(self.balances):
            if player['name'] in self.playerorder:
                balance = player['balance']
                y_position = start_y + index * spacing
                text = f"{player['name']} | Balance = ${balance}"
                self.canvas.create_text(window_width / 2, y_position, text=text, font=("Comic Sans MS", 20), fill="white")

        self.makebutton("Back", button_font, window_width / 2, window_height / 2 + 260, command=self.buttonscreen)

    def communitychest(self):
        self.clear_screen()
        self.setup_screen()
        
        card = random.choice(self.chest_data)
        
        current_player = self.playerorder[0]
        player_info = next(player for player in self.player_data if player['name'] == current_player)
        
        action_text = f"Card: {card['name']}\nAction: {card['action']}"
        balance_change = 0
        
        if card['action'] == 'collect':
            balance_change = card['amount']
        elif card['action'] == 'pay':
            balance_change = -card['amount']
        elif card['action'] == 'collect and advance':
            balance_change = card['amount']
            player_info['position'] = card['position']
        elif card['action'] == 'advance':
            player_info['position'] = card['position']
        
        player_balance_info = next(balance for balance in self.balances if balance['name'] == current_player)
        player_balance_info['balance'] += balance_change
        
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth() - window_height
        
        self.canvas.create_text(window_width / 2, window_height / 2 - 100, text=action_text, font=("Comic Sans MS", 20), fill="white")
        self.canvas.create_text(window_width / 2, window_height / 2, text=f"Balance Change: ${balance_change}", font=("Comic Sans MS", 20), fill="white")
        self.canvas.create_text(window_width / 2, window_height / 2 + 100, text=f"New Balance: ${player_balance_info['balance']}", font=("Comic Sans MS", 20), fill="white")
        self.makebutton("Back", ("Comic Sans MS", 20, "bold"), window_width / 2, window_height / 2 + 200, command=self.buttonscreen)

    def chance(self):
        self.clear_screen()
        self.setup_screen()
        
        card = random.choice(self.chance_data)
        
        current_player = self.playerorder[0]
        player_info = next(player for player in self.player_data if player['name'] == current_player)
        
        action_text = f"Card: {card['name']}\nAction: {card['action']}"
        balance_change = 0

        if card['action'] == 'collect':
            balance_change = card.get('amount', 0)
        elif card['action'] == 'pay':
            balance_change = -card.get('amount', 0)
        elif card['action'] == 'collect and advance':
            balance_change = card.get('amount', 0)
            player_info['position'] = card.get('position', 0)
        elif card['action'] == 'advance':
            player_info['position'] = card.get('position', 0)
        
        player_balance_info = next(balance for balance in self.balances if balance['name'] == current_player)
        player_balance_info['balance'] += balance_change
        
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth() - window_height
        
        self.canvas.create_text(window_width / 2, window_height / 2 - 100, text=action_text, font=("Comic Sans MS", 20), fill="white")
        self.canvas.create_text(window_width / 2, window_height / 2, text=f"Balance Change: ${balance_change}", font=("Comic Sans MS", 20), fill="white")
        self.canvas.create_text(window_width / 2, window_height / 2 + 100, text=f"New Balance: ${player_balance_info['balance']}", font=("Comic Sans MS", 20), fill="white")
        self.makebutton("Back", ("Comic Sans MS", 20, "bold"), window_width / 2, window_height / 2 + 200, command=self.buttonscreen)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monopoly Controls")
    app = TkinterLb(root, "data/images/b1.png", "data/json/monopolyboard.json", "data/json/chance.json", "data/json/communitychest.json")
    app.buttonscreen()
    root.mainloop()
