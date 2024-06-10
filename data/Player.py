# unused 
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

"Meditterranean Avenue" = 0
"Baltic Avenue" = 0
"Reading Railroad" = 0
"Oriental Avenue" = 0
"Vermont Avenue" = 0
"Connecticut Avenue" = 0
"St. Charles Place" = 0
"Electric Company" = 0
"States Avenue" = 0
"Virginia Avenue" = 0
"Pennsylvania Railroad" = 0
"St. James Place" = 0
"Tennessee Avenue" = 0
"New York Avenue" = 0
"Kentucky Avenue" = 0
"Indiana Avenue" = 0
"Illinois Avenue" = 0
"B. & O. Railroad" = 0
"Atlantic Avenue" = 0
"Ventnor Avenue" = 0
"Water Works" = 0
"Marvin Gardens" = 0
"Pacific Avenue" = 0
"North Carolina Avenue" = 0
"Pennysylvania Avenue" = 0
"Short Line Railroad" = 0
"Park Place" = 0
"Boardwalk" = 0
owned = []
morgaged =[]
Houses = 32
Hotels = 4
class Playeroptions:
    def __init__(self, name, data_path, character=None): 
        self.name = name
        self.character = character 
        self.balance = 1500 
        self.properties = []
        self.monopolies = []
        self.railroads = []
        self.utilities = []
        self.utilitiess = []
        self.location = 0
        self.Getoutofjailfree = False
        self.turns = 0
        with open(data_path, encoding="utf8") as file:
            self.data = json.load(file)
          
    def buy_property(self, property):
        for property in self.data:
            if self.location == property["position"]:
                if property not in owned:
                    if self.balance >= property["price"]:
                        self.properties.append(property)
                        owned.append(property) 
                        self.balance -= property["price"]
                        print(f"You bought {property} for ${price}.")
                        if property["position"] in [5,15,25,35]:
                            self.railroads.append.property["name"]
                        if property["position"] in [12,28]:
                            self.utilities.append.property["name"]
                    else:
                        print("You dont have enough money")
                elif property in owned:
                    slowprint("This property is already owned,")
                
    def sell_property(self, property):
        for property in self.data
            if property in self.properties:
                self.properties.remove(property)
                self.balance += property["price"] * 0.5
                print(f"You sold {property} for ${price}.")
            else:
                print("You don't own this.")

    def morgage(self, property):
        for property in self.data:
            slowprint(f"You have morgaged {property["name"]}, you can no longer collect rent from the property.")
            self.balance += property["morgage"]
            slowprint(f"You received {property["morgage"]}, pay this back to the bank with 10% interest to restore your property.")
            morgaged.append(property)

    def paymorgage(self,property)
        if property in self.morgaged:
            for property in self.data:
                self.balance -= property["morgage"] * 1.1
                morgaged.remove(property)
                slowprint(f"{property} has been restored, you can now collect rent from it again!")

    def currentbalance(self, balance):
        slowprint(f"Your current balance is ${self.balance}.")

    def random(self,group):
        w = group
        e = []
        for i in w:
            x = random.choice(w)
            w.remove(x)
            e.append(x)
        slowprint("The following order of players randomly generated will apply throughout the game!")
        return e

    def buyhousehotel(self,property):
        for property in self.data:
            if self.location == property["position"]:
                if property["name"] in self.properties:
                    buyhouse = slowprint(input("Would you like to buy a house on your property? Y/N: "))
                    if upper(buyhouse) == "Y":
                        if property["position"] in range(1,10):
                            if self.balance > 50:
                                self.balance -= 50
                                property["name"] += 1
                                slowprint(f"You bought a house for {property["name"]} it costed you $50, your remaining balance is ${self.balance}.")
                                Houses -= 1
                            elif self.balance <= 50:
                                slowprint("Your too poor!")
                        elif property["position"] in range(11,20):
                            if self.balance > 100:
                                self.balance -= 100
                                property["name"] += 1
                                slowprint(f"You just bought a house for {property["name"]} it costed you $100, your remaining balance is ${self.balance}.")
                                Houses -= 1
                            elif self.balance <= 100:
                                slowprint("Go away brokie")
                        elif property["position"] in range(21,30):
                            if self.balance > 150:
                                self.balance -= 150
                                property["name"] += 1
                                slowprint(f"You just bought a house for {property["name"]} it costed $150, your remaining balance is ${self.balance}.")
                                Houses -= 1
                            elif self.balance <= 150:
                                slowprint("You are too poor...")
                        elif property["position"] in range(31,40):
                            if self.balance > 200:
                                self.balance -= 200
                                property["name"] += 1
                                slowprint(f"You just bought a house for {property["name"]} it costed $200 and your remaining balance is {self.balance}.")
                                Houses -= 1
                            elif self.balance <= 200:
                                slowprint("Insufficent funds...")
                    elif upper(buyhouse) == "N":
                        slowprint("Your loss.")
                    if property["name"] == 4:
                        buyhotel = slowprint(input("Would you like to buy a hotel since you already have 4 houses on the property(the cap is 4)? Y/N"))
                        if upper(buyhotel) == "Y":
                            self.balance -= 150
                            property["name"] = 0
                            self.data.update.property({"hotel": True})
                            slowprint(f"{self.name} bought a hotel for $150!")
                        elif upper(buyhotel) == "N":
                            slowprint("Your loss.")

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

        if self.location in [12,28]:
            for property in self.data:
                if property["position"] in [12,28]:
                    utilities = []
                    utilities.append(property["name"])
                    for player in characters:
                        if property["name"] in player.properties:
                            player.utilitiess.append(property["name"])
                if self.location == property["position"]: 
                    done = False
                    for player in characters:
                        if property["name"] in player.utilitiess:
                            while done = False:
                                if len(player.utilitiess) == 1:
                                    self.balance -= 4 * z
                                    slowprint(f"Since {player} owns only 1 utility, you have to pay 4 times what you just rolled. Your remaining balance is {self.balance}")
                                    done = True
                                elif len(player.utilitiess) == 2:
                                    self.balance -= 10 * z
                                    slowprint(f"Since {player} owns 2 utilities, you have to pay 10 times what you just rolled, you remaining balance is {self.balance}")
                                    done = True