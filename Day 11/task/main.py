from art import logo
import time
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = 21

def add_cards(player_hand):
    score = 0
    for card in player_hand:
        score += card

    return score

def draw_card(player_hand):
    player_hand.append(random.choice(cards))

def display_results(player_hand, opponent_hand):
    print(f"Your final hand: {player_hand}, final score: {add_cards(player_hand)}")
    print(f"Computer's final hand: {opponent_hand}, final score: {add_cards(opponent_hand)}")

    player_score = add_cards(player_hand)
    opponent_score = add_cards(opponent_hand)

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
    while True:
        user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if user_input not in ("y", "yes"):
            break

        display_interface()

        player_cards = []
        computer_cards = []

        # Deal 2 cards to each player
        for i in range(2):
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        hit_or_pass = True
        while hit_or_pass:
            print(f"Your cards: {player_cards}, current score: {add_cards(player_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")

            if add_cards(player_cards) > blackjack:
                display_results(player_cards, computer_cards)
                hit_or_pass = False
            else:
                hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower() in ("y", "yes")

                if hit_or_pass:
                    draw_card(player_cards)
                else:
                    time.sleep(1.0)  # Adds suspense (computer takes time to decide)

                    while add_cards(computer_cards) < 17:
                        draw_card(computer_cards)
                        time.sleep(1.0)  # Adds suspense in terminal

                    display_results(opponent_hand=computer_cards, player_hand=player_cards)


play_blackjack()