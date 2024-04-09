import random
import time
import json
locations = open("./monopolyboard.json", encoding="utf8")
data = json.load(locations)

class Playeroptions:
    def __init__(self, name, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []

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

    def roll_dice(self, locations):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        z = x + y
        self.location = locations[self.location]['position']
        self.location += z
        new_location = self.location

        print("\nYou rolled...")
        time.sleep(2)
        print(f"First roll: {x}")
        print(f"Second roll: {y}")
        print(f"Your new location is {new_location}")

player = Playeroptions("Player 1")
player.roll_dice(locations)