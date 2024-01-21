# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")
    
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# local Scope

# def drink_potion():
#     potion_strength = 2
#     print(f"Potion Strength: {potion_strength}")
    
# drink_potion()
# print(f"Potion Strength: {potion_strength}")

# Global Scope

# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(f"Potion Strength: {player_health}")
    
#     drink_potion()
# game()
# print(player_health)
    
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]

#     if game_level < 5:
#         new_enemy = enemies[0]
        
#     print(new_enemy)

# Modifying Global Scope
# enemies = 1

# def increase_enemies():
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1
    
# enemies = increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "http://www.google.com"
TWITTER_HANDLE = "@zozoking_101"