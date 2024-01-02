import random

word_list = ["ARDVARK", "BABOON", "ANTELOPE", "OSTRICH", 'ELEPHANT', "HIPPOPOTAMUS","GAZELLE", "RHINOCEROS","GREATWHITESHARK","HUMPBACKWHALE", "GIRAFFE","PYTHON","HOUSEFLY","HUMMINGBIRD","DINOSAUR"]
display = []
animal = random.choice(word_list)

for i in range(len(animal)):
    display.append("_")
    
print("\nWelcome to the Animal Hangman Game!")
lives = 3

while lives > 0:
    guess = (input("\nGuess a Letter: ").strip()).upper()
    
    for char in range(len(animal)):
        if guess == animal[char]:
            display[char] = animal[char]
            
    if guess not in animal:
        lives -= 1
        
    print(display)
    
    if '_' not in display:
        print("\nYou Win!!!\n")
        break
    
    print(f"\nRemaining Lives: {lives}")
    
    if lives == 0:
        print("\nYou Lose!\n")
        break   