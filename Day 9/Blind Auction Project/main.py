from art import logo

print(logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_info):
    max_bid = 0
    winner = ""
    for person in bidding_info:
        max_bid = max(bidding_info[person], max_bid)

        if bidding_info[person] == max_bid:
            winner = person

    print(f"The winner is {winner} with a bid of ${bidding_info[winner]:.2f}.")

bids = {}
more_bids = True
while more_bids:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        find_highest_bidder(bids)
        more_bids = False
    else:
        print("\n" * 20)