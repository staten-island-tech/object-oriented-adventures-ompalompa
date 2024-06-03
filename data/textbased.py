import random
import time
import json
import sys
locations = open("./monopolyboard.json", encoding="utf8")
data = json.load(locations)

PlayerCount = []
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

PlayersNumber = int(input("How many players are participating in the game?: "))
while PlayersNumber < 1 or PlayersNumber > 5:
    print("Enter another number please:")
    PlayersNumber = int(input("How many players are participating in the game?: "))

for x in range(PlayersNumber):
    Player = input("Input Player Name: ")
    PlayerCount.append(Player)

for x in PlayerCount:
    while PlayerCount.count(x) > 1:
        PlayerCount.remove(x)
        removing = True
        print("A player has been removed because of a duplicate username.")
while removing == True:
    continuation = input("Would you like to add a different user, continue the game, or restart the game? 1|2|3: ")
    if continuation.upper() == '1':
        for x in PlayerCount:
            Player = input("Input Player Name: ")
            PlayerCount.append(Player)
            print(PlayerCount)
            break
    elif continuation.upper() == '2':
        player = Playeroptions(x, "./monopolyboard.json")
        player.roll_dice(x)
        break
    elif continuation.upper() == '3':
        removing == False
        sys.exit()
    else:
        print("Your answer is invalid, please retry.")
        
        
