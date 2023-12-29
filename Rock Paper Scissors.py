import random
pl1 = 0
compscore = 0

while pl1 <= 3 or compscore <= 3:
    player_play = int(input("\nPlay 1 for Rock, 2 for Paper and 3 for Scissors: "))
    comp_play = random.randint(1, 3)
    choice = ['ROCK', 'PAPER', 'SCISSORS']

    play = [player_play, comp_play]
    if play in [[1,3],[2,1],[3,2]]:
        #player winning conditions
        pl1 += 1
        print("\n\t\b\bYou : Computer")
        print(f"\t\b\b\b{choice[player_play - 1]} - {choice[comp_play - 1]}")
        print(f"\t{pl1} - {compscore}")
    elif play in [[3,1],[1,2],[2,3]]:
        #computer winning conditions
        compscore += 1
        print("\n\t\b\bYou : Computer")
        print(f"\t\b\b\b{choice[player_play - 1]} - {choice[comp_play - 1]}")
        print(f"\t{pl1} - {compscore}")
    elif play in [[1,1],[2,2],[3,3]]:
        #Draw conditions
        print("\n\t\b\bYou : Computer")
        print(f"\t\b\b\b{choice[player_play - 1]} - {choice[comp_play - 1]}")
        print(f"\t{pl1} - {compscore}")
    else:
        print('\nEnter valid number!')
    if pl1 == 3:
        print("\nYou Win!")
        break
    elif compscore == 3:
        print("\nThe Computer Wins!")
        break