import os
from art import logo

print(logo)


# Clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")


bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == 'yes':
        clear()

find_highest_bidder(bids)