from art import logo
import time
import random

blackjack = 21

def calculate_score(player_hand):
    if 11 in player_hand and sum(player_hand) > blackjack:
        player_hand.remove(11)
        player_hand.append(1)

    return sum(player_hand)

def draw_card(player_hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand.append(random.choice(cards))

def display_results(player_hand, opponent_hand):
    player_score = calculate_score(player_hand)
    opponent_score = calculate_score(opponent_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {opponent_hand}, final score: {opponent_score}")

    if player_score > blackjack:
        print("You went over. You lose 😭")
    elif opponent_score > blackjack:
        print("Opponent went over. You win 😁")
    elif player_score == opponent_score:
        if player_score == blackjack:
            print("Push! Both have Blackjack 🙃😎")
        else:
            print("Draw 🙃")
    elif opponent_score == blackjack:
        print("Lose, Opponent has Blackjack 😱")
    elif player_score == blackjack:
        print("Win with a Blackjack 😎")
    elif player_score > opponent_score:
        print("You win 😃")
    else:
        print("You lose 😤")

def display_interface():
    print("\n" * 20)
    print(logo)

def play_blackjack():
    player_cards = []
    computer_cards = []

    # Deal 2 cards to each player
    for i in range(2):
        draw_card(player_cards)
        draw_card(computer_cards)

    hit = True
    while hit:
        player_score = calculate_score(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score > blackjack:
            display_results(player_cards, computer_cards)
            hit = False
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower() in ("y", "yes")

            if hit:
                draw_card(player_cards)

    opponent_score = calculate_score(computer_cards)
    while opponent_score != blackjack and opponent_score < 17:
        time.sleep(1.0)  # Adds suspense in terminal
        draw_card(computer_cards)
        opponent_score = calculate_score(computer_cards)

    display_results(opponent_hand=computer_cards, player_hand=player_cards)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() in ("y", "yes"):
    display_interface()
    play_blackjack()