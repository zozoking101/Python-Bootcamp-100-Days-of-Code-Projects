# Bill Payment

import random
names_input = input("Give me everybodys names:")
names = names_input.split()
num = len(names)
payer = random.randint(0,num -  1)
print(f'{names[payer]} is paying for the meal today')