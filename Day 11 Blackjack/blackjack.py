import random


# Function to deal a card from the deck
def deal_card():
    """return a random card from cards in the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Function to calculate the score of a hand in Blackjack
def calculate_score(cards):
    """Calculate the score of a hand in Blackjack."""
    # Check for blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Adjust for Ace (11 to 1) if total score exceeds 21
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Main game loop to keep the game running
while True:
    # Initialization of cards and scores
    user_card = []
    computer_card = []
    user_hands = calculate_score(user_card)
    computer_hands = calculate_score(computer_card)
    is_game_over = False

    # Deal the initial two cards to the player and the computer
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    # Player's turn
    while not is_game_over:
        user_hands = calculate_score(user_card)
        computer_hands = calculate_score(computer_card)

        # Display player's cards and score, and computer's first card
        print(f" Your cards: {user_card}, current score: {user_hands}")
        print(f" Computer's first card: {computer_card[0]}")

        # Check for instant win or bust
        if user_hands == 0 or computer_hands == 0 or user_hands > 21:
            is_game_over = True
        else:
            # Ask player to hit or stay
            hit_stay = input("Type 'y' to get another card, type 'n' to stay: ").lower()
            if hit_stay == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn: Keep drawing cards until score reaches 17 or more, or gets a Blackjack
    while computer_hands != 0 and computer_hands < 17:
        computer_card.append(deal_card())
        computer_hands = calculate_score(computer_card)

    # Determine and display the game outcome
    print(f"\nComputer's final hand: {computer_card}, final score: {computer_hands}")
    if computer_hands == 0:
        print("Computer has Blackjack! You lose 😭")
    elif user_hands > 21:
        print("You went over. You lose 😭")
    elif computer_hands > 21:
        print("Computer went over. You win 😄")
    elif user_hands > computer_hands:
        print("You win 😄")
    elif user_hands < computer_hands:
        print("You lose 😭")
    else:
        print("It's a draw 🙃")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? Type 'y' for yes and 'n' for no: ").lower()
    if play_again != 'y':
        break
