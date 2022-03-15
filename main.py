import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''
options = [rock, paper, scissors]

choice = int(input("What is your choice?  Enter 0 for Rock, 1 for Paper, or 2 for Scissors.  "))
comp_choice = random.randint(0,2)
print("Rock Papper Scissors Shoot!")
print("Your choice:")
print(options[choice])
print("\n Computer chose:")
print(options[comp_choice])
if((choice == 0 and comp_choice == 2) or (choice == 2 and comp_choice == 1) or (choice == 1 and comp_choice == 0)):
    print("\nYou win!")
elif choice == comp_choice:
    print("\nDraw game.")
else:
    print("\nYou lose.")
