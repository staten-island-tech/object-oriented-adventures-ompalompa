import random
<<<<<<< HEAD
User_Data = []
x = int(input("How many players are playing? "))
for x in range(x):
    username = input("What is the name of this player? ")
    number_list = ["1","2","3","4","5","6"]
    random_number = int(random.choice(number_list))
    random_number2 = int(random.choice(number_list))
=======
import characters
for characters in range(characters):
    random_number = random.randint(1,6)
    random_number2 = random.choice(1,6)
>>>>>>> ca7e552cf87acafce70be966fe19e603d636f635
    Dice_rolls = []
    start = True
    if start == True:
        print(f"You have rolled a {random_number}!")
        Dice_rolls.append(random_number)
        print(f"You have rolled a {random_number2}!")
        Dice_rolls.append(random_number2)
<<<<<<< HEAD
        TotalDice = sum(Dice_rolls)
        player = {
        'username': str(username),
        'dices': TotalDice,
        }
        User_Data.append(player)
    
for player in User_Data:
    print("Username: ", player['username'])
    print("Dice Total: ", player['dices'])
=======
    Total = sum(Dice_rolls)
    print(Total)

>>>>>>> ca7e552cf87acafce70be966fe19e603d636f635
