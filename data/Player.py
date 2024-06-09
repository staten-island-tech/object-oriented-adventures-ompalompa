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

""""Meditterranean Avenue" = False
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
"Boardwalk" = False"""
owned = []
class Playeroptions:
    def __init__(self, name, data_path, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []
        self.monopolies = []
        self.location = 0
        self.Getoutofjailfree = False
        self.turns = 0
        with open(data_path, encoding="utf8") as file:
            self.data = json.load(file)
          
    def buy_property(self, property):
        if self.location == property["position"]:
            if property not in owned:
                if self.balance >= property["price"]:
                    self.properties.append(property)
                    owned.append(property) 
                    self.balance -= property["price"]
                    print(f"You bought {property} for ${price}.")
                else:
                    print("You dont have enough money")
            elif property in owned:
                slowprint("This property is already owned,")

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


    def roll_dice(self,name):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        z = x + y
        self.location += z
        if self.location > 37:
            if self.location = 38:
                self.balance += 200
                slowprint(f"For reaching GO you received $200, your current balance is ${self.balance}.")
            if self.location > 38:
                self.balance += 200
                slowprint(f'For passing GO you received $200, your current balance is ${self.balance}.')
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
        slowprint(f"{self.name}location is {new_location}.")