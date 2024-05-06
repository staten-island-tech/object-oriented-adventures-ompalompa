import random
import time
import json
locations = open("./monopolyboard.json", encoding="utf8")
data = json.load(locations)

class Playeroptions:
    def __init__(self, name, data_path, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []
        self.location = 0
        with open(data_path, encoding="utf8") as file:
          self.data = json.load(file)

    def select_character(self, available_characters):
        print("\nCharacters:")
        for character in available_characters:
            print(character.capitalize())

        while True:
            selected_character = input("Select your character: ").strip().capitalize()
            if selected_character in available_characters:
                self.character = selected_character
                print(f"You've selected {selected_character}.")
                break
            else:
                print("Invalid character. Select from the available characters.")

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

<<<<<<< HEAD
    def speed_dice(self, dye):
        continuee = True
        valuee = 1
        d = []
        while continuee == True:
            if dye == 1:
                continuee = False
            d.append(valuee)
            valuee = valuee + 1
            dye = dye - 1
        z = 0
        zz = []
        for x in d:
            x = random.randint(1,6)
            z = x
            zz.append(z)
        print(f"You rolled these numbers {zz}!")
        l = 0
        for w in zz:
            l = l + w
        print(l)
=======
    def income_tax(self):
        landed = False
        print("Do you want to pay a fine of $200, or pay 10% of your total networth?")
        choices = int(input("Choices: 1 ($200), or 2 (10%): "))
        if choices == '1':
            self.balance - 200
        if choices == '2':
            self.balance = (self.balance)*0.9
>>>>>>> Characters


player = Playeroptions("Player 1", "./monopolyboard.json")
player.roll_dice()
