from art import logo, vs
from game_data import data
import random

# Display the interface for the game
def show_interface(subject_a, subject_b, score):
    """Display game interface with user's current score"""
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {subject_a['name']}, {subject_a['description']} from {subject_a['country']}")

    print(vs)
    print(f"Against B: {subject_b['name']}, {subject_b['description']} from {subject_b['country']}")

# Display failure message
def show_failure(score):
    """Display game failure with user's current score"""
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

# Compare subject followers
def compare_followers(followers):
    """Compare the amount of followers. The followers parameter is a tuple."""
    a_count, b_count = followers # unpack tuple

    if a_count > b_count:
        return 1
    elif a_count < b_count:
        return -1
    else:
        return 0

# Get subject from data pool to compare
def get_subject(game_pool):
    """Select random subject to compare against. Removes from pool so it won't appear again during game."""
    subject_choice = random.randint(0, len(game_pool) - 1)
    return game_pool.pop(subject_choice)

# Play the Higher Lower game with the user
def play_game():
    """Play the game against user's current score."""
    user_score = 0

    # Make a fresh copy for this specific game session
    game_pool = data.copy()
    # Get initial subject A to compare
    subject_a = get_subject(game_pool)

    game_over = False
    while not game_over and len(game_pool) > 0:
        # Get the subject b to compare
        subject_b = get_subject(game_pool)

        print(logo)
        show_interface(subject_a, subject_b, user_score)

        user_choice = input("Who has more followers? Type 'A' or 'B' ").lower()
        print("\n" * 20)

        if user_choice in ('A', 'B', 'a', 'b'):
            result = compare_followers((subject_a["follower_count"], subject_b["follower_count"]))

            if result >= 0:
                user_score += 1
                subject_a = subject_b
            else:
                game_over = True
                show_failure(user_score)
        else:
            game_over = True
            show_failure(user_score)

play_game()