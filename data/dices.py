import random
import characters
for characters in range(characters):
    random_number = random.randint(1,6)
    random_number2 = random.choice(1,6)
    Dice_rolls = []
    start = True
    if start == True:
        print(f"You have rolled a {random_number}!")
        Dice_rolls.append(random_number)
        print(f"You have rolled a {random_number2}!")
        Dice_rolls.append(random_number2)
    Total = sum(Dice_rolls)
    print(Total)

