#Blackjack Project
import random
import os

ascii_art = 
 
.------.              _     _            _    _            _    
|A_  _ |             | |   | |          | |  (_)          | |   
|( \/ ).-----.       | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |       | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |       | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |       |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                              _/ |                
      `------'                             |__/    



def deal_card():
    # 
    # Returns a random card from the deck

    # Returns:
    #     int: card number
    # 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Take a list of cards and return the score calculated from the cards

    # Args:
    #     cards (int): card value

    # Returns:
    #     int: sum of cards
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    score = sum(cards)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return("Draw")
    elif computer_score == 0:
        return("Lose, opponent has a Blackjack")
    elif user_score == 0:
        return("Win with a Blackjack")
    elif user_score > 21:
        return("You went over. You lose")
    elif computer_score > 21:
        return("Opponent went over. You win!")
    elif user_score > computer_score:
        return("You win!")
    elif user_score < computer_score:
        return("You lose")    

def play_game():
    os.system('cls')    
    print(f"\n{ascii_art}\n")
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Comuter's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card()) 
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to (re)play the Blackjack game? Type 'y' or 'n':") == 'y':
    play_game()
    
play_game()
