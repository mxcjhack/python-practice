import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input("Enter ... \n1 for rock, \n2 for paper, \n3 for scissors:\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2 or 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("Your choice = " + str(RPS(player)).replace('RPS.' , '') + ".")
print("Computer choice = " + str(RPS(computer)).replace('RPS.' , '') + ".")
print("")

if player == 1 and computer == 3:
    print("🥳🥳You win")
elif player == 2 and computer == 1:
    print("🥳🥳You win")
elif player == 3  and computer == 2:
    print("🥳🥳You win")
elif player == computer:
    print("😑😑Draw")
else:
    print("🐍🐍Python wins!!")

