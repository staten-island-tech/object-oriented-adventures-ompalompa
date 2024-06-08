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
class Playeroptions:
    def __init__(self, name, data_path, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []
        self.location = 0
        self.intro_roll_dice = intro_roll_dice
        with open(data_path, encoding="utf8") as file:
          self.data = json.load(file)
          
    def buy_property(self, property, price):
        if self.balance >= price:
            self.properties.append(property)
            self.balance -= price
            print(f"You bought {property} for ${price}.")
        else:
            print("Not enough money")

    def sell_property(self, property, price):
        if property in self.properties:
            self.properties.remove(property)
            self.balance += price
            print(f"You sold {property} for ${price}.")
        else:
            print("You don't own this.")

    def currentbalance(self, balance)
        return self.balance



    def pay_fine(self):
        if self.balance >= 50:
            self.balance -= 50
            self.in_jail = False
            self.turns_in_jail = 0
            print(f"You paid $50 as fine and have been released.")
        else:
            print("Not enough money.")

    def pay_rent(self, rentprice):
        if self.balance >= rentprice:
            self.balance -= rentprice
            print(f"You paid ${rentprice} for rent")

    def intro_roll_dice(self,characterss):
        e = []
        for x in characterss:
            y = random.randint(1,6)
            z = random.randint(1,6)
            a = y + z
            x.number = a
            e.append(x.number)
        print = (f"{x} rolled a!")
        slowprint(print)
        slowprint(f"Did you roll a {max(e)}, guess what you get to go first! Turn order is in the order of the greatest number rolled to the least!")
        o = sorted(e)

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

    def income_tax(self):
        landed = True
        while landed == True:
            print("Do you want to pay a fine of $200, or pay 10% of your total networth?")
            choices = int(input("Choices: 1 ($200), or 2 (10%): "))
            if choices == '1':
                self.balance - 200
                print(f"Your current balance is ${self.balance}")
            if choices == '2':
                self.balance = (self.balance)*0.9
                print(f"Your current balance is ${self.balance}")
    def bankruptcy(self, balance, mode):
        self.networth = self.balance + self.property
        while self.balance <= 0:
            if property + self.balance >= 0:
                print(f"Your current balance is {balance}. You must sell a portion of your property to remain in the game.")
            elif property + self.balance <= 0:
                print(f"Your  balance is {balance}. Selling all your property will only get you to a balance of {self.networth}. You are eliminated from the game.")
                if self.mode == 'multiplayer':
                    

slowprint("Welcome to Monopoly! Lets have some Fun!")
characters = []
Add = True
while Add == True:
    slowprint("Who's playing?")
    newplayer = input(":")
    characters.append(newplayer)
    slowprint("Would you like to add more players? Y/N")
    more = input(":")
    if more == N:
        Add = False
player = Playeroptions("Player 1","./monopolyboard.json")
player.intro_roll_dice