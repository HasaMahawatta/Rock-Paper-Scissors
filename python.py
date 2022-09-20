import random


Choices =["Rock","Paper","Scissors"]


While True
Print ("Make your throw")
user_choice =input("  Type Rock, Paper or Scissors: ")
if(user_choice in Choices):
  computer_choice =random.choice(Choices)
  Print(f"\nYou threw '{user_choice}',the computer threw '{computer_choice}'") 


