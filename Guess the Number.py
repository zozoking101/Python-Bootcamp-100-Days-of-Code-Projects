# Guess the Number Game
import random

# function to set difficulty
def set_difficulty(difficulty):
    if difficulty.lower() == 'easy':
        attempts = 10
    elif difficulty.lower() == 'hard':
        attempts = 5
    return attempts

ascii_art = "'""
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP" 
"'"

# Choose Random Number between 1 and 100
number = random.randint(1, 100)

game_running = True

# Start Game
while game_running:
    print(f"\n{ascii_art}\n")
    print("Welcome to the Guess The Number Game!")
    choose_difficulty = input("Choose the difficulty of the game, easy or hard: ")
    no_of_attempts = set_difficulty(choose_difficulty)
    print(f"You have {no_of_attempts} attempts")
    
    # Repeat until game over or won
    while no_of_attempts > 0 and game_running:
        # User Guess
        choice = int(input("Choose a number between 1 and 100: "))
        
        # Check User Guess against Random Number
        if choice > number:
            no_of_attempts -= 1
            print(f"Too High! {no_of_attempts} attempts left.")
            
        elif choice < number:
            no_of_attempts -= 1
            print(f"Too Low! {no_of_attempts} attempts left.")
        else:
            print("Correct Guess. You Win!")
            game_running = False
            game_won = True
    if not game_won:
        print(f"The Correct Guess Was {number}.\n You Lose!")
        game_running = False