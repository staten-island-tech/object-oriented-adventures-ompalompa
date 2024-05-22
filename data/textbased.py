import random
import time
import json
locations = open("./monopolyboard.json", encoding="utf8")
data = json.load(locations)

PlayerCount = []
Player = input("What is the name of the first player?")
PlayerCount.append(Player)
AddAnother = input("Do you want to add another player?")
while AddAnother.upper == 'Yes':
    Player = input("What is the name of the next player?")
    PlayerCount.append(Player)
    AddAnother = input("Do you want to add another player?")
if AddAnother.upper == 'No':
    print()

class Playeroptions:
    def __init__(self, name, data_path, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []
        self.location = 0
        with open(data_path, encoding="utf8") as file:
          self.data = json.load(file)

def roll_dice(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        z = x + y
        self.location += z

        new_location = None
        for location in self.data:
            if self.location == location['position']:
                new_location = location['name']
                break

        print("\nYou rolled...")
        time.sleep(2)
        print(f"First roll: {x}")
        print(f"Second roll: {y}")
        print(f"Your new location is {new_location}")    

player = Playeroptions("Player 1", "./monopolyboard.json")
player.roll_dice()      