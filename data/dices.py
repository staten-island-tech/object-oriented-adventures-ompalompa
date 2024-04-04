import random
import characters
for characters in range(characters):
    number_list = ["1","2","3","4","5","6"]
    random_number = random.choice(number_list)
    random_number2 = random.choice(number_list)
    Dice_rolls = []
    start = True
    if start == True:
        print(f"You have rolled a {random_number}!")
        Dice_rolls.append(random_number)
        print(f"You have rolled a {random_number2}!")
        Dice_rolls.append(random_number2)
    Total = sum(Dice_rolls)
    print(Total)