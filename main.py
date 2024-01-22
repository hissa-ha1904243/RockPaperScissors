import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def picture(ans):
    if ans == 0:
        print(rock)
    elif ans == 1:
        print(paper)
    elif ans == 2:
        print(scissors)
    else:
        print("invalid choice!")


def result(user_choice, computer_choice):
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")




choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
picture(choice)
print("Computer Choice:")
random_number = random.randint(0, 2)
picture(random_number)
result(choice, random_number)
