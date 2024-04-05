
class Player:
    def __init__(self, name, character=None):
        self.name = name
        self.character = character
        self.balance = 1500 
        self.properties = []

    def select_character(self, available_characters):
        print("\nCharacters:")
        print("Top Hat")
        print("Battleship")
        print("Scottie Dog")
        print("Thimble")
        print("Boot")
        print("Wheelbarrow")
        print("Cat")
        print("Racecar")
        print("Iron")
        print("Penguin")
        print("T-Rex")
        print("Rubber Ducky")

        while True:
            selected_character = input("Select your character: ").strip().lower()
            if selected_character in available_characters:
                self.character = selected_character
                print(f"You've selected {selected_character.capitalize()}.")
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

    def pay_tax(self, tax):
        self.balance -= tax
        print(f"You paid ${tax} in taxes.")

    def get_paid(self, paycheck):
        self.balance += paycheck
        print(f"You received ${paycheck}.")

    def pay_fine(self):
        if self.balance >= 50:
            self.balance -= 50
            self.in_jail = False
            self.turns_in_jail = 0
            print(f"You paid ${50} as fine and have been released.")
        else:
            print("Not enough money.")
    
    

