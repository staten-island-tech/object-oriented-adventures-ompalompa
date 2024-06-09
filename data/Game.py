import json
import sys
import random
chances = open("./chance.json", encoding="utf8")
cccard = json.load(chances)
community = open("./communitychest.json", encoding = "utf8")
ttcard = json.load(community)
from Player import data
from Player import Playeroptions
from Player import slowprint
from Player import contestants

class Game:
    def __init__(self,name, data_path, character=None)
        self.name = name
        self.character = character
        self.balance = balance
        self.properties = []
        self.monopolies = []
        self.location = 0
        self.Getoutofjailfree = False
        self.turns = 0
        with open(data_path, encoding="utf8") as file:
            self.data = json.load(file)
    
    def taxing(self,name):
        if self.location in [4,38]:
            if self.location == 4:
                if self.balance > 200:
                    self.balance -= 200
                    slowprint(f"You paid your $200 income tax. You have ${self.balance} remaining")
                elif self.balance <= 200:
                    self.balance -= 200
                    slowprint("You paid your income tax but your about to go broke, better sell something!")
            if self.location == 38:
                if self.balance > 75:
                    self.balance -= 75
                    slowprint(f"You paid you $75 luxury tax, your current balance is ${self.balance}.")
                elif self.balance <= 75:
                    self.balance -= 75
                    slowprint("Your paid your luxury tax, but you are about to go broke, better sell something!")

    def injail(self,name):
        if self.postion == 10:
            if self.turns == 3:
                slowprint("You've been here too long, you gotta pay the $50 fine!")
                if self.balance >= 50:
                    self.balance -= 50
                if self.balance <= 50:
                    self.balance -= 50:
                    slowprint("Thisi will mean bankruptcy, but you gotta pay up!")
            choice = slowprint(input("You are currently in jail, would you like to attempt to roll doubles, pay a $50 fine, or use your Get Out of Jail Free Card assuming you have one? 1 = Roll dye, 2 = Pay $50, 3 = Use Card: "))
            if choice == 1:
                a = random.randint(1,6)
                b = random.randint(1,6)
                if a == b:                        
                    slowprint("Lucky! You escaped jail!")
                    self.location = 10.5
                    self.turns = 0
                elif a != b:
                    stay = slowprint(input("Ha! Bad luck! Would you like to stay in prison and wait for you next turn to roll, or pay the $50 fine to escape?"))
                    if stay == 1:
                        self.turns += 1
                    elif stay == 2:
                        self.balance -= 50
                        slowprint("You've escaped at a cost!")
                        self.turns = 0
            elif choice == 2:
                if self.balance >= 50:
                    self.balance -= 50
                    slowprint("You've escaped at a cost!")
                    self.turns = 0
                elif self.balance < 50:
                    self.balance -= 50
                    slowprint("Escape means bankruptcy, but you gotta pay up!")
                    self.turns = 0
            elif choice == 3:
                if self.Getoutofjailfree == True:
                    self.Getoutofjailfree = False
                    slowprint("See ya!")
                    self.turns = 0
                elif self.Getoutofjailfree == False:
                    choice2 = slowprint(input("You don't have the card, try a different option to escape! 1 = Roll doubles, 2 = Pay up"))
                    if choice == 1:
                        a = random.randint(1,6)
                        b = random.randint(1,6)
                        if a == b:
                            slowprint("Lucky! You escaped jail!")
                            self.location = 10.5
                            self.turns = 0
                        elif a != b:
                            stay = slowprint(input("Ha! Back luck! Would you like to stay in prison and wait for your next turn to roll, or pay the $50 fine to escape?"))
                            if stay == 1:
                                self.turns += 1
                            elif stay == 2:
                                self.balance -= 50
                                slowprint("You've escaped at a cost!")
                                self.turns = 0
                    elif choice == 2:
                        self.balance -= 50
                        slowprint("You've escaped but at a cost!")
                        self.turns = 0

    def rent(self,name):
        for movie in self.data:
            if movie["type"] == "property":
                if movie["name"] == True:


    def monopolies(self,name):
        if 

    def chancecard(self,name,ccard):
        slowprint(f"{self} you got the following chance card ..... {ccard}!")
        if ccard["action"] == "advance":
            if ccard["name"] == "Advance to the nearest Railroad":
                if self.location == 7:
                    self.location = 15
                elif self.location == 22:
                    self.location = 25
                elif self.location == 36:
                    self.location = 5
            elif ccard == "Advance to the neareat Utility":
                if self.location == 2:
                    self.location = 12
                elif self.location == 17:
                    self.location = 20
                elif self.location = 33:
                    self.location = 12
            else: 
                    self.location = position
        elif ccard["action"] == "advance and collect":
            self.location = 1
            self.balance += 200
        elif ccard["action"] == "pay":
            if ccard["name"] == "Make general repairs on all your property"
            elif ccard["name"] == "You have been elected Chairman of the Board":
                if self.balance <= contestants * 50:
                    slowprint("This will mean bankruptcy, but you gotta pay up!")
                self.balance -= contestants * 50
            else:
                if self.balance <= ccard["amount"]:
                    slowprint("You are about to go bankrupt, but still pay up...")
                self.balance -= ccard["amount"]
        elif ccard["action"] == "collect":
            self.balance += ccard["amount"]
            
    def communitychest(self,name,tcard):
        slowprint(f"{self} you received the following community chest ..... {tcard}")
        if tcard["action"] == "collect and advance":
            self.location = tcard["position"]
            self.balance += 200
        elif tcard["action"] == "collect":
            if tcard["name"] == "It is your birthday":
                self.balance += contestants * 10
            else:
                self.balance += tcard["amount"]
        elif tcard["action"] == "pay":
            if tcard["name"] == "You are assessed for street repair":
            else:
                if self.balance <= tcard["amount"]:
                    slowprint("This will mean bankruptcy, but that life...")
                self.balance -= tcard["amount"]
        elif tcard["action"] == "advance":
            if tcard["name"] == "Get out of Jail Free":
                self.Getoutofjailfree = True
            else: 
                self.location = tcard["position"]
        
    def backruptcy(self,name, balance, mode):
        while self.balance <= 0:
            if len(self.properties) > 0:
                survive = input(slowprint("Your current balance is 0 bucks, your broke... But dont worry the game is not over yet, sell a property is stay in it or give up. 1 = Sell your properties, 2 = Give up"))
                if survive == 1:
                    Playeroptions.sell_property
                if survive == 2:
                    slowprint("Your out of the game. GG")
                    contestants.remove(self)
                    slowprint(f"There are currently {len(contestants)} left in teh game, keep it up guys!")
            elif len(self.properties) = 0:
                slowprint("Your current balance is 0, your broke... You have no real estate... GAME OVER")
                contestants.remove(self)
                slowprint(f"There are currently {len(contestants)} left in the game, keep it up guys!")
            
    def victory(self,name,contestants):
        if len(contestants) = 1:
            x = random.choice(contestants)
            slowprint(f"{x} you have officially won this game of Monopoly! Great Game!")
            victory = True
