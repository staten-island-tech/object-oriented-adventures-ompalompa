import random
import time
import json
locations = open("./monopolyboard.json", encoding="utf8")
data = json.load(locations)

PlayerCount = []

PlayersNumber = int(input("How many players are participating in the game?: "))

for x in range(PlayersNumber):
    Player = int(input("Input Player Name: "))
    PlayerCount.append(Player)
print(f"The Current Players Are: {PlayerCount}")

for x in PlayerCount:
    x = []

GoFirst = []
class Playeroptions:
    def __init__(self, name, data_path, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []
        self.location = 0
        with open(data_path, encoding="utf8") as file:
          self.data = json.load(file)

    def roll_dice(self, player):
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
            print(f"{player}'s new location is {new_location}")

    def go_first(self, player):
        for x in int(range(PlayerCount)):
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            z = x + y

            print("\nYou rolled...")
            time.sleep(2)
            print(f"First roll: {x}")
            print(f"Second roll: {y}")
            print(f"{player}'s new location is {z}")
            GoFirst.append(z)
            largest = max(GoFirst)
            print(largest)

for x in PlayerCount:
    player = Playeroptions(x, "./monopolyboard.json")
    player.roll_dice(x)
    player.go_first(player)