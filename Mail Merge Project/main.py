# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

names_list = []
with open("./Input/Names/invited_names.txt") as f:
    data = f.read()

names = data.split()
for name in names:
    names_list.append(name)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

letter = letter_content.replace("[name]", "{name}")

for name in names_list:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
        f.write(f"Dear {name},\n\nYou are invited to my birthday this Saturday."
                f"\n\nHope you can make it!\n\nAngela\n")

#   Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#       Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#           Hint 3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
