import os
from art import logo


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_bid():
    """Gets a bid from the user and returns the name and bid amount."""
    name = input("What is your name?: ")
    while True:
        try:
            price = float(input("What is your bid?: $"))
            return name, price
        except ValueError:
            print("Please enter a valid number.")


def ask_continue_bidding():
    """Asks the user if they want to continue bidding and returns a boolean value."""
    return input("Are there any other bidders? Type 'yes' or 'no': ").lower() == 'yes'


def find_highest_bidder(bidding_record):
    """Finds and returns the highest bidder's name and bid amount."""
    winner = max(bidding_record, key=bidding_record.get)
    highest_bid = bidding_record[winner]
    return winner, highest_bid


def main():
    """Main function to handle the bidding application."""
    bids = {}
    while True:
        name, price = get_bid()
        bids[name] = price

        if not ask_continue_bidding():
            break

        clear_screen()

    winner, highest_bid = find_highest_bidder(bids)
    print(f"The winner is {winner} with the bid of ${highest_bid:.2f}")


if __name__ == "__main__":
    # ASCII art or logo would be printed here. For simplicity, I'm skipping it.
    print(logo)

    main()
