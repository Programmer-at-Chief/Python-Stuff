import random as rand
import os

def start():
    print("*"*50)
    print("Welcome to Hangman !!")
    print("\nEnter a sentence , then guess a word . \nYou get 7 lives")
    print("*"*50)


hangmanpics = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""", 
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", 
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", 
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", 
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", 
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

os.system('clear')
start()

lives=6
print()
array1=input("Enter a sentence : ").split(" ")
points=0
while lives >=0:
    user_input=input("Enter a word (q to quit): ")
    if (user_input=="q"):
        print("\nThanks for playing")
        print(f"You still had {lives} lives left. ")
        print(f"Congratulations , You scored {points} points.")
        exit()
    rand_word=rand.choice(array1)
    if (user_input==rand_word):
        print("\nYou guessed it right. \n")
        points+=1
    else:
        os.system('clear')
        start()
        print("\nWrong Word !! \n")
        print(hangmanpics[7-lives-1])
        lives-=1
        
else:
    print("You died !!\n")
    print(f"Congratulations , You scored {points} points.")
