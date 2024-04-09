import json
from data.Player import Playeroptions

def __init__(self, name, data_path, character=None):
    self.name = name
    self.character = character
    self.balance = 1500 
    self.properties = []
    self.location = 0
    with open(data_path, encoding="utf8") as file:
        self.data = json.load(file)


player = Playeroptions("Player 1", "./monopolyboard.json")
player.roll_dice()