# # Describe the problem

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
            
# my_function()

# # Reproduce the bug
# from random import randint

# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0,len(dice_imgs)-1)
# print(dice_imgs[dice_num])

# # Play the computer

# year = int()
# year = int(input("Whats your year of bith? "))
# if year > 1980 and year < 1984:
#     print("You're a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")


# # Fix the errors
# age = int(input("How old are you? "))
# if age >= 18:
#     print(f"You can drive at age {age}.")

# Print is your friend

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of wors per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use the Debugger

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
    
# mutate([1,2,3,4,5,8,13])

# Debug odd or even

# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")
    
# year = int(input("Which year do you want to check? : "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap.")
#         else:
#             print("Not divisible by 400. Not Leap.")
#     else:
#         print("Not divisible by 100. Not Leap.")
# else:
#     print("Not divisible by 4. Not Leap.")

# Higher Lower Game

# Display art