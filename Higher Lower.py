art_1 = """
 _   _  _         _                 
| | | |(_)       | |                
| |_| | _   __ _ | |__    ___  _ __ 
|  _  || | / _` || '_ \  / _ \| '__|
| | | || || (_| || | | ||  __/| |   
\_| |_/|_| \__, ||_| |_| \___||_|   
            __/ |                   
           |___/                    
 _                                  
| |                                 
| |      ___  __      __  ___  _ __ 
| |     / _ \ \ \ /\ / / / _ \| '__|
| |____| (_) | \ V  V / |  __/| |   
\_____/ \___/   \_/\_/   \___||_|   
                                    
    
"""
art_2 = """
 _   _         
| | | |        
| | | | ___    
| | | |/ __|   
\ \_/ /\__ \ _ 
 \___/ |___/(_)
               
"""

from random import randint
from os import system

def vowel_check(x):
    if x['description'][0].lower() in "aeiou":
        occupation_vowel = True
        return (occupation_vowel)


def compare_with(a, b):
    if vowel_check(a):
        article_1 = "an"
    else:
        article_1 = "a"
    if vowel_check(b):
        article_2 = "an"
    else:
        article_2 = "a"
    
    #Data in printable format
    print(f"Compare A: {a['name']}, {article_1} {a['description']} from {a['country']}.")
    print(art_2)
    print(f"Against B: {b['name']}, {article_2} {b['description']} from {b['country']}.\n")
    
    # Ask user to guess who has more followers
    followers = input("Who has more followers on Instagram? 'A' or 'B': ").strip().upper()
    
    # Checks if user is correct and returns feedback
    if followers == 'A':
        return a['follower_count'] > b['follower_count']
    elif followers == 'B':
        return b['follower_count'] > a['follower_count']
    else:
        return False

# game data.py
data = [
    {
        'name': 'Instagram',
        'follower_count': 665_000_000_000,
        'description': 'Social media platform',
        'country': 'The United States',
    },  
    {
        'name': 'Cristiano Ronaldo',
        'follower_count':  616_000_000_000,
        'description': 'Footballer',
        'country': 'Portugal',
    },
    
    {
        'name': 'Ariana Grande',
        'follower_count':  380_000_000,
        'description': 'Musician and Actress',
        'country': 'The United States',
    },
    {
        'name': 'Dwanye Johnson',
        'follower_count':  395_000_000,
        'description': 'Actor and proffesional wrestler',
        'country': 'The United States',
    },
    
    {
        'name': 'Davido',
        'follower_count':  28_500_000,
        'description': 'Musician',
        'country': 'Nigeria',
    },
    {
        'name': 'Beyonce',
        'follower_count':  319_000_000,
        'description': 'Musician and goddess',
        'country': 'The United States',
    },
    {
        'name': 'Wizkid',
        'follower_count':  18_200_200,
        'description': 'Singer',
        'country': 'Nigeria',
    },
    {
        'name': 'Burna Boy',
        'follower_count':  16_200_000,
        'description': 'Nigerian Artist',
        'country': 'Nigeria',
    },
    {
        'name': 'Leonel Messi',
        'follower_count':  496_000_000,
        'description': 'THE GOAT',
        'country': 'Argentina',
    },
    {
        'name': 'Selena Gomez',
        'follower_count':  429_000_000,
        'description': 'Musician',
        'country': 'The United States',
    },
    {
        'name': 'Nicki Minaj',
        'follower_count':  228_000_000,
        'description': 'Musician',
        'country': 'The United States',
    },
    {
        'name': 'Zendaya',
        'follower_count':  184_000_000,
        'description': 'Actress',
        'country': 'The United States',
    },
    {
        'name': 'Drake',
        'follower_count':  144_000_000,
        'description': 'Artist',
        'country': 'Canada',
    },
    {
        'name': 'Billie Eilish',
        'follower_count':  110_000_000,
        'description': 'Artist',
        'country': 'The United States',
    },
    {
        'name': 'Dua Lipa',
        'follower_count':  88_500_000,
        'description': 'Artist',
        'country': 'The United States',
    },
    {
        'name': 'Justin Beiber',
        'follower_count':  292_000_000,
        'description': 'Artist',
        'country': 'Canada',
    },
    {
        'name': 'Donald Trump',
        'follower_count':  23_600_000,
        'description': '45th President of the United States',
        'country': 'The United States',
    },
    {
        'name': 'Mark Zuckerberg',
        'follower_count':  12_900_000,
        'description': 'Founder of Meta',
        'country': 'The United States',
    },
    {
        'name': 'Doja Cat',
        'follower_count':  24_700_000,
        'description': 'Musician',
        'country': 'The United States',
    },
    {
        'name': 'Bill Gates',
        'follower_count':  8_800_000,
        'description': 'Founder of Microsoft',
        'country': 'The United States',
    },
    {
        'name': 'Barack Obama',
        'follower_count':  36_500_000,
        'description': 'Former President of the United States',
        'country': 'The United States',
    },
]



# game repeatability
def game():
    
    game_running = True
    score = 0
    round = 1
    print(f"Welcome to the Higher Lower Game! \n{art_1}")
    
    while game_running:
        
        r = randint(0, len(data) - 1)
        if round == 1:
            A = data.pop(r)
        else:
            A = C
        s = randint(0, len(data) - 2)
        B = data[s]
        C = B
        data.append(A)
        advance = compare_with(A, B)
        system('cls')
        print(art_1)
        if advance:
            game_running = True
            # Score keeping
            score += 1
            round += 1
            
            print(f"\nCorrect!\n {A['name']}: {A['follower_count']} Vs. {B['name']}: {B['follower_count']} \n\n\t\t\tSCORE: {score}\n\n")
        else:
            game_running = False
            print(f"\nThat's wrong.\n\n {A['name']}: {A['follower_count']} Vs. {B['name']}: {B['follower_count']} \n\n\t\t\tFinal score: {score}\n")
        
        replay = input("Replay the game? (y,n): ")
        
    print("\n")

    if replay.lower() == 'y':
        game()
    else:
        pass


game()
    