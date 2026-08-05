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

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. You lose!")
else:
    user_choice = game_images[user_input]
    computer_choice = game_images[random.randint(0, 2)]

    if user_input == computer_choice:
        status = "It's a draw"
    else:
        if user_input == rock and computer_choice == paper:
            status = "You lose"
        elif user_input == paper and computer_choice == scissors:
            status = "You lose"
        elif user_input == scissors and computer_choice == rock:
            status = "You lose"
        else:
            status = "You win"

    print(f"{user_input}\nComputer chose:\n{computer_choice}\n{status}")