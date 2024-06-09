import random
import time
import json
locations = open("./monopolyboard.json", encoding="utf8")
data = json.load(locations)
import sys
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush() 
		time.sleep(1./10)
contestants = 0

"Meditterranean Avenue" = False
"Baltic Avenue" = False
"Reading Railroad" = False
"Oriental Avenue" = False
"Vermont Avenue" = False
"Connecticut Avenue" = False
"St. Charles Place" = False
"Electric Company" = False
"States Avenue" = False
"Virginia Avenue" = False
"Pennsylvania Railroad" = False
"St. James Place" = False
"Tennessee Avenue" = False
"New York Avenue" = False
"Kentucky Avenue" = False
"Indiana Avenue" = False
"Illinois Avenue" = False
"B. & O. Railroad" = False
"Atlantic Avenue" = False
"Ventnor Avenue" = False
"Water Works" = False
"Marvin Gardens" = False
"Pacific Avenue" = False
"North Carolina Avenue" = False
"Pennysylvania Avenue" = False
"Short Line Railroad" = False
"Park Place" = False
"Boardwalk" = False

class Playeroptions:
    def __init__(self, name, data_path, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []
        self.monopolies = []
        self.location = 0
        self.Getoutofjailfree = False
        self.intro_roll_dice = intro_roll_dice
        self.turns = 0
        with open(data_path, encoding="utf8") as file:
          self.data = json.load(file)
          
    def buy_property(self, property):
        if self.location = property["position"]:
            if self.balance >= property["price"]:
                self.properties.append(property)
                self.balance -= property["price"]
                print(f"You bought {property} for ${price}.")
            else:
                print("You dont have enough money")

    def sell_property(self, property):
        if property in self.properties:
            self.properties.remove(property)
            self.balance += price
            print(f"You sold {property} for ${price}.")
        else:
            print("You don't own this.")

    def morgage(self, property):
        slowprint(f"You have morgaged {property["name"]}, you can no longer collect rent from the property.")
        self.balance += property["morgage"]
        slowprint(f"You received {property["morgage"]}, pay this back to the bank with 10% interest to restore your property.")
        property["name"] = "morgage"

    def paymorgage(self,property)
        self.balance -= property["morgage"] * 1.1
        property["name"] = True
        slowprint("This property has been restored, you can now collect rent from it again!")

    def currentbalance(self, balance):
        return self.balance

    def random(self,group):
        e = []
        for i in group:
            x = random.choice(group)
            group.remove(x)
            e.append(x)
            slowprint("The following order of players randomly generated will apply throughout the game!")
        return e

    """def intro_roll_dice(self,characterss):
        e = []
        for x in characterss:
            y = random.randint(1,6)
            z = random.randint(1,6)
            a = y + z
            x.number = a
            e.append(x.number)
            time.sleep(1)
            print = (f"{x} rolled a!")
            slowprint(print)
            self.intro_roll_dice = a
        slowprint(f"Did you roll a {max(e)}, guess what you get to go first! Turn order is in the order of the greatest number rolled to the least!")
        o = sorted(e)
        p = []
        for i in o:
            p.append"""


    def roll_dice(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        z = x + y
        self.location += z
        if self.location > 37:
            q = 0
            while self.location > 37:
                self.location -= 1
                q += 1
            self.location = q - 1

        new_location = None
        for location in self.data:
            if self.location == location['position']:
                new_location = location['name']
                break

        slowprint("\nYou rolled...")
        time.sleep(2)
        slowprint(f"First roll: {x}")
        slowprint(f"Second roll: {y}")
        slowprint(f"Your new location is {new_location}")

slowprint("Welcome to Monopoly! Lets have some Fun!")
characters = []
Add = True
while Add == True:
    slowprint("Who's playing?")
    newplayer = input(":")
    characters.append(newplayer)
    more = slowprint(input("Would you like to add more players? Y/N: "))
    if more == N:
        Add = False
w = contestants
player = Playeroptions("Player 1","./monopolyboard.json")
player.random(w)
time.sleep(2)
slowprint("The Game will now begin")
c = 0 
for x in contestants:
    c += 1
    ran = 
    o[c]

