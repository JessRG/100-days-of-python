from art import logo
import random

MIN_NUMBER = 1
MAX_NUMBER = 100
difficulty_map = {
    "easy": 10,
    "hard": 5,
}

def select_number():
    """Select a random number between 1 and 100."""
    return random.randint(MIN_NUMBER,MAX_NUMBER)

def show_intro():
    """Display the header of the program."""
    print(f"{logo}\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")

def compare(guess, target):
    """Compare the guess against the target."""
    if guess < target:
        return -1
    elif guess > target:
        return 1
    else:
        return 0

def guess_the_number():
    answer = select_number()

    show_intro()
    chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    n_attempts = difficulty_map.get(chosen_difficulty, difficulty_map["hard"])

    for i in range(n_attempts, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if i == 1 and compare(user_guess, answer) != 0:
            print("You have run out of guesses. Good luck next time!")
        elif compare(user_guess, answer) < 0:
            print("Too low.\nGuess again.")
        elif compare(user_guess, answer) > 0:
            print("Too high.\nGuess again.")
        else:
            print(f"You got it! The answer was {answer}")
            break

    print("Run the program to play again.")

guess_the_number()