# numbers = [1, 2, 3]
# new_list = [i + 1 for i in numbers]

name = "Angela"
letters_list = [letter for letter in name]

new_numbers = [2 * i for i in range(1, 10 + 1) if i % 2 != 0]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names = [name.upper() for name in names if len(name) >= 5]

# Ex 1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [i ** 2 for i in numbers]

# Ex 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)