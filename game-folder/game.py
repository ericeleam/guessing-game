#Welcome to my game 

#Used for making player objects
from playerClass import *
#All function that are used in game
from gameFunctions import *

print("Welcome to Eric's Guessing Game!")
rules()

#Get the number of players
numPlayers = int(input("How many players are there? "))

players = []

for i in range(numPlayers):
    name = input(f"What is the name of Player {i+1}: ")
    player = Player(name)
    players.append(player)


print("Which mode would you like to play?")
print("Enter 1 for Endless Mode")
print("Enter 2 for Limited Mode")

mode = int(input("Enter your choice: "))
if mode == 1:
    print("You have chosen Endless Mode")
    print("The game will end whenever you quit.")
    separator()
    endlessMode(players)
else:
    print("You have chosen Limited Mode")
    rounds = int(input("How many rounds would you like to play? ")) 
    print("The game will end after", rounds, "rounds.")
    separator()
    limitedMode(players, rounds)


    




