#Password generator
#100 Days of Code

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']   
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))

password_letters = []
password_symbols = []
password_numbers = []

for i in range(1, nr_letters + 1):
    letter = random.choice(letters)
    password_letters.append(letter)
    
for i in range(1, nr_symbols + 1):
    symbol = random.choice(symbols)
    password_symbols.append(symbol)
    
for i in range(1, nr_numbers + 1):
    number = random.choice(numbers)
    password_numbers.append(number)
    
password = password_letters + password_symbols + password_numbers
random.shuffle(password)
random.shuffle(password)
random.shuffle(password)
random.shuffle(password)
random.shuffle(password)
realpassword = ''.join(password)

print(f'Your password is {realpassword}')