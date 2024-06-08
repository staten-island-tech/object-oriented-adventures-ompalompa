import json
import sys
import Player
from Player import Playeroptions
from Player import slowprint
from Player import contestants

class Game:
    def backruptcy(self, balance, mode):
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
print("o)")