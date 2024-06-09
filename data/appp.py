import json
import time
import random
import sys
from Player import slowprint
from Player import Playeroptions
from Player import contestants
from Game import Game

victory = False
slowprint("Welcome to Monopoly! Lets have some Fun!")
characters = []
Add = True
while Addd == True:
    newplayer = slowprint(input("Who's playing?:"))
    characters.append(newplayer)
    contestants += 1
    more = slowprint(input("Would you like to add more players? Y/N: "))
    if more == N:
        Add = False
player = Playeroptions("Player 1","./monopolyboard.json")
order = player.random(characters)
slowprint(f"{order} is the order of player gameplay today, we will be playing from the left to right, so the first person in the list is going first!")
for x in order:
    x = Playeroptions(x,"./monopolyboard.json")
time.sleep(2)
slowprint("The Game will now begin!")
for x in order:
    x = Game(x,"./monopolyboard.json")
while victory = False:
    if len(contestants) == 1:
        Game.victory(contestants)
    o = 0
    for i in order:
        order[o].roll_dice
        o += 1
        
